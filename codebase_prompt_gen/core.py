import fnmatch  # Import fnmatch
import logging
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

from gitignore_parser import parse_gitignore

# Set of patterns that should always be excluded
ALWAYS_EXCLUDE = {".git", ".git/", ".git/**"}


def get_gitignore_matcher(gitignore_path: Path, root_path: Path) -> Callable[[Path], bool]:
    """
    Get a matcher function for a gitignore file.

    Args:
        gitignore_path: Path to the .gitignore file
        root_path: Root path for the repository

    Returns:
        A function that returns True if the path matches any gitignore pattern
    """
    if not gitignore_path.exists():
        # Return a function that always returns False (doesn't ignore anything)
        return lambda _: False

    # Create a matcher from the gitignore file
    try:
        matcher = parse_gitignore(gitignore_path)

        # Wrap the matcher to handle both absolute and relative paths correctly
        def path_matcher(file_path: Path) -> bool:
            # Use absolute paths for reliable matching within the gitignore library context
            try:
                # Convert to Path object for easier manipulation if it's not already
                abs_path = (
                    file_path if file_path.is_absolute() else root_path.absolute() / file_path
                )
                # Make relative to the root_path where .gitignore is expected to apply
                rel_path = abs_path.relative_to(root_path.absolute())
                return matcher(str(rel_path)) or matcher(str(abs_path))
            except ValueError:
                return matcher(str(file_path))
            except Exception as inner_e:
                logging.debug("Error during gitignore matching for %s: %s", file_path, inner_e)
                return False  # Treat errors as non-matches

    except Exception as e:
        logging.warning("Error parsing gitignore file %s: %s", gitignore_path, e)
        return lambda _: False

    return path_matcher


def generate_file_tree(
    root_dir: Path,
    exclude_patterns: list[str],
    include_patterns: list[str],
    respect_gitignore: bool = True,
) -> tuple[list[str], list[tuple[Path, Callable[[], str]]]]:
    """
    Generate a file tree structure for a given directory, respecting includes/excludes.

    Args:
        root_dir: The root directory to scan
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include (files only)
        respect_gitignore: Whether to respect .gitignore files

    Returns:
        Tuple of (file_tree, files_content) where file_tree is a list of
        formatted strings representing the directory structure, and
        files_content is a list of tuples, each containing the relative
        file path and a function to get its content.
    """
    file_tree: list[str] = []
    files_to_read: list[tuple[Path, Callable[[], str]]] = (
        []
    )  # Store (relative_path, content_getter)
    combined_exclude = set(exclude_patterns) | ALWAYS_EXCLUDE

    # Set up gitignore matcher if requested
    gitignore_matcher: Callable[[Path], bool] = lambda x: False

    if respect_gitignore:
        local_gitignore_path = root_dir / ".gitignore"
        local_matcher = get_gitignore_matcher(local_gitignore_path, root_dir)

        global_matcher: Callable[[Path], bool] = lambda _: False

        # Try to get global gitignore matcher too
        try:
            result = subprocess.run(
                ["git", "config", "--global", "--get", "core.excludesfile"],
                capture_output=True,
                text=True,
                check=False,
                encoding="utf-8",  # Explicitly set encoding
            )
            if result.returncode == 0 and result.stdout and result.stdout.strip():
                global_gitignore_path = Path(result.stdout.strip()).expanduser()
                if global_gitignore_path.exists():
                    global_matcher = get_gitignore_matcher(global_gitignore_path, root_dir)
                else:
                    logging.debug("Global gitignore file not found at: %s", global_gitignore_path)

        except (subprocess.SubprocessError, FileNotFoundError) as e:
            # Git not installed or other error
            logging.debug("Could not get global gitignore: %s", e)
        except Exception as e:
            logging.warning("Unexpected error getting global gitignore: %s", e)

        def combined_matcher(path: Path) -> bool:
            return local_matcher(path) or global_matcher(path)

        gitignore_matcher = combined_matcher

    for path in sorted(root_dir.rglob("*")):
        try:
            rel_path = path.relative_to(root_dir)
            rel_path_str = str(rel_path)
        except ValueError:
            # Should not happen with rglob starting from root_dir, but handle defensively
            logging.warning("Path %s could not be made relative to %s", path, root_dir)
            continue

        # --- Exclusion checks ---

        # 1. Check explicit exclude patterns and ALWAYS_EXCLUDE
        # We check against the relative path string.
        # Add '/' suffix check for directory patterns like 'node_modules/'
        is_explicitly_excluded = any(
            fnmatch.fnmatch(rel_path_str, pattern)
            or (path.is_dir() and fnmatch.fnmatch(rel_path_str + "/", pattern))
            for pattern in combined_exclude
        )
        if is_explicitly_excluded:
            if path.is_dir():
                logging.debug(
                    "Excluding directory and its contents based on exclude patterns: %s", rel_path
                )
                # To prevent rglob from descending into excluded directories,
                # this check ideally happens before yielding, but rglob yields all paths first.
                # We rely on filtering *after* rglob generates the path.
                # A future optimization might involve os.walk for finer control.
            else:
                logging.debug("Excluding file based on exclude patterns: %s", rel_path)
            continue  # Skip this path

        # 2. Check gitignore patterns (if enabled)
        # Pass the absolute path to the matcher wrapper for robust matching
        if respect_gitignore and gitignore_matcher(path):
            logging.debug("Excluding path based on gitignore: %s", rel_path)
            continue  # Skip this path

        # --- Inclusion logic ---

        # Handle directories: Add to tree if not excluded/ignored
        if path.is_dir():
            file_tree.append(f"📁 {rel_path}/")  # Add trailing slash for clarity
            continue  # Handled directory, move to the next path

        # Handle files: Check include patterns if they exist
        elif path.is_file():
            should_include_file = True  # Default to include
            if include_patterns:
                # If include_patterns are specified, the file MUST match at least one
                should_include_file = any(
                    fnmatch.fnmatch(rel_path_str, pattern) for pattern in include_patterns
                )

            if should_include_file:
                logging.debug("Including file: %s", rel_path)
                file_tree.append(f"📄 {rel_path}")
                # Store relative path for the tree/prompt, and a getter capturing the absolute path
                files_to_read.append((rel_path, build_file_content_getter(path)))
            else:
                logging.debug("Skipping file %s due to not matching include patterns", rel_path)

        # Note: Symlinks and other file types are currently ignored by this logic

    return file_tree, files_to_read


