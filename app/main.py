from config import getConfig
from utils.bot_utils import BeerdinBot
import discord
from db import dblogguer, models

bot = BeerdinBot(prefix="/", intents=discord.Intents.all())
extensions = ['general', 'events', 'metrics', 'admin']

def load_bot():
    for extension in extensions:
        try:
            bot.load_extension(f'cogs.{extension}')
        except Exception as e:
            print(f"Error loading extension {extension}: {e}")

if __name__ == "__main__":
    load_bot()
    models.init_db()  
    dblogguer.init_db()
    bot.run(getConfig().DISCORD_TOKEN.get_secret_value())