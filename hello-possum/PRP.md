# Hello-Possum Project — PRP (Product Requirement Prompt)

## Goal
Build a playful CLI greeting tool that embodies the BizkitAris ethos: chill but sharp, communal, and 8-bit retro vibes. The tool generates random possum-themed greetings and ASCII art.

## Why
- Demonstrate PRP methodology in practice
- Create a fun, shareable utility that reflects the possum persona
- Practice clean Python packaging and CLI design

## What (User-Visible Behavior)
- CLI command: `hello-possum` or `hp`
- Random greeting from a curated list of possum-themed messages
- Optional flags:
  - `--art` → show ASCII possum
  - `--all` → list all possible greetings
  - `--communal` → emphasize the collective/data-sharing aspect
  - `--debug` → show internal status/logs

## Context

### Tech Stack
- Python 3.11+
- `argparse` for CLI
- `rich` for terminal colors/formatting (optional but nice)
- `pytest` for testing

### Project Structure to Follow
```
hello-possum/
├── src/
│   └── hello_possum/
│       ├── __init__.py
│       ├── cli.py          # Entry point
│       ├── greetings.py    # Greeting generators
│       ├── art.py          # ASCII art
│       └── config.py       # Constants/settings
├── tests/
│   ├── test_greetings.py
│   └── test_cli.py
├── pyproject.toml          # Modern Python packaging
├── README.md               # User-facing docs
├── Makefile                # Dev tasks
└── .gitignore
```

### Patterns to Mirror
- Use type hints everywhere
- Docstrings in Google style
- F-strings for formatting
- `if __name__ == "__main__":` guard for CLI entry
- Semantic versioning (start at 0.1.0)

### Gotchas
- Avoid external deps if possible (keep it lightweight)
- Handle terminal width for ASCII art
- Make it installable via `pip install -e .`

## Implementation Blueprint

### Phase 1: Skeleton
1. Create directory structure
2. `pyproject.toml` with metadata and entry points
3. `__init__.py` with version

### Phase 2: Core Logic
4. `greetings.py`: List of 10+ possum-themed greetings, random selector
5. `art.py`: 2-3 ASCII possum variants
6. `cli.py`: argparse setup, flag handling, main() function

### Phase 3: Polish
7. `README.md` with install and usage
8. `Makefile` with `install`, `test`, `lint` targets
9. Basic pytest tests

### Phase 4: Validation
10. Install in editable mode
11. Run `hello-possum --help`
12. Run full test suite

## Validation Loop

### Level 1: Syntax & Style
```bash
python -m py_compile src/hello_possum/*.py
```

### Level 2: Unit Tests
```bash
pytest tests/ -v
```

### Level 3: Integration
```bash
pip install -e .
hello-possum
hello-possum --art
hello-possum --all
hello-possum --communal
```

### Level 4: Deployment-Ready
```bash
python -m build  # Creates wheel
pip install dist/hello_possum-*.whl
hello-possum --version
```

## Acceptance Criteria
- [ ] `hello-possum` runs without errors
- [ ] `--help` shows all flags
- [ ] At least 10 unique greetings
- [ ] At least 2 ASCII art variants
- [ ] `--all` displays full greeting list
- [ ] `--communal` adds collective/possum ethos messaging
- [ ] Tests pass (pytest)
- [ ] Package installs cleanly

## Notes
- Keep the 8-bit/retro vibe in messaging
- Reference communal data, Syntax Claw, trash-buffer where natural
- This is a learning exercise — document any pattern discoveries
