from discord.ext import commands
import time


class Pcommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poponfuck", aliases=["pf", "pfuck"])
    async def poponfuck(self, ctx, *, tape: str):
        ptr = 0  # pointer
        pc = 0  # program_counter
        mem = {}  # memory
        message = ""
        outbytes = b""
        start = time.time()

        token_table = {
            ":thinking::thinking:": ">",
            ":rage::rage:": "<",
            ":thinking::rage:": "[",
            ":rage::thinking:": "]",
            ":thinking:": "+",
            ":rage:": "-",
            ":crying_cat_face:": ".",
            "🤔🤔": ">",
            "😡😡": "<",
            "🤔😡": "[",
            "😡🤔": "]",
            "🤔": "+",
            "😡": "-",
            "😿": ".",
            " ": ""
        }

        for emoji, instr in token_table.items():
            tape = tape.replace(emoji, instr)

        while pc < len(tape):
            if ptr not in mem:
                mem[ptr] = 0
            if tape[pc] == "+":
                mem[ptr] += 1
                if mem[ptr] == 256:
                    mem[ptr] = 0
            elif tape[pc] == "-":
                mem[ptr] -= 1
                if mem[ptr] == -1:
                    mem[ptr] == 255
            elif tape[pc] == ">":
                ptr += 1
            elif tape[pc] == "<":
                ptr -= 1
                if ptr < 0:
                    message += "ポインタは負の値をとれません"
            elif tape[pc] == ".":
                outbytes += mem[ptr].to_bytes(1, "big")
            elif tape[pc] == "[":
                if mem[ptr] == 0:
                    depth = 0
                    while True:
                        pc += 1
                        if pc >= len(tape):
                            message += "対応する]が存在しません"
                        if tape[pc] == "[":
                            depth += 1
                        if tape[pc] == "]" and depth == 0:
                            break
                        if tape[pc] == "]":
                            depth -= 1
            elif tape[pc] == ']':
                if mem[ptr] != 0:
                    depth = 0
                    while True:
                        pc -= 1
                        if pc < 0:
                            message += "対応する[が存在しません"
                        if tape[pc] == ']':
                            depth += 1
                        if tape[pc] == '[' and depth == 0:
                            break
                        if tape[pc] == '[':
                            depth -= 1
            pc += 1
            if pc == len(tape):
                break
            if time.time() - start > 5:
                message += "5秒を超えたため停止しました"
        try:
            outstr = outbytes.decode('UTF-8')
        except UnicodeDecodeError:
            message = "デコードできませんでした"
        if message != "":
            await ctx.send(message)
        else:
            await ctx.send(outstr)


def setup(bot):
    return bot.add_cog(Pcommands(bot))
