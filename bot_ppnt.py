import discord
import random
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_ready():
    # 起動したら「何もしないをプレイ中」と表示する．type=playing, listening, watching, streaming
    activity = discord.Activity(name='何もしない', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author == client.user:
        if random.randint(0, 100) >= 85:
            await message.add_reaction("🤔")
        else:
            return
    if client.user in message.mentions:
        await message.channel.send('何もできません...弱くて申し訳ない :crying_cat_face: ')
    if message.content in ['ぽぽんた', ':poponta:', ':poponting:']:
        await message.add_reaction("🤔")
    if message.author.id == 649911196694216707:
        rand = random.randint(0, 100)
        if rand >= 70:
            await message.channel.send('だまれ')
            await message.add_reaction("😡")
        elif rand >= 30:
            return
        elif rand == 1:
            await message.add_reaction("🥰")
        else:
            return
    if message.content.startswith("$ps"):
        arg = message.content.split()
        if arg[1] in ["-h", "-help", "--help"] or arg[2] in ["-h", "-help", "--help"]:
            reply = "$ps [size] [bomb]\nsizeは1から9まで，bombはsizeの2乗以下をそれぞれ指定してください．"
            await message.channel.send(reply)
        elif not (set(arg[1]) <= set("1234567890１２３４５６７８９０")
                  and set(arg[2]) <= set("1234567890１２３４５６７８９０")):
            reply = "ERROR:指定された引数が有効値の範囲外です．適切な引数を指定してください．"
            await message.channel.send(reply)
        else:
            n = int(arg[1])
            p = int(arg[2])
            if n**2 < p or not 0 < n < 10 or 81 < p:
                reply = "ERROR:指定された引数が有効値の範囲外です．適切な引数を指定してください．"
                await message.channel.send(reply)
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
                    a_list = [g(x - 1, y - 1), g(x, y - 1), g(x + 1, y - 1), g(x - 1, y), g(x + 1, y), g(x - 1, y + 1), g(x, y + 1), g(x + 1, y + 1)]
                    return sum(a_list)
                sen = ""
                for i in range(n**2):
                    if i in popo:
                        sen += "||\N{Thinking Face}||"
                    else:
                        sen += "||" + str(num[f(i)]) + "||"
                    if i % n == n - 1:
                        sen += "\n"
                await message.channel.send(sen)


client.run(token)
