from discord.ext import commands
import discord


class Pcommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="helps", aliases=["h"])
    async def help(self, ctx, lang="ja"):
        if lang == "ja":
            embed = discord.Embed(
                title="Bot.ppnt",
                description="使用方法",
                color=discord.Color.from_rgb(255, 204, 77)
            )
            embed.add_field(
                name="`p:helps [lang]`",
                value="""\
                今表示しているようにBotの使用方法が確認できます．
                langはISO-639に準拠して指定してください． 例:ja, en
                指定しなかった場合は日本語で表示されます．
                エイリアス: `h`
                """,
                inline=False
            )
            embed.add_field(
                name="`p:psweeper <size> <mine>`",
                value="""\
                ぽぽスイーパーを起動できます．
                sizeは1から9，mineはsizeの2乗以下を指定してください．
                エイリアス: `s, ps, sweep, sweeper`
                """,
                inline=False
            )
            embed.add_field(
                name="`p:poponfuck [script]`",
                value="""\
                    Poponfuckを実行できます．コマンドは半角スペースで区切ってください．
                    コマンド一覧
                    +: :thinking:
                    -: :rage:
                    >: :thinking::thinking:
                    <: :rage::rage:
                    [: :thinking::rage:
                    ]: :rage::thinking:
                    .: :crying_cat_face:
                    エイリアス: `pf, pfuck`
                """,
                inline=False
            )
            embed.add_field(
                name="`p:popochem [化合物名]`",
                value="""\
                    化合物名から構造式を検索できます．
                    また，IUPAC名や分子式，分子量も表示されます．
                    エイリアス: `pc, pchem, chem, c`
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
                name="`p:helps [lang]`",
                value="""\
                As you see, you can check how to use this bot.
                For lang, give a language code based on ISO 639. e.g. ja, en
                If not given lang, display in Japanese.
                Alias: `h`
                """,
                inline=False
            )
            embed.add_field(
                name="`p:psweeper <size> <mine>`",
                value="""\
                You can play poposweeper.
                For size, specify a positive integer from 1 to 9, and for mine, give an integer from 0 to size squared.
                For example, if size is 6, you can specify mine from 0 to 36.
                Aliases: `s, ps, sweep, sweeper`
                """,
                inline=False
            )
            embed.add_field(
                name="`p:poponfuck [script]`",
                value="""\
                    You can run Poponfuck script. To separate each command, insert half-width space between emojis.
                    Commands
                    +: :thinking:
                    -: :rage:
                    >: :thinking::thinking:
                    <: :rage::rage:
                    [: :thinking::rage:
                    ]: :rage::thinking:
                    .: :crying_cat_face:
                    Aliases: `pf, pfuck`
                """,
                inline=False
            )
            embed.add_field(
                name="`p:popochem [compound name]`",
                value="""\
                    You can search for structural formula by compound name.
                    Also, IUPAC name, molecular formula and its weight are displayed.
                    Aliases: `pc, pchem, chem, c`
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
                name="`p:helps [lang]`",
                value="""\
                今表示しているようにBotの使用方法が確認できます．
                langはISO-639に準拠して指定してください． 例:ja, en
                指定しなかった場合は日本語で表示されます．
                エイリアス: `h`
                """,
                inline=False
            )
            embed.add_field(
                name="`p:psweeper <size> <mine>`",
                value="""\
                ぽぽスイーパーを起動できます．
                sizeは1から9，mineはsizeの2乗以下を指定してください．
                エイリアス: `s, ps, sweep, sweeper`
                """,
                inline=False
            )
            embed.add_field(
                name="`p:poponfuck [script]`",
                value="""\
                    Poponfuckを実行できます．コマンドは半角スペースで区切ってください．
                    コマンド一覧
                    +: :thinking:
                    -: :rage:
                    >: :thinking::thinking:
                    <: :rage::rage:
                    [: :thinking::rage:
                    ]: :rage::thinking:
                    .: :crying_cat_face:
                    エイリアス: `pf, pfuck`
                """,
                inline=False
            )
            embed.add_field(
                name="`p:popochem [化合物名]`",
                value="""\
                    化合物名から構造式を検索できます．
                    また，IUPAC名や分子式，分子量も表示されます．
                    エイリアス: `pc, pchem, chem, c`
                """,
                inline=False
            )
        await ctx.send(embed=embed)


def setup(bot):
    return bot.add_cog(Pcommands(bot))
