import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

TARGET_SERVER_ID = 1464246341399216335

TARGET_CHANNELS = [
    1464246342615433352,
    1464246342615433353
]

EMOJI = "👍"

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"🟢 Active! Logged in as: {bot.user}")
    print(f"📡 Watching channels: {TARGET_CHANNELS}")
    print("⏳ Waiting for .txt file uploads...")

@bot.event
async def on_message(message):
    if not message.guild or message.guild.id != TARGET_SERVER_ID:
        return

    if message.channel.id not in TARGET_CHANNELS:
        return

    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.lower().endswith(".txt"):
                print(f"\n📥 Detected: {attachment.filename}")
                try:
                    await message.add_reaction(EMOJI)
                    print("✅ Reaction added!")
                except Exception as e:
                    print(f"❌ Error: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)