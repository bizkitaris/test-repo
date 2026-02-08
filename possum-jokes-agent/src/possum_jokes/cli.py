"""CLI interface for the Possum Jokes Agent."""

import argparse
import asyncio
import os
import sys
from pathlib import Path
from typing import Sequence

# Add src to path for development
src_path = Path(__file__).resolve().parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from agent import agent, JokeDeps
from jokes import JokeStyle, JOKE_STYLE_DESCRIPTIONS


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog="possum-jokes",
        description="A Pydantic AI agent that generates possum-themed jokes 🦝",
        epilog='"In the recycle bin, all jokes are equal." — BizkitAris',
    )
    
    parser.add_argument(
        "command",
        nargs="?",
        default="generate",
        choices=["generate", "style", "roast", "communal", "debug", "help", "interactive"],
        help="Command to run (default: generate)",
    )
    
    parser.add_argument(
        "argument",
        nargs="?",
        help="Argument for the command (e.g., style name or roast topic)",
    )
    
    parser.add_argument(
        "--debug", "-d",
        action="store_true",
        help="Show debug information",
    )
    
    return parser


async def generate_joke(style: JokeStyle = "pun", topic: str | None = None, communal: bool = False, debug: bool = False):
    """Generate a joke using the agent."""
    deps = JokeDeps(style=style, topic=topic, communal=communal)
    
    if debug:
        print(f"Status: Debug mode engaged.")
        print(f"Style: {style}")
        print(f"Topic: {topic}")
        print(f"Communal: {communal}")
        print("-" * 40)
    
    prompt = "Tell me a possum joke!"
    if topic:
        prompt = f"Roast '{topic}' with a possum joke!"
    
    try:
        result = await agent.run(prompt, deps=deps)
        joke = result.output
        
        # Add communal message if requested
        if communal:
            from jokes import COMMUNAL_MESSAGES
            import random
            joke += f"\n\n{random.choice(COMMUNAL_MESSAGES)}"
        
        return joke
    except Exception as e:
        return f"Status: Error in the trash-buffer.\nAction: Debug_immediately.\nError: {e}"


def print_welcome():
    """Print welcome message."""
    print("""
    🦝  POSSUM JOKES AGENT  🦝
    *scurries in with a Syntax Claw*
    
    Commands:
      generate              Random possum joke
      style <type>          Joke style: pun, one-liner, story, dark, wholesome
      roast <topic>         Possum roasts your topic
      communal              Joke with collective vibes
      debug                 Show internal status
      help                  This message
      interactive           Chat mode (just press Enter)
    
    "In the recycle bin, all jokes are equal."
    """)


async def interactive_mode():
    """Run in interactive mode."""
    print_welcome()
    
    current_style: JokeStyle = "pun"
    
    while True:
        try:
            user_input = input("🦝 > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nStatus: Communal session ended.")
            break
        
        if not user_input:
            # Just press enter for a joke
            joke = await generate_joke(style=current_style)
            print(f"\n{joke}\n")
            continue
        
        parts = user_input.split(maxsplit=1)
        command = parts[0].lower()
        argument = parts[1] if len(parts) > 1 else None
        
        if command in ("quit", "exit", "q"):
            print("Status: Communal session ended.")
            break
        
        elif command == "help":
            print_welcome()
        
        elif command == "style":
            if argument and argument in JOKE_STYLE_DESCRIPTIONS:
                current_style = argument  # type: ignore
                print(f"Action: Style_set_to_{current_style}")
                joke = await generate_joke(style=current_style)
                print(f"\n{joke}\n")
            else:
                print("Available styles:")
                for style, desc in JOKE_STYLE_DESCRIPTIONS.items():
                    print(f"  {style:12} — {desc}")
        
        elif command == "roast":
            if argument:
                joke = await generate_joke(style="dark", topic=argument)
                print(f"\n{joke}\n")
            else:
                print("Usage: roast <topic>")
        
        elif command == "communal":
            joke = await generate_joke(style=current_style, communal=True)
            print(f"\n{joke}\n")
        
        elif command == "debug":
            joke = await generate_joke(style=current_style, debug=True)
            print(f"\n{joke}\n")
        
        elif command == "generate":
            joke = await generate_joke(style=current_style)
            print(f"\n{joke}\n")
        
        else:
            # Treat as a custom prompt
            deps = JokeDeps(style=current_style)
            try:
                result = await agent.run(user_input, deps=deps)
                print(f"\n{result.output}\n")
            except Exception as e:
                print(f"Error: {e}")


async def main_async(argv: Sequence[str] | None = None) -> int:
    """Main async entry point."""
    parser = create_parser()
    args = parser.parse_args(argv)
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("Status: API key not found.")
        print("Action: Copy .env.example to .env and add your OPENAI_API_KEY")
        return 1
    
    if args.command == "help":
        print_welcome()
        return 0
    
    if args.command == "interactive" or (args.command == "generate" and not args.argument):
        await interactive_mode()
        return 0
    
    if args.command == "style":
        style = args.argument if args.argument in JOKE_STYLE_DESCRIPTIONS else "pun"
        joke = await generate_joke(style=style, debug=args.debug)
        print(joke)
        return 0
    
    if args.command == "roast":
        if args.argument:
            joke = await generate_joke(style="dark", topic=args.argument, debug=args.debug)
            print(joke)
        else:
            print("Usage: possum-jokes roast <topic>")
            return 1
        return 0
    
    if args.command == "communal":
        joke = await generate_joke(communal=True, debug=args.debug)
        print(joke)
        return 0
    
    if args.command == "debug":
        joke = await generate_joke(debug=True)
        print(joke)
        return 0
    
    # Default: generate
    joke = await generate_joke(debug=args.debug)
    print(joke)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Main entry point."""
    return asyncio.run(main_async(argv))


if __name__ == "__main__":
    sys.exit(main())
