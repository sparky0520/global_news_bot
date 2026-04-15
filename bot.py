import datetime
import asyncio
import os
import discord
from discord.ext import commands, tasks
from functions import summarise_news
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
USER_ID = os.getenv("DISCORD_USER_ID")
# TARGET_TIME = "07:30"  # Target time for sending the DM (24-hour format)
TARGET_TIME = os.getenv("TARGET_TIME", "07:30")  # Default to 07:30 if not set

# Set up intents (permissions)
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")  # type: ignore
    if not scheduled_dm.is_running():
        scheduled_dm.start()


@tasks.loop(seconds=60)
async def scheduled_dm():
    now = datetime.datetime.now().strftime("%H:%M")

    if now == TARGET_TIME:
        try:
            if not USER_ID:
                print("DISCORD_USER_ID is not set; skipping scheduled DM.")
                return

            user = await bot.fetch_user(int(USER_ID))
            await send_news(user)
        except Exception as e:
            print(f"Error: {e}")


@scheduled_dm.before_loop
async def before_dm():
    await bot.wait_until_ready()


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


async def send_news(ctx):
    summary = await asyncio.to_thread(summarise_news)
    print("Summary generated, sending to Discord...", summary)
    for i in range(0, len(summary), 1500):
        await ctx.send(summary[i : i + 1500])


@bot.command()
async def news(ctx):
    await send_news(ctx)
