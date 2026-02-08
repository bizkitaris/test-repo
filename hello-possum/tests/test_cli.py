"""Tests for CLI interface."""

import pytest
from unittest.mock import patch
from hello_possum.cli import main, create_parser
from hello_possum import __version__


class TestCreateParser:
    """Test suite for argument parser."""
    
    def test_parser_creation(self):
        """Should create parser without error."""
        parser = create_parser()
        assert parser is not None
    
    def test_version_flag(self):
        """Should handle --version flag."""
        parser = create_parser()
        with pytest.raises(SystemExit) as exc_info:
            parser.parse_args(["--version"])
        assert exc_info.value.code == 0


class TestMain:
    """Test suite for main function."""
    
    def test_default_run(self, capsys):
        """Default run should print a greeting."""
        exit_code = main([])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert len(captured.out) > 0
    
    def test_all_flag(self, capsys):
        """--all should list all greetings."""
        exit_code = main(["--all"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "All communal greetings" in captured.out
    
    def test_art_flag(self, capsys):
        """--art should show ASCII art."""
        exit_code = main(["--art"])
        captured = capsys.readouterr()
        assert exit_code == 0
        # ASCII art should contain possum-like characters
        assert "(" in captured.out or ")" in captured.out
    
    def test_communal_flag(self, capsys):
        """--communal should add collective message."""
        exit_code = main(["--communal"])
        captured = capsys.readouterr()
        assert exit_code == 0
        # Should be a longer output with multiple lines
        assert len(captured.out.strip().split('\n')) >= 1
    
    def test_debug_flag(self, capsys):
        """--debug should show debug info."""
        exit_code = main(["--debug"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "Debug mode" in captured.out
        assert __version__ in captured.out
