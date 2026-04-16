# ASCII Possum Agent — PRP (Product Requirement Prompt)

## Goal
Build a lightweight CLI tool that converts a word, multiple words, or a sentence into ASCII art.

## Why
- Extend the `test-repo` experimental toolbox with a practical text transformation utility
- Practice clean Python packaging and CLI structure
- Keep a deterministic, dependency-light project in the repo alongside the more playful/agentic examples

## What (User-Visible Behavior)
- CLI command: `ascii-possum` or `ap`
- Accept plain text input from positional arguments
- Render text as ASCII art using a selected font
- Optional flags:
  - `--font` → choose font
  - `--list-fonts` → show available fonts
  - `--debug` → render metadata

## Context

### Tech Stack
- Python 3.9+
- `pyfiglet`
- `argparse`
- `pytest`

### Project Structure
```text
ascii-possum-agent/
├── src/
│   └── ascii_possum/
│       ├── __init__.py
│       ├── cli.py
│       └── renderer.py
├── tests/
│   ├── test_cli.py
│   └── test_renderer.py
├── pyproject.toml
├── README.md
└── PRP.md
```

## Validation Loop

```bash
pip install -e .
pytest -v
ascii-possum hello
ascii-possum --font slant "hello possum"
ascii-possum --list-fonts
```

## Acceptance Criteria
- [ ] CLI runs without errors
- [ ] Accepts words and full sentences
- [ ] Supports font selection
- [ ] Lists fonts
- [ ] Tests pass
