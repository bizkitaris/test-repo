"""CLI entry point for hello-possum."""

import argparse
import sys
from typing import Optional, Sequence

from hello_possum import __version__
from hello_possum.greetings import get_random_greeting, get_all_greetings
from hello_possum.art import get_possum


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog="hello-possum",
        description="A communal CLI greeting tool with possum vibes 🦝",
        epilog='"In the recycle bin, all data is equal." — BizkitAris',
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--art", "-a",
        action="store_true",
        help="Show ASCII possum art",
    )
    parser.add_argument(
        "--all", "-A",
        action="store_true",
        dest="show_all",
        help="List all possible greetings",
    )
    parser.add_argument(
        "--communal", "-c",
        action="store_true",
        help="Emphasize collective/data-sharing ethos",
    )
    parser.add_argument(
        "--debug", "-d",
        action="store_true",
        help="Show debug info (internal status)",
    )
    
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main entry point.
    
    Args:
        argv: Command line arguments (defaults to sys.argv[1:]).
        
    Returns:
        Exit code (0 for success).
    """
    parser = create_parser()
    args = parser.parse_args(argv)
    
    if args.debug:
        print("Status: Debug mode engaged.")
        print(f"Version: {__version__}")
        print(f"Args: {vars(args)}")
        print()
        print(get_possum("debug"))
        print()
    
    if args.show_all:
        print("All communal greetings:")
        print("-" * 40)
        for i, greeting in enumerate(get_all_greetings(), 1):
            print(f"{i:2}. {greeting}")
        return 0
    
    if args.art:
        art_variant = "communal" if args.communal else "random"
        print(get_possum(art_variant))
        print()
    
    print(get_random_greeting(communal=args.communal))
    return 0


if __name__ == "__main__":
    sys.exit(main())
