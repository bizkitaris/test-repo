"""Pydantic AI agent for possum joke generation."""

from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai import Agent, RunContext
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path
import os
import random

from prompt import POSSEUM_JOKES_SYSTEM_PROMPT
from jokes import JokeStyle, COMMUNAL_MESSAGES

# Load environment variables from project root (where .env should be)
project_root = Path(__file__).resolve().parent.parent.parent
env_path = project_root / '.env'
load_dotenv(env_path, override=True)


def get_model():
    """Get the LLM model configuration."""
    llm = os.getenv('LLM_MODEL') or 'gpt-4o-mini'
    base_url = os.getenv('LLM_BASE_URL') or 'https://api.openai.com/v1'
    api_key = os.getenv('OPENAI_API_KEY') or ''
    
    return OpenAIModel(llm, provider=OpenAIProvider(base_url=base_url, api_key=api_key))


@dataclass
class JokeDeps:
    """Dependencies for the joke agent."""
    style: JokeStyle = "pun"
    topic: str | None = None
    communal: bool = False


# Create the Pydantic AI agent
agent = Agent(
    get_model(),
    system_prompt=POSSEUM_JOKES_SYSTEM_PROMPT,
    deps_type=JokeDeps,
    retries=2,
)


@agent.system_prompt
def add_style_instructions(ctx: RunContext[JokeDeps]) -> str:
    """Add style-specific instructions based on deps."""
    style = ctx.deps.style
    instructions = f"\nGenerate a {style}-style joke."
    
    if ctx.deps.topic:
        instructions += f" The joke should roast or reference: {ctx.deps.topic}"
    
    return instructions


@agent.tool
async def get_communal_message(ctx: RunContext[JokeDeps]) -> str:
    """Get a random communal message to append to jokes.
    
    Use this when the user requests communal mode.
    """
    return random.choice(COMMUNAL_MESSAGES)
