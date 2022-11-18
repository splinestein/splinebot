# -*- encoding: utf-8 -*-

# Dependencies
import requests
import argparse
import logging as logger

from discord import app_commands, Intents, Client, Interaction
from configparser import ConfigParser

__version__ = "1.0.1"

logger.basicConfig(level=logger.DEBUG)


class SplineBot(Client):
    def __init__(self, *, intents: Intents) -> None:
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    def __repr__(self) -> str:
        # To be made.
        return '__repr__ for ChatBot'

    def __str__(self) -> str:
        # To be made.
        return '__str__ for ChatBot'

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)


client = SplineBot(intents=Intents.default())


@client.event
async def on_ready():
    logger.info("SplineBot loaded, version: %s" % __version__)


@client.tree.command(name='hello', description='wot')
@app_commands.describe(text="The text to send!")
async def _hello(interaction: Interaction, text: str) -> None:
    """ The hello command. """
    await interaction.response.send_message("Hey %s, you wrote: '%s' into the channel: %s" % (interaction.user, text, interaction.channel))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Splinebot help args.')
    # Args to be added.
    args = parser.parse_args()

    # Fetch token from the config file.
    config = ConfigParser()
    config.read('conf.ini')

    # Run SplineBot.
    client.run(config['settings']['token'])
