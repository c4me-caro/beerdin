import discord
from discord.ext import commands

class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command(name="sync")
    @commands.has_any_role('admin')
    async def sync(self, ctx):
        await self.bot.sync_commands()
        await ctx.respond('Command tree synced.')

    @commands.command(name="clear")
    @commands.has_any_role('admin')
    async def clear(self, ctx):
        await ctx.message.channel.purge()

def setup(bot):
    bot.add_cog(Administration(bot))
