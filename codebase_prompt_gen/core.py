"""Core functionality for the Codebase AI Prompt Generator."""
from __future__ import annotations

import fnmatch
import logging
import subprocess
from pathlib import Path

from gitignore_parser import parse_gitignore

# Set of patterns that should always be excluded
ALWAYS_EXCLUDE = {".git", ".git/", ".git/**"}


def get_gitignore_matcher(gitignore_path: Path, root_path: Path) -> callable:
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
        return lambda path: False

    try:
        # Create a matcher from the gitignore file
        matcher = parse_gitignore(gitignore_path)

        # Wrap the matcher to handle both absolute and relative paths
        def path_matcher(file_path: str) -> bool:
            # Convert to Path object for easier manipulation
            path_obj = Path(file_path)

            # If the path is absolute, try to make it relative to the root path
            if path_obj.is_absolute():
                try:
                    rel_path = path_obj.relative_to(root_path)
                    return matcher(str(rel_path))
                except ValueError:
                    # If the path is not relative to root_path, it's outside the repo
                    # and should not be matched by the gitignore
                    return False
            else:
                # If already relative, use it directly
                return matcher(file_path)

        return path_matcher
    except Exception as e:
        logging.warning("Error parsing gitignore file %s: %s", gitignore_path, e)
        # Return a function that always returns False (doesn't ignore anything)
        return lambda path: False


def generate_file_tree(
    root_dir: str | Path,
    exclude_patterns: list[str] | None = None,
    include_patterns: list[str] | None = None,
    *,
    respect_gitignore: bool = True,
) -> tuple[list[str], list[dict[str, str]]]:
    """
    Generate a file tree structure for a given directory.

    Args:
        root_dir: The root directory to scan
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include
        respect_gitignore: Whether to respect .gitignore files

    Returns:
        Tuple of (file_tree, files_content) where file_tree is a list of
        formatted strings and files_content is a list of dictionaries with
        path and content keys

    """
    # Default exclude patterns
    default_excludes = ["__pycache__", "*.pyc", "node_modules", ".DS_Store"]
    root_path = Path(root_dir)

    # Always include the .git folder in exclusions
    if exclude_patterns is None:
        exclude_patterns = default_excludes + list(ALWAYS_EXCLUDE)
    else:
        # Make a copy to avoid modifying the original list and ensure .git is excluded
        exclude_patterns = exclude_patterns.copy()
        # Add default exclusions for .git
        for pattern in ALWAYS_EXCLUDE:
            if pattern not in exclude_patterns:
                exclude_patterns.append(pattern)

    # Set up gitignore matcher if requested
    gitignore_matcher = None
    if respect_gitignore:
        local_gitignore_path = root_path / ".gitignore"
        gitignore_matcher = get_gitignore_matcher(local_gitignore_path, root_path)

        # Try to get global gitignore matcher too
        try:
            result = subprocess.run(
                ["git", "config", "--global", "--get", "core.excludesfile"],
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                global_gitignore_path = Path(result.stdout.strip()).expanduser()
                global_matcher = get_gitignore_matcher(global_gitignore_path, root_path)

                # Combine both matchers
                local_matcher = gitignore_matcher

                def gitignore_matcher(path):
                    return local_matcher(path) or global_matcher(path)

        except (subprocess.SubprocessError, FileNotFoundError) as e:
            # Git not installed or other error
            logging.debug("Error getting global gitignore: %s", e)

    file_tree = []
    files_content = []

    # Get all files and directories
    all_files = []
    # Use Path.rglob instead of os.walk
    for path in sorted(root_path.rglob("*")):
        # Skip .git directory entirely
        if ".git" in path.parts:
            continue

        rel_path = path.relative_to(root_path)
        rel_path_str = str(rel_path)

        # Check if path should be excluded by gitignore
        if gitignore_matcher and gitignore_matcher(rel_path_str):
            continue

        # Check if path should be excluded by explicit patterns
        if any(fnmatch.fnmatch(rel_path_str, pattern) for pattern in exclude_patterns) or any(
            fnmatch.fnmatch(path.name, pattern) for pattern in exclude_patterns
        ):
            continue

        # Handle directories
        if path.is_dir():
            file_tree.append(f"📁 {rel_path_str}/")
        # Handle files
        elif path.is_file():
            # Apply include patterns if specified
            if (
                include_patterns
                and not any(fnmatch.fnmatch(path.name, pattern) for pattern in include_patterns)
                and not any(fnmatch.fnmatch(rel_path_str, pattern) for pattern in include_patterns)
            ):
                continue

            file_tree.append(f"📄 {rel_path_str}")
            all_files.append(rel_path_str)

    # Get content of all files
    for file_path in all_files:
        abs_path = root_path / file_path
        try:
            with abs_path.open(encoding="utf-8", errors="replace") as f:
                content = f.read()
                files_content.append({"path": file_path, "content": content})
        except OSError as e:
            files_content.append({"path": file_path, "content": f"[Error reading file: {e!s}]"})

    return file_tree, files_content


def generate_prompt(
    repo_path: str | Path,
    exclude_patterns: list[str] | None = None,
    include_patterns: list[str] | None = None,
    output_file: str | Path | None = None,
    *,
    respect_gitignore: bool = True,
) -> str:
    """
    Generate a prompt for AI models containing the file tree and file contents.

    Args:
        repo_path: Path to the Git repository
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include
        output_file: Optional file path to write the prompt to
        respect_gitignore: Whether to respect .gitignore files

    Returns:
        The generated prompt as a string

    """
    repo_path_obj = Path(repo_path).resolve()
    repo_name = repo_path_obj.name

    file_tree, files_content = generate_file_tree(
        repo_path_obj,
        exclude_patterns,
        include_patterns,
        respect_gitignore=respect_gitignore,
    )

    # Build the prompt
    prompt = f"# Repository: {repo_name}\n\n"

    # Add file tree
    prompt += "## File Tree Structure\n\n"
    prompt += "\n".join(file_tree)
    prompt += "\n\n"

    # Add file contents
    prompt += "## File Contents\n\n"
    for file_info in files_content:
        prompt += f"### {file_info['path']}\n\n"
        prompt += "```\n"
        prompt += file_info["content"]
        prompt += "\n```\n\n"

    # Write to file or print
    if output_file:
        output_path = Path(output_file)
        with output_path.open("w", encoding="utf-8") as f:
            f.write(prompt)

    return prompt
