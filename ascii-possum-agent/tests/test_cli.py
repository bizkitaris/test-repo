from ascii_possum.cli import build_parser, main


def test_parser_uses_expected_program_name() -> None:
    parser = build_parser()
    assert parser.prog == "ascii-possum"


def test_list_fonts_mode_exits_cleanly() -> None:
    assert main(["--list-fonts"]) == 0
