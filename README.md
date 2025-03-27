# Codebase AI Prompt Generator

A tool to scan a Git repository and generate a comprehensive prompt for AI models, including file tree structure, file paths, and content.

## Features

- Creates a hierarchical file tree representation of a repository
- Includes file contents formatted for AI prompts
- Customizable file inclusion/exclusion via patterns
- Option to save output to a file or print to console
- Automatically respects local and global .gitignore files
- Cursor IDE integration with one command
- Automatically excludes `.git` directories
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

# Output to Cursor IDE rules directory
codebase-prompt --cursor

# Combine options
codebase-prompt /path/to/repository --exclude "node_modules" "*.pyc" --include "*.py" "*.js" --output prompt.md
```

## Default Exclusions

The tool automatically excludes certain files and directories to keep the output clean and relevant:

- `.git` directory and all its contents (always excluded)
- Files matching patterns in `.gitignore` files (unless `--no-gitignore` is used)
- Common build artifacts and cache directories (`__pycache__`, `*.pyc`, `node_modules`, etc.)

These exclusions help reduce noise and keep the generated prompt focused on the actual codebase content.

## .gitignore Support

By default, the tool respects both:
- The repository's local `.gitignore` file
- The user's global gitignore file (found via `git config --global --get core.excludesfile`)

Files matching any pattern in these files will be excluded from the output. To disable this feature, use the `--no-gitignore` flag.

## Cursor IDE Integration

The `--cursor` flag automatically generates a prompt file at `.cursor/rules/entire-codebase.mdc` in your repository. This allows Cursor IDE to use your codebase as context when you're working with AI assistance.

To use:

1. Navigate to your repository
2. Run `codebase-prompt --cursor`
3. The prompt will be available to Cursor IDE

The `--cursor` flag overrides the `--output` flag if both are specified.

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
- Integrate with Cursor IDE for better AI-assisted coding

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
