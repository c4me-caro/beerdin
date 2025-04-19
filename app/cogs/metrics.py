from discord.ext import commands
from collections import Counter
import discord
from datetime import datetime, timedelta
from db.dblogguer import Messages, Reactions, new_message, new_reaction

class MetricsCog(commands.Cog, name="MetricsCog"):
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(name="analytics")
    @commands.has_any_role('admin')
    async def analytics(self, ctx, period: int = 30):
        now = datetime.now()
        last_period = now - timedelta(days=period)

        counter = 0
        async for message in ctx.channel.history(limit=999999, after=last_period):
            if message.author.bot:
                continue
            
            mesg = Messages(message.id, message.content, message.author.id, message.channel.id, message.created_at)
            new_message(mesg)
            counter += 1
            
            for reaction in message.reactions:
                if isinstance(reaction.emoji, str):
                    emoji = reaction.emoji
                else:
                    emoji = reaction.emoji.name
                
                rea = Reactions(message.id, emoji, message.author.id, message.created_at)
                new_reaction(rea)
        
        embed = discord.Embed(title="Analytics")
        embed.add_field(name="Total Analyzed Messages", value=str(counter), inline=False)
        
        await self.bot.typing(ctx, embed=embed)
        
def setup(bot):
    bot.add_cog(MetricsCog(bot))