import discord
from discord.ext import commands

class General(commands.Cog, name="GeneralCog"):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="help",aliases=["h","ayuda"])
    async def help(self, ctx):
        embed_help=discord.Embed(title="**Helper**", color=0xff0000)
        embed_help.add_field(name="**Test**", value="**Prueba ok**", inline=True)
        await self.bot.typing(ctx,embed=embed_help,time=1)

def setup(bot):
    bot.add_cog(General(bot))