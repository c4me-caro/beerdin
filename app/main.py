from config import getConfig
from utils.bot_utils import BeerdinBot
import discord

bot = BeerdinBot(prefix="pe/", intents=discord.Intents.all())
extensions = ['general', 'events', 'metrics']

def load_bot():
    for extension in extensions:
        try:
            bot.load_extension(f'cogs.{extension}')
        except Exception as e:
            print(f"Error loading extension {extension}: {e}")

if __name__ == "__main__":
    load_bot()
    bot.run(getConfig().DISCORD_TOKEN.get_secret_value())
    