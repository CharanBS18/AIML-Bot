import discord
from discord.ext import commands
import os

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot ready event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Welcome message in #general
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")

    if channel:
        await channel.send(f"Hi 👋 welcome to server {member.mention}")

# Test command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🤖 Bot is working")

# Run bot (Render safe)
bot.run(os.getenv("TOKEN"))