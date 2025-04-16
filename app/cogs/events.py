from discord.ext import commands

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
            return

def setup(bot):
    bot.add_cog(Events(bot))