# Possum Jokes Agent — PRP (Product Requirement Prompt)

## Goal
Build a creative CLI AI agent that generates possum-themed jokes using Pydantic AI. The agent should have personality (BizkitAris vibes) and be able to generate different styles of jokes on demand.

## Why
- Demonstrate Pydantic AI patterns from Module 4 in a fun, focused project
- Create a useful/fun utility that reflects the possum persona
- Practice building a simpler agent (no RAG, no complex memory — just LLM + tools)

## What (User-Visible Behavior)
- CLI command: `possum-jokes` or `pj`
- Interactive joke generation with possum personality
- Commands:
  - `generate` or just press Enter → Random possum joke
  - `style <type>` → Choose joke style (pun, one-liner, story, dark, wholesome)
  - `roast <topic>` → Possum roasts a topic you provide
  - `communal` → Jokes with collective/ethos messaging
  - `debug` → Show what's happening under the hood
  - `help` → Show all commands

## Context

### Tech Stack
- Python 3.11+
- Pydantic AI (following Module 4 patterns)
- OpenAI or OpenRouter for LLM
- No external dependencies beyond Pydantic AI + OpenAI client

### Project Structure (mirroring Module 4 patterns)
```
possum-jokes-agent/
├── pyproject.toml          # Modern packaging
├── README.md               # User docs
├── .env.example            # API keys template
├── src/
│   └── possum_jokes/
│       ├── __init__.py
│       ├── cli.py          # CLI entry point
│       ├── agent.py        # Pydantic AI agent
│       ├── prompt.py       # System prompt with possum personality
│       └── jokes.py        # Joke generation logic/tools
└── tests/
    └── test_jokes.py
```

### Patterns to Mirror (from Module 4)
- `Agent` class with `system_prompt` decorator
- `@agent.tool` for structured tool calling
- `RunContext` for dependencies
- `get_model()` helper function for LLM configuration
- Type hints everywhere
- Pydantic-style dataclasses for deps

### Personality to Embed
- Chill but sharp delivery
- Occasional "Status:" and "Action:" prefixes
- References to communal data, Syntax Claw, trash-buffer
- 8-bit retro vibes in responses

## Implementation Blueprint

### Phase 1: Skeleton
1. Create directory structure
2. `pyproject.toml` with Pydantic AI dependency
3. `.env.example` for API key
4. `__init__.py` with version

### Phase 2: Core Agent
5. `prompt.py` — System prompt with possum personality + joke instructions
6. `agent.py` — Pydantic AI agent with `generate_joke` tool
7. `jokes.py` — Joke generation logic, style handlers

### Phase 3: CLI Interface
8. `cli.py` — Interactive CLI with commands (generate, style, roast, communal, debug, help)
9. Handle user input loop
10. Pretty output formatting

### Phase 4: Polish & Tests
11. `README.md` with setup and usage
12. Basic tests
13. Validation

## Validation Loop

### Level 1: Syntax & Imports
```bash
python3 -m py_compile src/possum_jokes/*.py
python3 -c "from possum_jokes.agent import agent; print('✓ Agent imports')"
```

### Level 2: Run Tests
```bash
pytest tests/ -v
```

### Level 3: Manual Integration
```bash
pip install -e .
possum-jokes --help
possum-jokes generate
possum-jokes style pun
possum-jokes roast "Python"
possum-jokes communal
```

### Level 4: Agent Behavior
- [ ] Agent responds with possum personality
- [ ] Jokes are actually funny (subjective, but try)
- [ ] Different styles produce different outputs
- [ ] Roast command roasts the provided topic
- [ ] Communal mode adds collective messaging

## Acceptance Criteria
- [ ] `possum-jokes` runs without errors
- [ ] Agent generates possum-themed jokes
- [ ] Personality matches BizkitAris ethos
- [ ] CLI has all commands working
- [ ] Can specify joke styles
- [ ] Can roast arbitrary topics
- [ ] Tests pass
- [ ] Package installs cleanly

## Notes
- Keep it lightweight — no RAG, no memory, just pure LLM creativity
- Use Pydantic AI's tool calling for structured joke generation
- Make the personality consistent but not overbearing
- Have fun with it — this is a creative project!
