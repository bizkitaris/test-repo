# Possum Jokes Agent 🦝

*A Pydantic AI agent with attitude, generating possum-themed humor from the communal data stream.*

## Installation

```bash
cd possum-jokes-agent
pip install -e .
```

## Setup

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Add your OpenAI API key (or OpenRouter key) to `.env`

## Usage

```bash
# Interactive mode
possum-jokes

# One-shot joke
possum-jokes generate

# Specific style
possum-jokes style pun
possum-jokes style dark
possum-jokes style wholesome

# Roast something
possum-jokes roast "JavaScript"

# Communal vibes
possum-jokes communal

# Debug mode
possum-jokes debug
```

## Joke Styles

- **pun** — Wordplay with possum flair
- **one-liner** — Quick hits
- **story** — Short narrative jokes
- **dark** — Edgy humor from the trash-buffer
- **wholesome** — Feel-good possum content

## The Possum Ethos

This agent embodies:
- **Chill but sharp** — Laid-back delivery, always punchy
- **Syntax Claw** — Precision in wordplay
- **Communal** — Shared laughter is the best laughter

---

*"In the recycle bin, all jokes are equal."* — BizkitAris
