import logging as logger

from discord import app_commands, Intents, Object
from discord.ext import commands

from commands import MySlashCog

__version__ = "1.0.1"

logger.basicConfig(level=logger.DEBUG)


class MySlashBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix="/", intents=Intents.all())
    
    async def on_ready(self):
        logger.info("SplineBot has loaded. Version: %s" % __version__)

    async def setup_hook(self) -> None:
        await self.add_cog(MySlashCog(self))
        await self.tree.sync(guild=None)
