# Global News Bot

Discord bot that pulls Google News text and summarizes it with an OpenRouter/OpenAI-compatible API.

## Quick Start

Requirements:
- Python 3.14+
- Discord bot token
- OpenRouter/OpenAI-compatible API key

Install and run:

```bash
uv sync
uv run main.py
```

Create a .env file:

```env
DISCORD_BOT_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openrouter_api_key
NEWS_CHANNEL_ID=your_discord_channel_id
```

## Commands

- !ping
- !news

## Notes

- Scheduled news posts go to DISCORD_USER_ID.
- TARGET_TIME in bot.py uses local machine time.
