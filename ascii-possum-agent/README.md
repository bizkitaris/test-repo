# ASCII Possum Agent 🦝

*A small CLI utility that turns words, phrases, or full sentences into ASCII art.*

## Installation

```bash
cd ascii-possum-agent
pip install -e .
```

## Usage

```bash
ascii-possum hello
ascii-possum "hello possum"
ascii-possum --font slant "communal data"
ascii-possum --list-fonts
ascii-possum --debug "syntax claw"
```

## Features

- Render a single word, multiple words, or a full sentence as ASCII art
- Choose a pyfiglet font with `--font`
- List available fonts with `--list-fonts`
- Use `--debug` for render metadata

## Examples

```bash
$ ascii-possum hello
# ASCII art output

$ ascii-possum --font slant "hello possum"
# ASCII art output
```

## Notes

- Built to match the lightweight experimental pattern used in this repo
- Deterministic output, no model/API dependency required
- Good candidate for a future "creative mode" if we want an LLM-powered variant later
