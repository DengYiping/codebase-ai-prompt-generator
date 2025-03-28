"""Tests for CLI functionality."""

import os
import sys
import tempfile
from pathlib import Path
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
        temp_path = Path(tempdir)
        # Create a test file
        (temp_path / "test.py").write_text('print("Hello")\n')

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda _: False  # No ignores from gitignore

        # Change to the temp directory and run the main function
        with mock.patch.object(sys, "argv", ["codebase-prompt"]):
            with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
                old_cwd = Path.cwd()
                try:
                    os.chdir(tempdir)
                    assert main() == 0
                    captured = capsys.readouterr()
                    assert "# Repository:" in captured.out
                    assert "test.py" in captured.out
                finally:
                    os.chdir(old_cwd)


def test_main_with_output_file() -> None:
    """Test main function with output to a file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = Path(temp_dir) / "test.py"
        test_file.write_text("print('test')")

        output_file = Path(temp_dir) / "output.md"

        # Mock gitignore parser to avoid actual parsing
        def mock_parse_gitignore(_gitignore_file):
            return lambda _: False

        # Test with specified output file
        with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
            with mock.patch.object(
                sys, "argv", ["codebase-prompt", str(temp_dir), "--output", str(output_file)]
            ):
                with mock.patch("codebase_prompt_gen.cli.main.generate_prompt") as mock_generate:
                    assert main() == 0
                    # Check that generate_prompt was called with correct args
                    mock_generate.assert_called_once()
                    args, kwargs = mock_generate.call_args
                    assert str(args[0]) == str(temp_dir)
                    assert args[1] == []  # exclude_patterns
                    assert args[2] == []  # include_patterns
                    assert kwargs["respect_gitignore"] is True
                    assert callable(kwargs["output_stream"])  # Check that output_stream is callable


def test_main_with_cursor() -> None:
    """Test the --cursor flag."""
    with tempfile.TemporaryDirectory() as tempdir:
        temp_path = Path(tempdir)
        # Create a test file
        (temp_path / "test.py").write_text('print("Hello")\n')

        # Create .cursor directory to ensure it works with existing directories
        cursor_dir = temp_path / ".cursor" / "rules"
        cursor_dir.mkdir(parents=True, exist_ok=True)

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda _: False  # No ignores from gitignore

        # Run with cursor flag
        with mock.patch.object(sys, "argv", ["codebase-prompt", tempdir, "--cursor"]):
            with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
                with mock.patch("codebase_prompt_gen.cli.main.generate_prompt") as mock_generate:
                    assert main() == 0

                    # Check that generate_prompt was called with correct args
                    mock_generate.assert_called_once()
                    args, kwargs = mock_generate.call_args
                    assert str(args[0]) == str(tempdir)
                    assert args[1] == []  # exclude_patterns
                    assert args[2] == []  # include_patterns
                    assert kwargs["respect_gitignore"] is True
                    assert callable(kwargs["output_stream"])  # Check that output_stream is callable


def test_main_with_cursor_override_output() -> None:
    """Test that --cursor overrides --output."""
    with tempfile.TemporaryDirectory() as tempdir:
        temp_path = Path(tempdir)
        # Create a test file
        (temp_path / "test.py").write_text('print("Hello")\n')

        output_file = temp_path / "output.md"

        # Mock the gitignore parser
        def mock_parse_gitignore(_gitignore_file):
            return lambda _: False  # No ignores from gitignore

        # Mock logging.warning to check for the warning message
        with mock.patch("logging.warning") as mock_warning:
            # Run with both cursor and output flags
            with mock.patch.object(
                sys,
                "argv",
                ["codebase-prompt", tempdir, "--cursor", "--output", str(output_file)],
            ):
                with mock.patch("codebase_prompt_gen.core.parse_gitignore", mock_parse_gitignore):
                    with mock.patch(
                        "codebase_prompt_gen.cli.main.generate_prompt"
                    ) as mock_generate:
                        assert main() == 0

                        # Check that generate_prompt was called with correct args
                        mock_generate.assert_called_once()
                        args, kwargs = mock_generate.call_args
                        assert str(args[0]) == str(tempdir)
                        assert args[1] == []  # exclude_patterns
                        assert args[2] == []  # include_patterns
                        assert kwargs["respect_gitignore"] is True
                        assert callable(
                            kwargs["output_stream"]
                        )  # Check that output_stream is callable

                        # Verify that the warning was logged
                        mock_warning.assert_called_once()
                        warning_message = mock_warning.call_args[0][0]
                        assert (
                            "cursor flag overrides" in warning_message.lower()
                            or "overrides" in warning_message.lower()
                        )


def test_main_error(capsys) -> None:
    """Test handling of errors in the main function."""
    with mock.patch("codebase_prompt_gen.cli.main.generate_prompt") as mock_generate:
        mock_generate.side_effect = Exception("Test error")

        with mock.patch.object(sys, "argv", ["codebase-prompt"]):
            assert main() == 1
            captured = capsys.readouterr()
            assert "Error: Test error" in captured.err
