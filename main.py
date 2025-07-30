from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    allowed_roles = [
        "flame", "aqua", "rose", "Amethyst", "lemon", "sky",
        "lilac", "ice", "blush", "navy", "red", "snow"
    ]

    msg = message.content.lower()

    if msg in [r.lower() for r in allowed_roles]:
        role = discord.utils.get(message.guild.roles, name=msg)
        if role:
            await message.author.add_roles(role)
            await message.delete()
        else:
            print(f"Role '{msg}' not found.")

    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if "وينكم" in content:
        await message.channel.send("<:sad:1399948407233188102>")

    await bot.process_commands(message)

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
