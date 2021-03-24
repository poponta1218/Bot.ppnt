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
                description="使用方法",
                color=discord.Color.from_rgb(255, 204, 77)
            )
            embed.add_field(
                name="`p:h [lang]`",
                value="""\
                今表示しているようにBotの使用方法が確認できます．
                langはISO-639に準拠して指定してください． 例:ja, en
                指定しなかった場合は日本語で表示されます．
                """,
                inline=False
            )
            embed.add_field(
                name="`p:s <size> <mine>`",
                value="""\
                ぽぽスイーパーを起動できます．
                sizeは1から9，mineはsizeの2乗以下を指定してください．
                """,
                inline=False
            )
        elif lang == "en":
            embed = discord.Embed(
                title="Bot.ppnt",
                description="Usage",
                color=discord.Color.from_rgb(255, 204, 77)
            )
            embed.add_field(
                name="`p:h [lang]`",
                value="""\
                As you see, You can check the usage of this bot.
                For lang, give a language code based on ISO 639. e.g. ja, en
                If lang is not given, displayed in Japanese.
                """,
                inline=False
            )
            embed.add_field(
                name="`p:s <size> <mine>`",
                value="""\
                You can play poposweeper.
                For size, specify a positive integer from 1 to 9, and for mine, give an integer from 0 to size squared.
                """,
                inline=False
            )
        else:
            reply = "その言語に対応していなくて申し訳ない... :crying_cat_face:"
            await ctx.send(reply)
            embed = discord.Embed(
                title="Bot.ppnt",
                description="使用方法",
                color=discord.Color.from_rgb(255, 204, 77)
            )
            embed.add_field(
                name="`p:h [lang]`",
                value="""\
                今表示しているようにBotの使用方法が確認できます．
                langはISO-639に準拠して指定してください． 例:ja, en
                指定しなかった場合は日本語で表示されます．
                """,
                inline=False
            )
            embed.add_field(
                name="`p:s <size> <mine>`",
                value="""\
                ぽぽスイーパーを起動できます．
                sizeは1から9，mineはsizeの2乗以下を指定してください．
                """,
                inline=False
            )
        await ctx.send(embed=embed)


def setup(bot):
    return bot.add_cog(Pcommands(bot))
