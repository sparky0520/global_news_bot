# Global News Bot

A simple Discord bot that fetches Google News text and uses OpenRouter (via the OpenAI SDK) to generate a concise news summary.

## Features

- `!ping`: health check command
- `!news`: fetches and summarizes current Google News content
- Sends long summaries in chunks to avoid Discord message limits

## Requirements

- Python 3.14+
- A Discord bot token
- An OpenRouter/OpenAI-compatible API key

## Setup

1. Install dependencies:

```bash
uv sync
```

2. Create a `.env` file in the repo root:

```env
DISCORD_BOT_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openrouter_api_key
```

3. Run the bot:

```bash
uv run main.py
```

## Commands

- `!ping`
- `!news`
