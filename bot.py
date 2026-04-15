import os
import discord
from discord.ext import commands
from functions import summarise_news
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up intents (permissions)
intents = discord.Intents.default()
intents.message_content = True  # Add this line!

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")  # type: ignore


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def news(ctx):
    summary = summarise_news()
    print("Summary generated, sending to Discord...", summary)
    for i in range(0, len(summary), 1500):
        await ctx.send(summary[i : i + 1500])
    await ctx.send("Here are the latest news updates!")
