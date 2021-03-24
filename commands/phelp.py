from discord.ext import commands
import discord


class Pcommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="h")
    async def help(self, ctx, lang="ja"):
        if lang == "ja":
            embed = discord.Embed(
                title="Bot.ppnt",
                description="使い方",
                color=discord.Color.blue())
            embed.add_field(
                name="p:s <size> <mine>",
                value="ぽぽスイーパーを起動できます．sizeは1から9，mineはsizeの2乗以下を指定してください．"
            )
        else:
            reply = "その言語に対応していなくて申し訳ない... :crying_cat_face:"
            await ctx.send(reply)
            embed = discord.Embed(
                title="Bot.ppnt",
                description="使い方",
                color=discord.Color.blue())
            embed.add_field(
                name="p:s <size> <mine>",
                value="ぽぽスイーパーを起動できます．sizeは1から9，mineはsizeの2乗以下を指定してください．"
            )
        await ctx.send(embed=embed)


def setup(bot):
    return bot.add_cog(Pcommands(bot))
