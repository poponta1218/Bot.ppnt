from config import DISCORD_BOT_TOKEN
from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix="p:")


@bot.event
async def on_ready():
    print('Running Bot.ppnt')
    # 起動したら「何もしないをプレイ中」と表示する．type=playing, listening, watching, streaming
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
                or "ぽぽんた" in message.content or ":poponta:" in message.content or ":poponting:" in message.content):
            await message.add_reaction("🤔")
        if bot.user in message.mentions:
            await message.channel.send("何もできません...弱くて申し訳ない :crying_cat_face: ")
        if message.author.id == 649911196694216707:  # りゅう
            rand = random.randint(1, 100)
            if rand >= 70:
                await message.channel.send("だまれ")
                await message.add_reaction("😡")
            elif rand >= 30:
                return
            elif rand == 1:
                await message.add_reaction("🥰")
            else:
                return


@bot.command(name="s")
async def poposweeper(ctx, *args):
    if args[0] in ["-h", "-help", "--help"]:
        reply = "USAGE: If you play poposweeper, type 'p:s <size [0-9]> <mine [0-size^2]>'."
        await ctx.send(reply)
    elif not (
            set(args[0]) <= set("1234567890１２３４５６７８９０")
            and set(args[1]) <= set("1234567890１２３４５６７８９０")):
        reply = "ERROR: Specified argument was out of the range of valid values."
        await ctx.send(reply)
    else:
        n = int(args[0])
        p = int(args[1])
        if n**2 < p or not 0 < n < 10 or 81 < p:
            reply = "ERROR:Specified argument was out of the range of valid values."
            await ctx.send(reply)
        else:
            num = {
                0: ":zero:",
                1: ":one:",
                2: ":two:",
                3: ":three:",
                4: ":four:",
                5: ":five:",
                6: ":six:",
                7: ":seven:",
                8: ":eight:"}
            popo = random.sample(range(n**2), p)

            def g(t, u):
                if (t + 1) * (u + 1) * (t - n) * (u - n) == 0:
                    return 0
                elif t + n * u in popo:
                    return 1
                else:
                    return 0

            def f(s):
                x = s % n
                y = s // n
                a_list = [
                    g(x - 1, y - 1),
                    g(x, y - 1),
                    g(x + 1, y - 1),
                    g(x - 1, y),
                    g(x + 1, y),
                    g(x - 1, y + 1),
                    g(x, y + 1),
                    g(x + 1, y + 1)]
                return sum(a_list)
            board = ""
            for i in range(n**2):
                if i in popo:
                    board += "||\N{Thinking Face}||"
                else:
                    board += "||" + str(num[f(i)]) + "||"
                if i % n == n - 1:
                    board += "\n"
            await ctx.send("\N{Thinking Face} = " + str(p) + "\n" + board)


bot.run(DISCORD_BOT_TOKEN)
