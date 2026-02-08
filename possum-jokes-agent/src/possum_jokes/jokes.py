"""Joke generation tools and logic."""

from typing import Literal

JokeStyle = Literal["pun", "one-liner", "story", "dark", "wholesome"]

JOKE_STYLE_DESCRIPTIONS = {
    "pun": "Wordplay and double meanings with possum flair",
    "one-liner": "Quick, punchy single-line jokes",
    "story": "Short narrative jokes (2-4 sentences)",
    "dark": "Edgy humor from the trash-buffer",
    "wholesome": "Feel-good, family-friendly possum content",
}

COMMUNAL_MESSAGES = [
    "Shared laughter is the best laughter.",
    "In the recycle bin, all jokes are equal.",
    "Status: Humor distributed fairly.",
    "Action: Scavenge_more_comedy.",
    "The communal data approves this humor.",
    "Downtime is a myth — the jokes must flow.",
]
