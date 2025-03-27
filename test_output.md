# Repository: codebase-ai-prompt-generator

## File Tree Structure

📄 .gitignore
📄 .python-version
📄 LICENSE
📄 README.md
📄 main.py
📄 pyproject.toml

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

```

### .python-version

```
3.10

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

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/codebase-ai-prompt-generator.git
cd codebase-ai-prompt-generator

# Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Usage

```bash
# Basic usage (scans current directory)
python main.py

# Scan a specific repository
python main.py /path/to/repository

# Exclude specific file patterns
python main.py --exclude "*.log" "*.tmp" ".env"

# Include only specific file patterns
python main.py --include "*.py" "*.js" "*.html"

# Write output to a file
python main.py --output prompt.md

# Combine options
python main.py /path/to/repository --exclude "node_modules" "*.pyc" --include "*.py" "*.js" --output prompt.md
```

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```

### main.py

```
import os
import argparse
from pathlib import Path
import fnmatch


def generate_file_tree(root_dir, exclude_patterns=None, include_patterns=None):
    """Generate a file tree structure for a given directory."""
    if exclude_patterns is None:
        exclude_patterns = [".git", "__pycache__", "*.pyc", "node_modules", ".DS_Store"]
    
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
            # Skip excluded files
            if any(fnmatch.fnmatch(filename, pattern) for pattern in exclude_patterns):
                continue
                
            # Apply include patterns if specified
            if include_patterns and not any(fnmatch.fnmatch(filename, pattern) for pattern in include_patterns):
                continue
                
            file_path = os.path.join(rel_path, filename) if rel_path else filename
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


def generate_prompt(repo_path, exclude_patterns=None, include_patterns=None, output_file=None):
    """Generate a prompt for AI models containing the file tree and file contents."""
    repo_path = os.path.abspath(repo_path)
    repo_name = os.path.basename(repo_path)
    
    file_tree, files_content = generate_file_tree(repo_path, exclude_patterns, include_patterns)
    
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
    else:
        print(prompt)
    
    return prompt


def main():
    parser = argparse.ArgumentParser(description='Generate AI prompts from Git repositories')
    parser.add_argument('repo_path', type=str, nargs='?', default='.', 
                        help='Path to the Git repository (default: current directory)')
    parser.add_argument('--exclude', type=str, nargs='+', 
                        help='Patterns of files/directories to exclude (e.g., *.log)')
    parser.add_argument('--include', type=str, nargs='+', 
                        help='Patterns of files to include (e.g., *.py)')
    parser.add_argument('--output', type=str, 
                        help='Output file to write the prompt to')
    
    args = parser.parse_args()
    
    generate_prompt(args.repo_path, args.exclude, args.include, args.output)


if __name__ == "__main__":
    main()

```

### pyproject.toml

```
[project]
name = "codebase-ai-prompt-generator"
version = "0.1.0"
description = "Generate AI prompts from Git repositories with file tree structures and content"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
license = {text = "MIT"}
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.scripts]
codebase-ai-prompt = "main:main"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
packages = [""]

```

