"""Tests for core functionality."""

import fnmatch
import tempfile
from pathlib import Path
from unittest import mock

from codebase_prompt_gen.core import (
    generate_file_tree,
    generate_prompt,
    get_gitignore_matcher,
)


def test_generate_file_tree_original() -> None:
    # Create a temporary directory structure
    with tempfile.TemporaryDirectory() as tempdir:
        temp_path = Path(tempdir)
        # Create some files and directories
        (temp_path / "src").mkdir(parents=True)
        (temp_path / "tests").mkdir(parents=True)
        (temp_path / ".git").mkdir(parents=True)

        (temp_path / "src" / "main.py").write_text("def main():\n    pass\n")
        (temp_path / "README.md").write_text("# Test Project\n")
        (temp_path / ".gitignore").write_text("*.log\n")
        (temp_path / ".git" / "config").write_text("# Git config\n")

        # Mock the gitignore parser to return a simple matcher that matches *.log
        def mock_parse_gitignore(_gitignore_file):
            # Read the patterns from the file
            patterns = []
            gitignore_path = Path(_gitignore_file)
            with gitignore_path.open(encoding="utf-8") as f:
                for line_raw in f:
                    line = line_raw.strip()
                    if line and not line.startswith("#"):
                        patterns.append(line)

            # Return a matcher function that uses fnmatch to match patterns
            def matcher(path_str) -> bool:
                # Convert backslashes to forward slashes
                path_str = path_str.replace("\\", "/")
                # Extract filename
                path_obj = Path(path_str)
                filename = path_obj.name

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
            (temp_path / "test.log").write_text("Test log file\n")

            # With respect_gitignore=True (default), the log file should be excluded
            file_tree, _ = generate_file_tree(tempdir)
            assert not any("test.log" in item for item in file_tree)

            # With respect_gitignore=False, the log file should be included
            file_tree, _ = generate_file_tree(tempdir, respect_gitignore=False)
            assert any("test.log" in item for item in file_tree)


def test_always_exclude_git() -> None:
    """Test that .git is always excluded regardless of settings."""
    with tempfile.TemporaryDirectory() as tempdir:
        temp_path = Path(tempdir)
        (temp_path / ".git").mkdir(parents=True)
        (temp_path / ".git" / "config").write_text("# Git config\n")

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda _: False  # No ignores from gitignore

        with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
            # Try to include .git explicitly
            file_tree, _ = generate_file_tree(tempdir, include_patterns=[".git", ".git/**"])

            # Verify .git is still excluded
            for item in file_tree:
                assert ".git/" not in item
                assert ".git\\" not in item


def test_generate_prompt_original() -> None:
    """Test the generate_prompt function."""
    with tempfile.TemporaryDirectory() as tempdir:
        temp_path = Path(tempdir)
        # Create a simple test file
        (temp_path / "test.py").write_text("print('Hello World')\n")

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda _: False  # No ignores from gitignore

        with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
            # Test with output to stdout
            prompt = generate_prompt(tempdir)

            # Check prompt content
            assert "# Repository:" in prompt
            assert "## File Tree Structure" in prompt
            assert "## File Contents" in prompt
            assert "### test.py" in prompt

            # Test with output to file
            output_file = temp_path / "output.md"
            generate_prompt(tempdir, output_file=output_file)

            # Verify file was created
            assert output_file.exists()

            # Read the content and verify
            content = output_file.read_text()
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


def test_get_gitignore_matcher() -> None:
    """Test the get_gitignore_matcher function."""
    # Create temporary file with gitignore content
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as f:
        f.write("*.txt\n")
        f.write("test/\n")
        temp_file = Path(f.name)

    # Mock the gitignore parser function
    def mock_parse_gitignore(_):
        def matcher(path):
            return path.endswith(".txt") or path.startswith("test/")
        return matcher

    with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
        root_path = Path("/fake/root")
        matcher = get_gitignore_matcher(temp_file, root_path)

        # Test with relative paths
        assert matcher("file.txt") is True
        assert matcher("file.py") is False
        assert matcher("test/file.py") is True

        # Test with absolute paths
        fake_root = Path("/fake/root")
        assert matcher(str(fake_root / "file.txt")) is True
        assert matcher(str(fake_root / "file.py")) is False
        assert matcher(str(fake_root / "test/file.py")) is True

        # Test with path outside root (should not match)
        assert matcher("/other/path/file.txt") is False

    # Clean up
    temp_file.unlink()


def test_get_gitignore_matcher_nonexistent() -> None:
    """Test get_gitignore_matcher with a nonexistent file."""
    matcher = get_gitignore_matcher(Path("/does/not/exist"), Path("/fake/root"))
    assert matcher("file.txt") is False
    assert matcher("file.py") is False


def mock_parse_gitignore(_gitignore_file):
    """Mock for parse_gitignore."""
    def matcher(path):
        return "excluded" in path
    return matcher


def test_generate_file_tree() -> None:
    """Test generate_file_tree function with simplified mock."""
    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create a file to be included
        included_file = temp_path / "included.txt"
        included_file.write_text("included content")

        # Create a file to be excluded
        excluded_file = temp_path / "excluded.txt"
        excluded_file.write_text("excluded content")

        # Patch the gitignore parser
        with mock.patch('codebase_prompt_gen.core.parse_gitignore', mock_parse_gitignore):
            # Test with exclude patterns
            file_tree, files_content = generate_file_tree(
                temp_dir, exclude_patterns=["excluded.txt"]
            )

            # Check file tree
            assert "📄 included.txt" in file_tree
            assert "📄 excluded.txt" not in file_tree

            # Check files content
            paths = [file_info["path"] for file_info in files_content]
            assert "included.txt" in paths
            assert "excluded.txt" not in paths

            # Test with include patterns
            file_tree, files_content = generate_file_tree(
                temp_dir, include_patterns=["included*"]
            )

            # Check file tree
            assert "📄 included.txt" in file_tree
            assert "📄 excluded.txt" not in file_tree


def test_generate_prompt() -> None:
    """Test generate_prompt function with simplified test case."""
    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create a file
        test_file = temp_path / "test.txt"
        test_file.write_text("test content")

        # Create an output file path
        output_file = temp_path / "output.md"

        # Patch the gitignore parser
        with mock.patch('codebase_prompt_gen.core.parse_gitignore', mock_parse_gitignore):
            # Generate prompt
            prompt = generate_prompt(
                temp_dir, output_file=output_file
            )

            # Check prompt content
            assert "# Repository:" in prompt
            assert "## File Tree Structure" in prompt
            assert "📄 test.txt" in prompt
            assert "## File Contents" in prompt
            assert "### test.txt" in prompt
            assert "test content" in prompt

            # Check output file exists and has the same content
            assert output_file.exists()
            assert output_file.read_text() == prompt
