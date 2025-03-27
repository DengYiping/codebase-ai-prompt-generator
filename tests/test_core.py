"""Tests for core functionality."""

import os
import subprocess
import tempfile
from pathlib import Path
from unittest import mock

from codebase_prompt_gen.core import (
    ALWAYS_EXCLUDE,
    generate_file_tree,
    generate_prompt,
    get_global_gitignore_patterns,
    gitignore_to_pattern,
    read_gitignore_file,
)


def test_read_gitignore_file():
    # Create a temporary .gitignore file
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("# Comment line\n")
        f.write("\n")  # Empty line
        f.write("*.log\n")
        f.write("node_modules/\n")
        f.write("!important.log\n")
        temp_gitignore = f.name

    try:
        # Test reading the file
        patterns = read_gitignore_file(temp_gitignore)
        assert len(patterns) == 3
        assert "*.log" in patterns
        assert "node_modules/" in patterns
        assert "!important.log" in patterns
    finally:
        # Clean up
        os.unlink(temp_gitignore)

    # Test with non-existent file
    patterns = read_gitignore_file("/path/that/does/not/exist")
    assert patterns == []


def test_gitignore_to_pattern():
    # Test normal pattern
    assert gitignore_to_pattern("*.log") == "*.log"

    # Test directory pattern
    assert gitignore_to_pattern("node_modules/") == "node_modules"

    # Test negation pattern
    assert gitignore_to_pattern("!important.log") == "important.log"

    # Test double-star pattern
    assert gitignore_to_pattern("**/*.log") == "**/*.log"


def test_get_global_gitignore_patterns():
    # Test with a mock subprocess result
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("*.log\n")
        f.write("node_modules/\n")
        temp_gitignore = f.name

    try:
        # Mock the subprocess call to return our temp file
        mock_result = mock.MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = temp_gitignore

        with mock.patch("subprocess.run", return_value=mock_result):
            patterns = get_global_gitignore_patterns()
            assert len(patterns) == 2
            assert "*.log" in patterns
            assert "node_modules/" in patterns
    finally:
        # Clean up
        os.unlink(temp_gitignore)

    # Test with a failed subprocess result
    mock_result = mock.MagicMock()
    mock_result.returncode = 1

    with mock.patch("subprocess.run", return_value=mock_result):
        patterns = get_global_gitignore_patterns()
        assert patterns == []

    # Test with a subprocess error
    with mock.patch("subprocess.run", side_effect=subprocess.SubprocessError):
        patterns = get_global_gitignore_patterns()
        assert patterns == []


def test_generate_file_tree():
    # Create a temporary directory structure
    with tempfile.TemporaryDirectory() as tempdir:
        # Create some files and directories
        os.makedirs(os.path.join(tempdir, "src"))
        os.makedirs(os.path.join(tempdir, "tests"))
        os.makedirs(os.path.join(tempdir, ".git"))

        with open(os.path.join(tempdir, "src", "main.py"), "w") as f:
            f.write("def main():\n    pass\n")
        with open(os.path.join(tempdir, "README.md"), "w") as f:
            f.write("# Test Project\n")
        with open(os.path.join(tempdir, ".gitignore"), "w") as f:
            f.write("*.log\n")
        with open(os.path.join(tempdir, ".git", "config"), "w") as f:
            f.write("# Git config\n")

        # Test without any custom patterns
        file_tree, files_content = generate_file_tree(tempdir)

        # Check file tree structure
        assert any("src/" in item for item in file_tree)
        assert any("tests/" in item for item in file_tree)
        assert any("README.md" in item for item in file_tree)

        # Verify .git directory files are excluded
        for item in file_tree:
            assert ".git/" not in item and ".git\\" not in item

        for info in files_content:
            assert not info["path"].startswith(".git/") and not info["path"].startswith(".git\\")

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
        with open(os.path.join(tempdir, "test.log"), "w") as f:
            f.write("Test log file\n")

        # With respect_gitignore=True (default), the log file should be excluded
        file_tree, _ = generate_file_tree(tempdir)
        assert not any("test.log" in item for item in file_tree)

        # With respect_gitignore=False, the log file should be included
        file_tree, _ = generate_file_tree(tempdir, respect_gitignore=False)
        assert any("test.log" in item for item in file_tree)


def test_always_exclude_git():
    """Test that .git is always excluded regardless of settings."""
    with tempfile.TemporaryDirectory() as tempdir:
        os.makedirs(os.path.join(tempdir, ".git"))
        with open(os.path.join(tempdir, ".git", "config"), "w") as f:
            f.write("# Git config\n")

        # Try to include .git explicitly
        file_tree, _ = generate_file_tree(tempdir, include_patterns=[".git", ".git/**"])

        # Verify .git is still excluded
        for item in file_tree:
            assert ".git/" not in item and ".git\\" not in item


def test_generate_prompt():
    """Test the generate_prompt function."""
    with tempfile.TemporaryDirectory() as tempdir:
        # Create a simple test file
        with open(os.path.join(tempdir, "test.py"), "w") as f:
            f.write("print('Hello World')\n")

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
        with open(output_file, "r") as f:
            content = f.read()
            assert "# Repository:" in content
            assert "### test.py" in content

        # Test with various parameters
        prompt = generate_prompt(
            tempdir, exclude_patterns=["*.md"], include_patterns=["*.py"], respect_gitignore=False
        )
        assert "### test.py" in prompt
