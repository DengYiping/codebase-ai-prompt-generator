"""Tests for CLI functionality."""

import os
import sys
import tempfile
from unittest import mock

from codebase_prompt_gen.cli.main import main


def test_main_version(capsys) -> None:
    """Test the --version flag."""
    with mock.patch.object(sys, "argv", ["codebase-prompt", "--version"]):
        assert main() == 0
        captured = capsys.readouterr()
        assert "Codebase AI Prompt Generator v" in captured.out


def test_main_default(capsys) -> None:
    """Test the default behavior with no arguments."""
    with tempfile.TemporaryDirectory() as tempdir:
        # Create a test file
        with open(os.path.join(tempdir, "test.py"), "w", encoding="utf-8") as f:
            f.write('print("Hello")\n')

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda path: False  # No ignores from gitignore

        # Change to the temp directory and run the main function
        with mock.patch.object(sys, "argv", ["codebase-prompt"]):
            with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
                old_cwd = os.getcwd()
                try:
                    os.chdir(tempdir)
                    assert main() == 0
                    captured = capsys.readouterr()
                    assert "# Repository:" in captured.out
                    assert "test.py" in captured.out
                finally:
                    os.chdir(old_cwd)


def test_main_with_output_file() -> None:
    """Test writing output to a file."""
    with tempfile.TemporaryDirectory() as tempdir:
        # Create a test file
        with open(os.path.join(tempdir, "test.py"), "w", encoding="utf-8") as f:
            f.write('print("Hello")\n')

        output_file = os.path.join(tempdir, "output.md")

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda path: False  # No ignores from gitignore

        # Run with output file
        with mock.patch.object(sys, "argv", ["codebase-prompt", tempdir, "--output", output_file]):
            with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
                assert main() == 0

                # Check that the file was created
                assert os.path.exists(output_file)

                # Check content
                with open(output_file, encoding="utf-8") as f:
                    content = f.read()
                    assert "# Repository:" in content
                    assert "test.py" in content


def test_main_with_cursor() -> None:
    """Test the --cursor flag."""
    with tempfile.TemporaryDirectory() as tempdir:
        # Create a test file
        with open(os.path.join(tempdir, "test.py"), "w", encoding="utf-8") as f:
            f.write('print("Hello")\n')

        # Create .cursor directory to ensure it works with existing directories
        cursor_dir = os.path.join(tempdir, ".cursor", "rules")
        os.makedirs(cursor_dir, exist_ok=True)

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda path: False  # No ignores from gitignore

        # Run with cursor flag
        with mock.patch.object(sys, "argv", ["codebase-prompt", tempdir, "--cursor"]):
            with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
                assert main() == 0

                # Check that the file was created
                cursor_file = os.path.join(cursor_dir, "entire-codebase.mdc")
                assert os.path.exists(cursor_file)

                # Check content
                with open(cursor_file, encoding="utf-8") as f:
                    content = f.read()
                    assert "# Repository:" in content
                    assert "test.py" in content


def test_main_with_cursor_override_output(capsys) -> None:
    """Test that --cursor overrides --output."""
    with tempfile.TemporaryDirectory() as tempdir:
        # Create a test file
        with open(os.path.join(tempdir, "test.py"), "w", encoding="utf-8") as f:
            f.write('print("Hello")\n')

        output_file = os.path.join(tempdir, "output.md")

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda path: False  # No ignores from gitignore

        # Run with both cursor and output flags
        with mock.patch.object(
            sys,
            "argv",
            ["codebase-prompt", tempdir, "--cursor", "--output", output_file],
        ):
            with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
                assert main() == 0
                captured = capsys.readouterr()
                assert "Warning: --cursor flag overrides --output flag" in captured.err

                # Check that the cursor file was created
                cursor_file = os.path.join(tempdir, ".cursor", "rules", "entire-codebase.mdc")
                assert os.path.exists(cursor_file)


def test_main_error(capsys) -> None:
    """Test handling of errors in the main function."""
    with mock.patch("codebase_prompt_gen.cli.main.generate_prompt") as mock_generate:
        mock_generate.side_effect = Exception("Test error")

        with mock.patch.object(sys, "argv", ["codebase-prompt"]):
            assert main() == 1
            captured = capsys.readouterr()
            assert "Error: Test error" in captured.err