def build_file_content_getter(file_path: Path) -> Callable[[], str]:
    """Builds a closure to lazily read file content."""
    absolute_path = file_path.resolve()  # Ensure we capture the absolute path

    def get_content() -> str:
        try:
            # Specify encoding, handle potential errors
            with absolute_path.open("r", encoding="utf-8", errors="replace") as f:
                return f.read()
        except FileNotFoundError:
            logging.exception("File not found when trying to read content: %s", absolute_path)
            return "[Error: File not found]"
        except Exception:
            logging.exception("Error reading file %s", absolute_path)
            # Return error message in content - useful for debugging in the prompt
            return ""

    return get_content


def generate_prompt(
    repo_path: Path,
    exclude_patterns: list[str],
    include_patterns: list[str],
    output_file: Path | None = None,
    *,
    respect_gitignore: bool = True,
) -> None:
    """
    Generate a prompt for AI models containing the file tree and file contents.

    Args:
        repo_path: Path to the Git repository root directory
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include (files only)
        output_file: Optional file path to write the prompt to
        respect_gitignore: Whether to respect .gitignore files

    Returns:
        None. Prints to stdout or writes to the specified file.
    """
    # Configure basic logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    try:
        repo_path_obj = Path(repo_path).resolve(strict=True)  # Ensure path exists
        repo_name = repo_path_obj.name
    except FileNotFoundError:
        logging.exception("Repository path not found: %s", repo_path)
        print(f"Error: Repository path not found: {repo_path}")
        return
    except Exception:
        logging.exception("Error resolving repository path %s", repo_path)
        return

    logging.info("Generating file tree for %s", repo_path_obj)
    logging.info("Exclude patterns: %s", exclude_patterns)
    logging.info("Include patterns: %s", include_patterns)
    logging.info("Respect gitignore: %s", respect_gitignore)

    file_tree, files_content = generate_file_tree(
        repo_path_obj,
        exclude_patterns,
        include_patterns,
        respect_gitignore=respect_gitignore,
    )

    # Build the prompt header
    prompt_header = f"# Repository: {repo_name}\n\n"
    prompt_header += "## File Tree Structure\n\n"
    if file_tree:
        prompt_header += "```\n" + "\n".join(file_tree) + "\n```"
    else:
        prompt_header += "No files or directories found matching the criteria."
    prompt_header += "\n\n"
    prompt_header += "## File Contents\n\n"

    # --- Output Handling ---
    writer: Callable[[str], int | None] = lambda _: None

    output_stream = None
    try:
        if output_file:
            output_path = Path(output_file).resolve()
            output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
            output_stream = output_path.open("w", encoding="utf-8")
            writer = output_stream.write
            logging.info("Writing prompt to file: %s", output_path)
        else:
            # Use print for stdout, handling potential encoding issues

            writer = lambda text: print(text, end="", flush=True, file=sys.stdout)

            logging.info("Printing prompt to standard output.")

        # Write header
        writer(prompt_header)

        # Write file contents incrementally
        if not files_content:
            writer("No file contents included based on criteria.\n")

        for file_path, content_getter in files_content:
            # Use the relative path for display
            relative_path_str = str(file_path)
            writer(f"### `{relative_path_str}`\n\n")
            # Determine language for markdown code block if possible (simple extension mapping)
            lang = file_path.suffix.lstrip(".") if file_path.suffix else ""
            writer(f"```{(lang)}\n")  # Add lang hint if available
            # Call the getter to read content only when needed
            try:
                content = content_getter()
                writer(content)
            except Exception:
                # Should be caught by getter, but as a fallback
                logging.exception("Unexpected error getting content for %s", file_path)
            writer("\n```\n\n")

        logging.info("Prompt generation complete.")

    except OSError:
        logging.exception("Error writing to output %s", output_file or "stdout")
    except Exception:
        logging.exception("An unexpected error occurred during prompt generation: %s")
    finally:
        if output_stream:
            output_stream.close()
