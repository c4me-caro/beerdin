import discord
from discord.ext import commands

class General(commands.Cog, name="GeneralCog"):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="help")
    async def help(self, ctx):
        embed_help=discord.Embed(title="**Helper**")
        embed_help.add_field(name="**Test**", value="**Prueba ok**", inline=True)
        await self.bot.typing(ctx,embed=embed_help,time=1)
        
    @discord.slash_command(name='ping')
    async def ping(self, ctx):
        await ctx.respond('Pong! {0}'.format(round(self.bot.latency, 1)))

    @discord.slash_command(name='avatar')
    async def avatar(self, ctx, member_id):
        try:
            member_id = member_id.replace("<@", "").replace(">", "")
            member = await self.bot.fetch_user(member_id)
            if member.avatar != "":
                embed = discord.Embed(
                    title='@{}\'s avatar'.format(member.name))
                embed.set_image(url=member.avatar)
                embed.set_footer(
                    icon_url=ctx.author.avatar, text="Image requested by: {}".format(ctx.author))
                await self.bot.typing(ctx, embed=embed)
            else:
                await ctx.respond("User has no avatars to show.")
                
        except Exception as e:
            await ctx.respond("Error: {}".format(e))
            return

def setup(bot):
    bot.add_cog(General(bot))