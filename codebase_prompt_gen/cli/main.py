"""Command-line interface for Codebase AI Prompt Generator."""

import argparse
import os
import sys
from typing import Optional

from codebase_prompt_gen.core import generate_prompt

# Version information
__version__ = "0.1.0"


def main() -> Optional[int]:
    """Main entry point for the CLI."""
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
    output_file = args.output
    if args.cursor:
        if args.output:
            print("Warning: --cursor flag overrides --output flag", file=sys.stderr)

        # Get the absolute path to the repository
        repo_path = os.path.abspath(args.repo_path)

        # Create the .cursor/rules directory if it doesn't exist
        cursor_dir = os.path.join(repo_path, ".cursor", "rules")
        os.makedirs(cursor_dir, exist_ok=True)

        # Set the output file path
        output_file = os.path.join(cursor_dir, "entire-codebase.mdc")

    try:
        prompt = generate_prompt(
            args.repo_path,
            args.exclude,
            args.include,
            output_file,
            respect_gitignore=not args.no_gitignore,
        )
        if not args.output and not args.cursor:
            # Print to stdout if no output file is specified
            print(prompt)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
