from config import DISCORD_BOT_TOKEN
from discord.ext import commands
import discord
import random
import traceback

bot = commands.Bot(command_prefix="p:")

PCOMMANDS = [
    "commands.phelp",
    "commands.psweeper",
    "commands.pfuck"
]

for cog in PCOMMANDS:
    try:
        bot.load_extension(cog)
    except Exception:
        traceback.print_exc()


@bot.event
async def on_ready():
    print("---------------------")
    print("Logged in as " + bot.user.name)
    print("Running " + bot.user.name)
    print("---------------------")
    # type=playing, listening, watching, streaming
    activity = discord.Activity(
        name="何もしない",
        type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)


@bot.event
async def on_message(message):
    await reply(message)
    await bot.process_commands(message)


@bot.event
async def reply(message):
    if message.author == bot.user:
        return
    else:
        if (random.randint(1, 100) >= 85
                or "ぽぽんた" in message.content or ":poponta:" in message.content
                or ":poponting:" in message.content or ":thinking:" in message.content):
            await message.add_reaction("🤔")
        if bot.user in message.mentions:
            await message.channel.send("何もできません...弱くて申し訳ない :crying_cat_face:")
        if message.author.id == 649911196694216707:  # りゅう
            rand = random.randint(1, 100)
            if rand >= 70:
                await message.channel.send("だまれ")
            elif rand >= 40:
                await message.add_reaction("😡")
            elif rand <= random.randint(2, 4):
                await message.add_reaction("🥰")
            else:
                return


bot.run(DISCORD_BOT_TOKEN)
