# -*- encoding: utf-8 -*-

from discord.ext import commands

from setup import logger


class ListenersCog(commands.Cog):
    """ A cog is a collection of commands, listeners, and optional state to help group commands together. """
    def __init__(self, bot: commands.Bot) -> None:
        """ Initialize the cog. """
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("SplineBot has loaded")

    @commands.Cog.listener()
    async def on_message(self, message):
        logger.info("Message was sent by: %s" % message.author)
