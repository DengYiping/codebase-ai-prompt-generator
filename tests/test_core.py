"""Tests for core functionality."""

import fnmatch
import io
import tempfile
from pathlib import Path
from unittest import mock

from codebase_prompt_gen.core import generate_file_tree, generate_prompt, get_gitignore_matcher


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
            file_tree, files_content = generate_file_tree(
                Path(tempdir), exclude_patterns=[], include_patterns=[]
            )

            # Check file tree structure
            assert any("src/" in item for item in file_tree)
            assert any("tests/" in item for item in file_tree)
            assert any("README.md" in item for item in file_tree)

            # Verify .git directory files are excluded
            for item in file_tree:
                assert ".git/" not in item
                assert ".git\\" not in item

            for file_path, _ in files_content:
                assert not str(file_path).startswith(".git/")
                assert not str(file_path).startswith(".git\\")

            # Check content
            assert any(str(file_path) == "README.md" for file_path, _ in files_content)
            assert any(str(file_path) == "src/main.py" for file_path, _ in files_content)

            # Test with custom exclude patterns
            file_tree, files_content = generate_file_tree(
                Path(tempdir), exclude_patterns=["*.md"], include_patterns=[]
            )
            assert not any("README.md" in item for item in file_tree)

            # Test with custom include patterns
            file_tree, files_content = generate_file_tree(
                Path(tempdir), exclude_patterns=[], include_patterns=["*.py"]
            )
            assert any("main.py" in item for item in file_tree)
            assert not any("README.md" in item for item in file_tree)

            # Test with respect_gitignore=False
            (temp_path / "test.log").write_text("Test log file\n")

            # With respect_gitignore=True (default), the log file should be excluded
            file_tree, _ = generate_file_tree(
                Path(tempdir), exclude_patterns=[], include_patterns=[]
            )
            assert not any("test.log" in item for item in file_tree)

            # With respect_gitignore=False, the log file should be included
            file_tree, _ = generate_file_tree(
                Path(tempdir), respect_gitignore=False, exclude_patterns=[], include_patterns=[]
            )
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
            file_tree, _ = generate_file_tree(
                Path(tempdir), exclude_patterns=[], include_patterns=[".git", ".git/**"]
            )

            # Verify .git is still excluded
            for item in file_tree:
                assert ".git/" not in item
                assert ".git\\" not in item


def test_generate_prompt_original() -> None:
    """Test the generate_prompt function."""
    # Create a simple mock repo with 2 files - one to include and one to exclude
    with tempfile.TemporaryDirectory() as tempdir:
        temp_path = Path(tempdir)
        # Create a file to include
        included_file = temp_path / "included.py"
        included_file.write_text("# Python file for testing\nprint('Hello World')")

        # Create a file to exclude
        excluded_file = temp_path / "excluded.js"
        excluded_file.write_text("// JavaScript file for testing\nconsole.log('Hello World')")

        # Create a .gitignore file
        gitignore_file = temp_path / ".gitignore"
        gitignore_file.write_text("excluded.js\n")

        # Create a proper mock for gitignore parser
        def mock_parse_gitignore(gitignore_file_path: Path):
            with gitignore_file_path.open(encoding="utf-8") as f:
                patterns = [line.strip() for line in f if line.strip() and not line.startswith("#")]

            def matcher(path_str):
                path_str = str(path_str)
                return any(pattern in path_str for pattern in patterns)

            return matcher

        # Patch gitignore parser
        with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
            # Test stdout output
            with mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                generate_prompt(Path(tempdir), exclude_patterns=[], include_patterns=[])
                stdout_prompt = mock_stdout.getvalue()
                assert "included.py" in stdout_prompt
                assert "# Python file for testing" in stdout_prompt
                # The file tree section shouldn't include excluded.js
                file_tree_section = stdout_prompt.split("## File Tree Structure")[1].split(
                    "## File Contents"
                )[0]
                assert "excluded.js" not in file_tree_section

            # Test file output
            output_file = temp_path / "output.md"
            file_handle = output_file.open("w", encoding="utf-8")

            def file_writer(text: str) -> None:
                file_handle.write(text)

            try:
                generate_prompt(
                    Path(tempdir),
                    exclude_patterns=["*.js"],
                    include_patterns=["*.py"],
                    output_stream=file_writer,
                )
            finally:
                file_handle.close()

            prompt_content = output_file.read_text()
            file_tree_section = prompt_content.split("## File Tree Structure")[1].split(
                "## File Contents"
            )[0]
            assert "included.py" in file_tree_section
            assert "excluded.js" not in file_tree_section

            # Test with explicit exclude
            output_file2 = temp_path / "output2.md"
            file_handle2 = output_file2.open("w", encoding="utf-8")

            def file_writer2(text: str) -> None:
                file_handle2.write(text)

            try:
                generate_prompt(
                    Path(tempdir),
                    exclude_patterns=["included.py"],
                    include_patterns=[],
                    output_stream=file_writer2,
                )
            finally:
                file_handle2.close()

            prompt_content2 = output_file2.read_text()
            file_tree_section = prompt_content2.split("## File Tree Structure")[1].split(
                "## File Contents"
            )[0]
            assert "included.py" not in file_tree_section
            assert "excluded.js" not in file_tree_section  # Still respects gitignore


