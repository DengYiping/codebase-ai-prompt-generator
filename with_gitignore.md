# Repository: codebase-ai-prompt-generator

## File Tree Structure

📄 .gitignore
📄 LICENSE
📄 README.md
📄 pyproject.toml
📁 codebase_prompt_gen/
📄 codebase_prompt_gen/__init__.py
📄 codebase_prompt_gen/core.py
📁 codebase_prompt_gen/cli/
📄 codebase_prompt_gen/cli/__init__.py
📄 codebase_prompt_gen/cli/main.py

## File Contents

### .gitignore

```
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv
venv/
ENV/

# Testing and output files
test_output.md
cli_test_output.md

# IDEs and editors
.vscode/
.idea/
*.swp
*~
.DS_Store

```

### LICENSE

```
MIT License

Copyright (c) 2023 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
```

### README.md

```
# Codebase AI Prompt Generator

A tool to scan a Git repository and generate a comprehensive prompt for AI models, including file tree structure, file paths, and content.

## Features

- Creates a hierarchical file tree representation of a repository
- Includes file contents formatted for AI prompts
- Customizable file inclusion/exclusion via patterns
- Option to save output to a file or print to console
- Automatically respects local and global .gitignore files
- Installable CLI tool

## Installation

```bash
# From PyPI (recommended)
pip install codebase-ai-prompt-generator

# From source
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator
pip install -e .
```

## Usage

After installation, you can use the `codebase-prompt` command directly from your terminal:

```bash
# Basic usage (scans current directory)
codebase-prompt

# Scan a specific repository
codebase-prompt /path/to/repository

# Exclude specific file patterns
codebase-prompt --exclude "*.log" "*.tmp" ".env"

# Include only specific file patterns
codebase-prompt --include "*.py" "*.js" "*.html"

# Write output to a file
codebase-prompt --output prompt.md

# Show version information
codebase-prompt --version

# Ignore .gitignore files (both local and global)
codebase-prompt --no-gitignore

# Combine options
codebase-prompt /path/to/repository --exclude "node_modules" "*.pyc" --include "*.py" "*.js" --output prompt.md
```

## .gitignore Support

By default, the tool respects both:
- The repository's local `.gitignore` file
- The user's global gitignore file (found via `git config --global --get core.excludesfile`)

Files matching any pattern in these files will be excluded from the output. To disable this feature, use the `--no-gitignore` flag.

## Example Output

The generated prompt will have the following structure:

```
# Repository: repo-name

## File Tree Structure

📁 src/
📄 src/main.py
📄 src/utils.py
📁 tests/
📄 tests/test_main.py
📄 README.md

## File Contents

### src/main.py

```python
def main():
    print("Hello World")
```

### src/utils.py

```python
def helper():
    return "Helper function"
```

...
```

## Use Cases

- Generate prompts for AI code assistants to understand your entire codebase
- Create documentation snapshots of your repository
- Share codebase context with AI models for better assistance
- Provide comprehensive context to LLMs for code-related questions

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```

### pyproject.toml

```
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "codebase-ai-prompt-generator"
version = "0.1.0"
description = "Generate AI prompts from Git repositories with file tree structures and content"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
keywords = ["ai", "prompt", "git", "code", "repository"]
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/codebase-ai-prompt-generator"
"Bug Tracker" = "https://github.com/yourusername/codebase-ai-prompt-generator/issues"

[project.scripts]
codebase-prompt = "codebase_prompt_gen.cli.main:main"

[tool.setuptools]
packages = ["codebase_prompt_gen", "codebase_prompt_gen.cli"]

```

### codebase_prompt_gen/__init__.py

```
"""Codebase AI Prompt Generator.

A tool to scan Git repositories and generate comprehensive prompts for AI models.
"""

__version__ = "0.1.0" 
```

### codebase_prompt_gen/core.py

```
"""Core functionality for the Codebase AI Prompt Generator."""

import os
import fnmatch
from pathlib import Path
import subprocess


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
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith('#'):
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
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
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
    if gitignore_pattern.startswith('!'):
        # Negation is not directly supported in fnmatch
        # Just return the pattern without the negation for now
        gitignore_pattern = gitignore_pattern[1:]
    
    # Handle directory-specific patterns (ending with /)
    if gitignore_pattern.endswith('/'):
        gitignore_pattern = gitignore_pattern[:-1]
    
    # Convert ** to match any number of directories
    if '**' in gitignore_pattern:
        gitignore_pattern = gitignore_pattern.replace('**/', '**/').replace('/**', '/**')
    
    return gitignore_pattern


def generate_file_tree(root_dir, exclude_patterns=None, include_patterns=None, respect_gitignore=True):
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
    if exclude_patterns is None:
        exclude_patterns = [".git", "__pycache__", "*.pyc", "node_modules", ".DS_Store"]
    else:
        # Make a copy to avoid modifying the original list
        exclude_patterns = exclude_patterns.copy()
    
    # Add gitignore patterns if requested
    if respect_gitignore:
        # Add global gitignore patterns
        global_patterns = get_global_gitignore_patterns()
        for pattern in global_patterns:
            glob_pattern = gitignore_to_pattern(pattern)
            if glob_pattern and glob_pattern not in exclude_patterns:
                exclude_patterns.append(glob_pattern)
        
        # Add local gitignore patterns
        local_gitignore_path = os.path.join(root_dir, '.gitignore')
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
        # Skip excluded directories
        dirnames[:] = [d for d in dirnames if not any(fnmatch.fnmatch(d, pattern) for pattern in exclude_patterns)]
        
        # Process files
        rel_path = os.path.relpath(dirpath, root_dir)
        if rel_path == '.':
            rel_path = ''
        
        # Add directory to tree
        if rel_path:
            file_tree.append(f"📁 {rel_path}/")
        
        # Add files to tree
        for filename in sorted(filenames):
            # Check if full path matches any exclude pattern
            file_path = os.path.join(rel_path, filename) if rel_path else filename
            if any(fnmatch.fnmatch(file_path, pattern) for pattern in exclude_patterns) or \
               any(fnmatch.fnmatch(filename, pattern) for pattern in exclude_patterns):
                continue
                
            # Apply include patterns if specified
            if include_patterns and not any(fnmatch.fnmatch(filename, pattern) for pattern in include_patterns) and \
               not any(fnmatch.fnmatch(file_path, pattern) for pattern in include_patterns):
                continue
                
            file_tree.append(f"📄 {file_path}")
            all_files.append(file_path)
    
    # Get content of all files
    for file_path in all_files:
        abs_path = os.path.join(root_dir, file_path)
        try:
            with open(abs_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
                files_content.append({
                    "path": file_path,
                    "content": content
                })
        except Exception as e:
            files_content.append({
                "path": file_path,
                "content": f"[Error reading file: {str(e)}]"
            })
    
    return file_tree, files_content


def generate_prompt(repo_path, exclude_patterns=None, include_patterns=None, output_file=None, respect_gitignore=True):
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
    
    file_tree, files_content = generate_file_tree(repo_path, exclude_patterns, include_patterns, respect_gitignore)
    
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
        prompt += file_info['content']
        prompt += "\n```\n\n"
    
    # Write to file or print
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
        print(f"Prompt written to {output_file}")
    
    return prompt 
```

### codebase_prompt_gen/cli/__init__.py

```
"""Command-line interface for Codebase AI Prompt Generator.""" 
```

### codebase_prompt_gen/cli/main.py

```
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
```

