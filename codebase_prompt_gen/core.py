"""Core functionality for the Codebase AI Prompt Generator."""
from __future__ import annotations

import fnmatch
import os
import subprocess

# Set of patterns that should always be excluded
ALWAYS_EXCLUDE = {".git", ".git/", ".git/**"}


def read_gitignore_file(file_path):
    """Read a .gitignore file and return a list of patterns.

    Args:
        file_path: Path to the .gitignore file

    Returns:
        List of gitignore patterns

    """
    patterns = []
    if os.path.exists(file_path):
        try:
            with open(file_path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith("#"):
                        patterns.append(line)
        except Exception:
            # Silently fail if the file can't be read
            pass
    return patterns


def get_global_gitignore_patterns():
    """Get global gitignore patterns.

    Returns:
        List of global gitignore patterns

    """
    try:
        # Try to get the global gitignore file path
        result = subprocess.run(
            ["git", "config", "--global", "--get", "core.excludesfile"],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode == 0 and result.stdout.strip():
            global_gitignore_path = os.path.expanduser(result.stdout.strip())
            return read_gitignore_file(global_gitignore_path)
    except (subprocess.SubprocessError, FileNotFoundError):
        # Git not installed or other error
        pass

    return []


def gitignore_to_pattern(gitignore_pattern):
    """Convert a gitignore pattern to a glob pattern.

    Args:
        gitignore_pattern: A pattern from a .gitignore file

    Returns:
        A glob pattern compatible with fnmatch

    """
    # Handle negation (patterns that start with !)
    if gitignore_pattern.startswith("!"):
        # Negation is not directly supported in fnmatch
        # Just return the pattern without the negation for now
        gitignore_pattern = gitignore_pattern[1:]

    # Handle directory-specific patterns (ending with /)
    if gitignore_pattern.endswith("/"):
        gitignore_pattern = gitignore_pattern[:-1]

    # Convert ** to match any number of directories
    if "**" in gitignore_pattern:
        gitignore_pattern = gitignore_pattern.replace("**/", "**/").replace("/**", "/**")

    return gitignore_pattern


def generate_file_tree(
    root_dir,
    exclude_patterns=None,
    include_patterns=None,
    respect_gitignore=True,
) -> tuple[str, str]:
    """Generate a file tree structure for a given directory.

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

    # Add gitignore patterns if requested
    if respect_gitignore:
        # Add global gitignore patterns
        global_patterns = get_global_gitignore_patterns()
        for pattern in global_patterns:
            glob_pattern = gitignore_to_pattern(pattern)
            if glob_pattern and glob_pattern not in exclude_patterns:
                exclude_patterns.append(glob_pattern)

        # Add local gitignore patterns
        local_gitignore_path = os.path.join(root_dir, ".gitignore")
        local_patterns = read_gitignore_file(local_gitignore_path)
        for pattern in local_patterns:
            glob_pattern = gitignore_to_pattern(pattern)
            if glob_pattern and glob_pattern not in exclude_patterns:
                exclude_patterns.append(glob_pattern)

    file_tree = []
    files_content = []

    # Get all files and directories
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip .git directory entirely
        if ".git" in dirpath.split(os.path.sep):
            continue

        # Skip excluded directories
        dirnames[:] = [
            d
            for d in dirnames
            if d != ".git" and not any(fnmatch.fnmatch(d, pattern) for pattern in exclude_patterns)
        ]

        # Process files
        rel_path = os.path.relpath(dirpath, root_dir)
        if rel_path == ".":
            rel_path = ""

        # Add directory to tree
        if rel_path:
            file_tree.append(f"📁 {rel_path}/")

        # Add files to tree
        for filename in sorted(filenames):
            # Check if full path matches any exclude pattern
            file_path = os.path.join(rel_path, filename) if rel_path else filename
            if any(fnmatch.fnmatch(file_path, pattern) for pattern in exclude_patterns) or any(
                fnmatch.fnmatch(filename, pattern) for pattern in exclude_patterns
            ):
                continue

            # Apply include patterns if specified
            if (
                include_patterns
                and not any(fnmatch.fnmatch(filename, pattern) for pattern in include_patterns)
                and not any(fnmatch.fnmatch(file_path, pattern) for pattern in include_patterns)
            ):
                continue

            file_tree.append(f"📄 {file_path}")
            all_files.append(file_path)

    # Get content of all files
    for file_path in all_files:
        abs_path = os.path.join(root_dir, file_path)
        try:
            with open(abs_path, encoding="utf-8", errors="replace") as f:
                content = f.read()
                files_content.append({"path": file_path, "content": content})
        except Exception as e:
            files_content.append({"path": file_path, "content": f"[Error reading file: {e!s}]"})

    return file_tree, files_content


def generate_prompt(
    repo_path,
    exclude_patterns=None,
    include_patterns=None,
    output_file=None,
    respect_gitignore=True,
) -> str:
    """Generate a prompt for AI models containing the file tree and file contents.

    Args:
        repo_path: Path to the Git repository
        exclude_patterns: List of glob patterns to exclude
        include_patterns: List of glob patterns to include
        output_file: Optional file path to write the prompt to
        respect_gitignore: Whether to respect .gitignore files

    Returns:
        The generated prompt as a string

    """
    repo_path = os.path.abspath(repo_path)
    repo_name = os.path.basename(repo_path)

    file_tree, files_content = generate_file_tree(
        repo_path,
        exclude_patterns,
        include_patterns,
        respect_gitignore,
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
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(prompt)

    return prompt
