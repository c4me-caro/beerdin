from discord.ext import commands
from db.dblogguer import new_message, Messages, new_reaction, Reactions, new_voice_log, VoiceLog
import datetime

class Events(commands.Cog, name="EventsCog"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}')

    @commands.Cog.listener()
    async def on_disconnect(self):
        print("Bot was disconnected")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if self.bot.user in message.mentions and not message.content.startswith(self.bot.command_prefix):
            await message.channel.send(f'Hola, necesitas algo? Puedes usar `{ self.bot.command_prefix }help` para obtener ayuda ^^')
        
        message = Messages(message.id, message.content, message.author.id, message.channel.id, message.created_at)
        new_message(message)
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        if reaction.user_id == self.bot.user.id:
            return

        reaction = Reactions(reaction.message_id, reaction.emoji.name, reaction.user_id, datetime.datetime.now())
        new_reaction(reaction)
        
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.bot:
            return
        
        if after.channel is not None:
            channel = VoiceLog(member.id, after.channel.id, datetime.datetime.now(), "join")
            new_voice_log(channel)
            
        elif before.channel is not None and after.channel is None:
            channel = VoiceLog(member.id, before.channel.id, datetime.datetime.now(), "leave")
            new_voice_log(channel)
            
def setup(bot):
    bot.add_cog(Events(bot))