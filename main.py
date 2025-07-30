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

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