def test_get_gitignore_matcher() -> None:
    """Test the get_gitignore_matcher function."""
    # Create temporary file with gitignore content
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as f:
        f.write("*.txt\n")
        f.write("test/\n")
        temp_file = Path(f.name)

    try:
        # Mock the gitignore parser function
        def mock_parse_gitignore(_):
            def matcher(path):
                path_str = str(path)
                return path_str.endswith(".txt") or path_str.startswith("test/")

            return matcher

        with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
            root_path = Path("/fake/root")
            matcher = get_gitignore_matcher(temp_file, root_path)

            # Test with string paths
            assert matcher(Path("file.txt")) is True
            assert matcher(Path("file.py")) is False
            assert matcher(Path("test/file.py")) is True

            # Test with absolute paths
            fake_root = Path("/fake/root")
            assert matcher(fake_root / "file.txt") is True
            assert matcher(fake_root / "file.py") is False
            assert matcher(fake_root / "test/file.py") is True

            # Test with path outside root (should still match if it ends with .txt)
            assert matcher(Path("/other/path/file.txt")) is True
    finally:
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
        with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
            # Test with exclude patterns
            file_tree, files_content = generate_file_tree(
                Path(temp_dir), exclude_patterns=["excluded.txt"], include_patterns=[]
            )

            # Check file tree
            assert "📄 included.txt" in file_tree
            assert "📄 excluded.txt" not in file_tree

            # Check files content
            paths = [str(file_path) for file_path, _ in files_content]
            assert "included.txt" in paths
            assert "excluded.txt" not in paths

            # Test with include patterns
            file_tree, files_content = generate_file_tree(
                Path(temp_dir), exclude_patterns=[], include_patterns=["included*"]
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
        with mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
                # Create file output stream
                file_handle = output_file.open("w", encoding="utf-8")

                def file_writer(text: str) -> None:
                    file_handle.write(text)

                try:
                    # Generate prompt to file
                    generate_prompt(
                        Path(temp_dir),
                        exclude_patterns=[],
                        include_patterns=[],
                        output_stream=file_writer,
                    )
                finally:
                    file_handle.close()

                # Check output file content
                assert output_file.exists()
                content = output_file.read_text()
                assert "# Repository:" in content
                assert "test.txt" in content

                # Generate prompt to stdout
                generate_prompt(Path(temp_dir), exclude_patterns=[], include_patterns=[])

                # Get captured output
                prompt = mock_stdout.getvalue()
                assert "# Repository:" in prompt
