"""ASCII rendering helpers."""

from __future__ import annotations

from dataclasses import dataclass
from pyfiglet import Figlet, FigletFont


@dataclass(frozen=True)
class RenderResult:
    """ASCII render result and metadata."""

    text: str
    font: str
    output: str


def list_fonts(limit: int | None = None) -> list[str]:
    """Return sorted available fonts."""
    fonts = sorted(FigletFont.getFonts())
    return fonts if limit is None else fonts[:limit]


def render_text(text: str, font: str = "standard") -> RenderResult:
    """Render text as ASCII art."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("text must not be empty")
    figlet = Figlet(font=font)
    output = figlet.renderText(cleaned)
    return RenderResult(text=cleaned, font=font, output=output)
