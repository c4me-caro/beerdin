from config import getConfig
from utils.bot_utils import BeerdinBot, typing
import discord
from collections import Counter
from datetime import datetime, timedelta, timezone
from cogs import events, general

bot = BeerdinBot()
extensions = ['general', 'events']

def load_bot():
    for extension in extensions:
        try:
            bot.load_extension(f'bot.commands.{extension}')
        except Exception as e:
            print(f"Error loading extension {extension}: {e}")

if __name__ == "__main__":
    load_bot()
    bot.run(getConfig().DISCORD_TOKEN.get_secret_value())
