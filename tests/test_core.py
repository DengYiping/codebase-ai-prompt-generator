"""Tests for core functionality."""

import fnmatch
import os
import tempfile
from unittest import mock

from codebase_prompt_gen.core import (
    generate_file_tree,
    generate_prompt,
)


def test_generate_file_tree() -> None:
    # Create a temporary directory structure
    with tempfile.TemporaryDirectory() as tempdir:
        # Create some files and directories
        os.makedirs(os.path.join(tempdir, "src"))
        os.makedirs(os.path.join(tempdir, "tests"))
        os.makedirs(os.path.join(tempdir, ".git"))

        with open(os.path.join(tempdir, "src", "main.py"), "w", encoding="utf-8") as f:
            f.write("def main():\n    pass\n")
        with open(os.path.join(tempdir, "README.md"), "w", encoding="utf-8") as f:
            f.write("# Test Project\n")
        with open(os.path.join(tempdir, ".gitignore"), "w", encoding="utf-8") as f:
            f.write("*.log\n")
        with open(os.path.join(tempdir, ".git", "config"), "w", encoding="utf-8") as f:
            f.write("# Git config\n")

        # Mock the gitignore parser to return a simple matcher that matches *.log
        def mock_parse_gitignore(gitignore_file):
            # Read the patterns from the file
            patterns = []
            with open(gitignore_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        patterns.append(line)

            # Return a matcher function that uses fnmatch to match patterns
            def matcher(path_str):
                # Convert backslashes to forward slashes
                path_str = path_str.replace("\\", "/")
                # Extract filename
                filename = os.path.basename(path_str)

                # Check if path matches any pattern
                for pattern in patterns:
                    if "*" in pattern:
                        # It's a glob pattern, use fnmatch
                        if fnmatch.fnmatch(filename, pattern) or fnmatch.fnmatch(path_str, pattern):
                            return True
                    # It's a direct path match
                    elif pattern in path_str:
                        return True
                return False

            return matcher

        with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
            # Test without any custom patterns
            file_tree, files_content = generate_file_tree(tempdir)

            # Check file tree structure
            assert any("src/" in item for item in file_tree)
            assert any("tests/" in item for item in file_tree)
            assert any("README.md" in item for item in file_tree)

            # Verify .git directory files are excluded
            for item in file_tree:
                assert ".git/" not in item
                assert ".git\\" not in item

            for info in files_content:
                assert not info["path"].startswith(".git/")
                assert not info["path"].startswith(".git\\")

            # Check content
            assert any(info["path"] == "README.md" for info in files_content)
            assert any(info["path"] == "src/main.py" for info in files_content)

            # Test with custom exclude patterns
            file_tree, files_content = generate_file_tree(tempdir, exclude_patterns=["*.md"])
            assert not any("README.md" in item for item in file_tree)

            # Test with custom include patterns
            file_tree, files_content = generate_file_tree(tempdir, include_patterns=["*.py"])
            assert any("main.py" in item for item in file_tree)
            assert not any("README.md" in item for item in file_tree)

            # Test with respect_gitignore=False
            with open(os.path.join(tempdir, "test.log"), "w", encoding="utf-8") as f:
                f.write("Test log file\n")

            # With respect_gitignore=True (default), the log file should be excluded
            file_tree, _ = generate_file_tree(tempdir)
            assert not any("test.log" in item for item in file_tree)

            # With respect_gitignore=False, the log file should be included
            file_tree, _ = generate_file_tree(tempdir, respect_gitignore=False)
            assert any("test.log" in item for item in file_tree)


def test_always_exclude_git() -> None:
    """Test that .git is always excluded regardless of settings."""
    with tempfile.TemporaryDirectory() as tempdir:
        os.makedirs(os.path.join(tempdir, ".git"))
        with open(os.path.join(tempdir, ".git", "config"), "w", encoding="utf-8") as f:
            f.write("# Git config\n")

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda path: False  # No ignores from gitignore

        with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
            # Try to include .git explicitly
            file_tree, _ = generate_file_tree(tempdir, include_patterns=[".git", ".git/**"])

            # Verify .git is still excluded
            for item in file_tree:
                assert ".git/" not in item
                assert ".git\\" not in item


def test_generate_prompt() -> None:
    """Test the generate_prompt function."""
    with tempfile.TemporaryDirectory() as tempdir:
        # Create a simple test file
        with open(os.path.join(tempdir, "test.py"), "w", encoding="utf-8") as f:
            f.write("print('Hello World')\n")

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda path: False  # No ignores from gitignore

        with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
            # Test with output to stdout
            prompt = generate_prompt(tempdir)

            # Check prompt content
            assert "# Repository:" in prompt
            assert "## File Tree Structure" in prompt
            assert "## File Contents" in prompt
            assert "### test.py" in prompt

            # Test with output to file
            output_file = os.path.join(tempdir, "output.md")
            generate_prompt(tempdir, output_file=output_file)

            # Verify file was created
            assert os.path.exists(output_file)

            # Read the content and verify
            with open(output_file, encoding="utf-8") as f:
                content = f.read()
                assert "# Repository:" in content
                assert "### test.py" in content

            # Test with various parameters
            prompt = generate_prompt(
                tempdir,
                exclude_patterns=["*.md"],
                include_patterns=["*.py"],
                respect_gitignore=False,
            )
            assert "### test.py" in prompt
