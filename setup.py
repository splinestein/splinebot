# -*- encoding: utf-8 -*-

import logging as logger

from discord import app_commands, Intents, Object
from discord.ext import commands

from commands import CommandsCog
from listeners import ListenersCog

logger.basicConfig(level=logger.DEBUG)


class SplineBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix="/", intents=Intents.all())

    async def setup_hook(self) -> None:
        await self.add_cog(ListenersCog(self))
        await self.add_cog(CommandsCog(self))
        await self.tree.sync(guild=None)
