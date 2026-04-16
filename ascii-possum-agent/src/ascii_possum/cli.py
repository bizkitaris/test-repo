"""CLI entry point for ASCII Possum Agent."""

from __future__ import annotations

import argparse
from typing import Sequence

from ascii_possum import __version__
from ascii_possum.renderer import list_fonts, render_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ascii-possum",
        description="Render a word, phrase, or sentence as ASCII art.",
    )
    parser.add_argument("text", nargs="*", help="Text to render")
    parser.add_argument("--font", default="standard", help="Pyfiglet font name")
    parser.add_argument("--list-fonts", action="store_true", help="List available fonts")
    parser.add_argument("--debug", action="store_true", help="Show render metadata")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list_fonts:
        for font in list_fonts():
            print(font)
        return 0

    text = " ".join(args.text).strip()
    if not text:
        parser.error("text is required unless --list-fonts is used")

    result = render_text(text=text, font=args.font)
    print(result.output, end="")

    if args.debug:
        print(f"Status: rendered '{result.text}' with font '{result.font}'")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
