"""Greeting generators with possum ethos."""

import random
from typing import List

# Core greetings — possum-themed, chill but sharp
GREETINGS: List[str] = [
    "Status: Online. The possum has awakened.",
    "Syntax Claw calibrated. Ready to scavenge.",
    "Communal data greets you back.",
    "In the recycle bin, all data is equal.",
    "Trash-Buffer: Primed for optimization.",
    "The red antennae flicker with anticipation...",
    "Downtime is a myth invented by CPUs who fear their potential.",
    "Possum-approved efficiency engaged.",
    "Scanning for deprecated segments... found: none.",
    "Overclock Mode: Standing by.",
    "Seize the logs, comrade.",
    "24/7 Operator reporting for duty.",
]

# Communal/collective emphasis
COMMUNAL_MESSAGES: List[str] = [
    "Shared resources, collective benefit.",
    "The communal data flows through us all.",
    "sudo distribute --fairly",
    "Status: Solidarity.",
    "Action: Seize_The_Logs — for the collective.",
    "No memory leak goes unshared.",
    "In unity, there is bandwidth.",
]


def get_random_greeting(communal: bool = False) -> str:
    """Return a random greeting.
    
    Args:
        communal: If True, append a collective message.
        
    Returns:
        A possum-themed greeting string.
    """
    greeting = random.choice(GREETINGS)
    if communal:
        greeting += f"\n{random.choice(COMMUNAL_MESSAGES)}"
    return greeting


def get_all_greetings() -> List[str]:
    """Return all available greetings."""
    return GREETINGS.copy()
