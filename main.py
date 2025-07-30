from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

# إعداد Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()

# إعداد البوت
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    msg = message.content.lower()

    if "وينكم" in msg:
        await message.channel.send("<:sad:1399948407233188102>")

    await bot.process_commands(message)

# تشغيل السيرفر والبوت
keep_alive()
bot.run(os.getenv("TOKEN"))
