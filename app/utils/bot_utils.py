import discord 
from discord.ext import commands
import asyncio

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class BeerdinBot(commands.Bot, metaclass=Singleton):
    def __init__(self, prefix="/", intents=None):
        if intents is None:
            intents = discord.Intents.default()
            intents.message_content = True  # Necesario para leer mensajes
            intents.guilds = True  # Información de servidores
            intents.members = True  # Para acceder a miembros
            
        super().__init__(
            command_prefix=prefix,
            intents=intents,
            help_command=None
        )

async def typing(ctx, embed=None, time:int=2):
    async with ctx.typing():
        await asyncio.sleep(time)
    if embed:
        await ctx.send(embed=embed)
