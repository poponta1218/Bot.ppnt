from settings import DISCORD_BOT_TOKEN
from discord.ext import commands
import discord
import random
import traceback
import urllib.parse
import re

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
    await reaction(message)
    await encode_url(message)
    await bot.process_commands(message)


@bot.event
async def reaction(message):
    if message.author.bot:
        return
    else:
        if (random.randint(1, 100) >= 85
                or re.search(r"ぽぽんた|:poponta:|:poponting:|:thinking:|🤔", message.content)):
            await message.add_reaction("🤔")
        if bot.user in message.mentions:
            await message.channel.send("何もできません...弱くて申し訳ない :crying_cat_face:")
        if re.search(r":rage:|😡|笑|卍", message.content):
            await message.add_reaction("😡")
            await message.channel.send(":rage:")
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


@bot.event
async def encode_url(message):
    if message.author.bot:
        return
    else:
        pattern = r"https?://\S+\.\S+"
        url_list = re.findall(pattern, message.content)
        send_list = ""
        for url in url_list:
            url = re.sub(r'>?(`|```)?$', '', url)
            domain = urllib.parse.urlparse(url).netloc
            domain_idna = str(domain.encode("idna"), "utf-8")
            query = urllib.parse.urlparse(url).query.replace("＋", "%2B")
            replaced_url = url.replace(domain, domain_idna).replace("＋", "%2B").replace("?" + query, "")
            q_dic = urllib.parse.parse_qs(query)
            for key in q_dic:
                q_dic[key] = q_dic[key][0]
            encoded_query = urllib.parse.urlencode(q_dic)
            encoded_url = urllib.parse.quote(replaced_url, safe=":/%#")
            if encoded_query != "":
                encoded_url += "?" + encoded_query
            if url != encoded_url:
                send_list += "<" + encoded_url + ">"
                if url != url_list[-1]:
                    send_list += "\n"
        if send_list != "":
            await message.reply(send_list[:2000], allowed_mentions=discord.AllowedMentions(replied_user=False))


bot.run(DISCORD_BOT_TOKEN)
