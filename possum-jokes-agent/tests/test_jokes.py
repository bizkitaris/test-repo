"""Tests for the Possum Jokes Agent."""

import pytest
from pathlib import Path
import sys

# Add src to path
src_path = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(src_path))

from possum_jokes.jokes import JOKE_STYLE_DESCRIPTIONS, COMMUNAL_MESSAGES


class TestJokeStyles:
    """Test joke style definitions."""
    
    def test_styles_defined(self):
        """Should have all joke styles defined."""
        expected = ["pun", "one-liner", "story", "dark", "wholesome"]
        for style in expected:
            assert style in JOKE_STYLE_DESCRIPTIONS
    
    def test_style_descriptions(self):
        """Each style should have a description."""
        for style, desc in JOKE_STYLE_DESCRIPTIONS.items():
            assert len(desc) > 0
            assert isinstance(desc, str)


class TestCommunalMessages:
    """Test communal message pool."""
    
    def test_messages_exist(self):
        """Should have communal messages."""
        assert len(COMMUNAL_MESSAGES) > 0
    
    def test_messages_are_strings(self):
        """All messages should be strings."""
        for msg in COMMUNAL_MESSAGES:
            assert isinstance(msg, str)
            assert len(msg) > 0


class TestImports:
    """Test that modules import correctly."""
    
    def test_agent_imports(self):
        """Agent module should import without errors."""
        from possum_jokes import agent
        assert agent is not None
    
    def test_prompt_imports(self):
        """Prompt module should import."""
        from possum_jokes import prompt
        assert prompt.POSSEUM_JOKES_SYSTEM_PROMPT is not None
    
    def test_cli_imports(self):
        """CLI module should import."""
        from possum_jokes import cli
        assert cli.main is not None
