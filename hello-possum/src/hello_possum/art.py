"""ASCII art possums for the 8-bit aesthetic."""

from typing import List

# Classic standing possum
STANDING_POSSUM = r"""
        🦝
       (o.o)
       (___)
      /|   |\\
       |   |
""".strip()

# Possum with headphones (debug mode)
DEBUG_POSSUM = r"""
       _____
      /     \\___
     |  o o  |__)
     |   <   |
   __|  ___  |__
  /  |_______|  \\
 /   |#######|   \\
     |#######|
     |_______|
""".strip()

# Communal possum (collective vibe)
COMMUNAL_POSSUM = r"""
      🦝    🦝    🦝
     (o.o) (o.o) (o.o)
     (___) (___) (___)
    /|||| |||| ||||\\
    Shared Territory
""".strip()

ART_VARIANTS: List[str] = [STANDING_POSSUM, DEBUG_POSSUM, COMMUNAL_POSSUM]


def get_possum(variant: str = "random") -> str:
    """Return ASCII possum art.
    
    Args:
        variant: "standing", "debug", "communal", or "random"
        
    Returns:
        ASCII art string.
    """
    if variant == "standing":
        return STANDING_POSSUM
    elif variant == "debug":
        return DEBUG_POSSUM
    elif variant == "communal":
        return COMMUNAL_POSSUM
    else:
        import random
        return random.choice(ART_VARIANTS)
