"""Command-line interface for Codebase AI Prompt Generator."""

import argparse
import sys
from codebase_prompt_gen.core import generate_prompt


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description='Generate AI prompts from Git repositories')
    parser.add_argument('repo_path', type=str, nargs='?', default='.', 
                        help='Path to the Git repository (default: current directory)')
    parser.add_argument('--exclude', type=str, nargs='+', 
                        help='Patterns of files/directories to exclude (e.g., *.log)')
    parser.add_argument('--include', type=str, nargs='+', 
                        help='Patterns of files to include (e.g., *.py)')
    parser.add_argument('--output', type=str, 
                        help='Output file to write the prompt to')
    parser.add_argument('--no-gitignore', action='store_true',
                        help='Ignore .gitignore files (both local and global)')
    parser.add_argument('--version', action='store_true',
                        help='Show version information and exit')
    
    args = parser.parse_args()
    
    if args.version:
        from codebase_prompt_gen import __version__
        print(f"Codebase AI Prompt Generator v{__version__}")
        return 0
    
    try:
        prompt = generate_prompt(
            args.repo_path, 
            args.exclude, 
            args.include, 
            args.output,
            respect_gitignore=not args.no_gitignore
        )
        if not args.output:
            print(prompt)
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main()) 