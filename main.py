from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

# السيرفر الخلفي لتشغيل البوت باستمرار
app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()

# إعدادات البوت
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

    # وينكم → يرد بصورة
    if "وينكم" in msg:
        try:
            await message.channel.send(file=discord.File("sad.png"))
        except Exception as e:
            print(f"⚠️ Error sending sad.png: {e}")

    # @everyone → يرد بإيموجي excited
    if "@everyone" in msg:
        await message.channel.send("<:excited:1399952577499500616>")

    # منو سواج؟ → يرد بإسم و إيموجي
    if "منو سواج؟" in msg:
        await message.channel.send("رووووووووووري <:66:1399953120309809253>")

    await bot.process_commands(message)

# تشغيل السيرفر والبوت
keep_alive()
bot.run(os.getenv("TOKEN"))
