from discord.ext import commands
from db.dblogguer import new_message, Messages

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
        
        message = Messages(message.id, message.content, message.author.id, message.channel.id, message.created_at, [])
        new_message(message)

def setup(bot):
    bot.add_cog(Events(bot))