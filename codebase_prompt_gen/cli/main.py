"""Command-line interface for Codebase AI Prompt Generator."""

import argparse
import logging
import sys
from pathlib import Path

from codebase_prompt_gen.core import generate_prompt

# Version information
__version__ = "0.1.0"
version_info = tuple(int(part) for part in __version__.split("."))

__all__ = ["__version__", "version_info"]


def main() -> int | None:
    """Execute the main CLI functionality."""
    parser = argparse.ArgumentParser(description="Generate AI prompts from Git repositories")
    parser.add_argument(
        "repo_path",
        type=str,
        nargs="?",
        default=".",
        help="Path to the Git repository (default: current directory)",
    )
    parser.add_argument(
        "--exclude",
        type=str,
        nargs="+",
        help="Patterns of files/directories to exclude (e.g., *.log)",
    )
    parser.add_argument(
        "--include",
        type=str,
        nargs="+",
        help="Patterns of files to include (e.g., *.py)",
    )
    parser.add_argument("--output", type=str, help="Output file to write the prompt to")
    parser.add_argument(
        "--cursor",
        action="store_true",
        help="Output to .cursor/rules/entire-codebase.mdc for Cursor IDE integration",
    )
    parser.add_argument(
        "--no-gitignore",
        action="store_true",
        help="Ignore .gitignore files (both local and global)",
    )
    parser.add_argument("--version", action="store_true", help="Show version information and exit")

    args = parser.parse_args()

    if args.version:
        print(f"Codebase AI Prompt Generator v{__version__}")
        return 0

    # Handle cursor output path
    output_file = None

    if args.output:
        output_file = Path(args.output)

    if args.cursor:
        if args.output:
            logging.warning("Warning: --cursor flag overrides --output flag\n")

        # Get the absolute path to the repository
        repo_path = Path(args.repo_path).resolve()

        # Create the .cursor/rules directory if it doesn't exist
        cursor_dir = repo_path / ".cursor" / "rules"
        cursor_dir.mkdir(parents=True, exist_ok=True)

        # Set the output file path
        output_file = cursor_dir / "entire-codebase.mdc"

    try:
        generate_prompt(
            Path(args.repo_path),
            args.exclude or [],
            args.include or [],
            output_file,
            respect_gitignore=not args.no_gitignore,
        )
    except (OSError, ValueError, FileNotFoundError):
        logging.exception("Error generating prompt!")
        return 1
    except Exception as e:
        sys.stderr.write(f"Error: {e!s}\n")
        logging.exception("Unexpected error generating prompt!")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
