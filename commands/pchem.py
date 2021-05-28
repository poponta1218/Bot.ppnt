from discord.ext import commands
import discord
import os
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from googletrans import Translator


class Pcommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="popochem", aliases=["pc", "pchem", "chem", "c"])
    async def popochem(self, ctx, *, name: str):
        outstr = ""
        properties = [
            "IUPACName",
            "MolecularFormula",
            "MolecularWeight",
            "CanonicalSMILES"
        ]
        translator = Translator()
        name = translator.translate(text=name, dest="en").text
        rslt = pcp.get_properties(properties, name, "name")
        if rslt == []:
            outstr += "検索した分子は見つかりませんでした．\nタイプミス等の可能性があります．"
            await ctx.send(outstr)
        else:
            smiles = rslt[0].get("CanonicalSMILES")
            if rslt[0].get("IUPACName") is not None:
                iupac_name = "IUPAC名: " + rslt[0].get("IUPACName") + "\n"
            else:
                iupac_name = ""
            mol_info = "分子式 (分子量): " + rslt[0].get("MolecularFormula") + \
                " (" + rslt[0].get("MolecularWeight") + ")"
            outstr += iupac_name + mol_info
            view = rdMolDraw2D.MolDraw2DCairo(330, 300)
            options = view.drawOptions()
            options.legendFontSize = 24
            options.multipleBondOffset = 0.1
            options.useBWAtomPalette()
            struct = rdMolDraw2D.PrepareMolForDrawing(Chem.MolFromSmiles(smiles))
            view.DrawMolecule(struct)
            view.FinishDrawing()
            view.WriteDrawingText("structure.png")
            img_path = discord.File("structure.png")
            await ctx.send(outstr, file=img_path)
            os.remove("structure.png")


def setup(bot):
    return bot.add_cog(Pcommands(bot))
