"""Tests for greeting generators."""

import pytest
from hello_possum.greetings import (
    get_random_greeting,
    get_all_greetings,
    GREETINGS,
    COMMUNAL_MESSAGES,
)


class TestGetRandomGreeting:
    """Test suite for get_random_greeting."""
    
    def test_returns_string(self):
        """Should return a string."""
        result = get_random_greeting()
        assert isinstance(result, str)
    
    def test_returns_from_greetings_list(self):
        """Should return a greeting from the known list."""
        result = get_random_greeting()
        # Check it's in the main greetings (communal adds extra line)
        first_line = result.split('\n')[0]
        assert first_line in GREETINGS
    
    def test_communal_adds_message(self):
        """Communal mode should add a collective message."""
        result = get_random_greeting(communal=True)
        lines = result.split('\n')
        assert len(lines) >= 2
        # Second line should be a communal message
        assert any(msg in lines[1] for msg in COMMUNAL_MESSAGES)


class TestGetAllGreetings:
    """Test suite for get_all_greetings."""
    
    def test_returns_list(self):
        """Should return a list."""
        result = get_all_greetings()
        assert isinstance(result, list)
    
    def test_returns_copy(self):
        """Should return a copy, not the original."""
        result = get_all_greetings()
        result.append("Test modification")
        assert len(get_all_greetings()) == len(GREETINGS)
    
    def test_contains_all_greetings(self):
        """Should contain all defined greetings."""
        result = get_all_greetings()
        assert set(result) == set(GREETINGS)
