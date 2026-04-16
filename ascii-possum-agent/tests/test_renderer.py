from ascii_possum.renderer import list_fonts, render_text


def test_render_text_returns_ascii_art() -> None:
    result = render_text("hello")
    assert result.text == "hello"
    assert result.font == "standard"
    assert len(result.output.strip()) > 0


def test_list_fonts_contains_standard() -> None:
    fonts = list_fonts()
    assert "standard" in fonts
