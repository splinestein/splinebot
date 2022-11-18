# -*- encoding: utf-8 -*-

# Dependencies
import requests
import json
import argparse
import asyncio
import time
import logging as logger

from discord import app_commands, Intents, Client, Interaction, ui, ButtonStyle, Embed, Color
from configparser import ConfigParser
from requests.exceptions import HTTPError

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


class Menu(ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @ui.button(label="Confirm", style=ButtonStyle.green)
    async def menu1(self, interaction: Interaction, button: ui.Button):
        embed = Embed(color=Color.random())
        embed.set_author(name=f"Confirm GET request.")
        embed.add_field(name="You are about to send a GET request.", value="Confirm it.")
        await interaction.response.edit_message(embed=embed)


client = SplineBot(intents=Intents.default())


@client.event
async def on_ready():
    logger.info("SplineBot loaded, version: %s" % __version__)


@client.tree.command(name='hello', description='wot')
@app_commands.describe(text="The text to send!")
async def _hello(interaction: Interaction, text: str) -> None:
    """ The hello command. """
    await interaction.response.send_message("Hey %s, you wrote: '%s' into the channel: %s" % (interaction.user, text, interaction.channel))


@client.tree.command(name='get-request', description='Make a GET request to any API.')
@app_commands.describe(url="URL / Endpoint / API")
async def _get_request(interaction: Interaction, url: str) -> None:
    """ Makes a GET request to a URL and prints the response. """

    # Prompt confirmation.
    view = Menu()
    await interaction.channel.send(view=view)

    # Send request (Still need to do interaction response.)
    try:
        response = requests.get(url)
        response.raise_for_status()

        jsonResponse = response.json()
        paragraph = json.dumps(jsonResponse, indent=4).strip()

        SPLIT_AT_LEN = 1988

        formatting = [paragraph[i: i + SPLIT_AT_LEN] for i in range(0, len(paragraph), SPLIT_AT_LEN)]

        for splits in formatting:
            #await interaction.response.defer()
            await asyncio.sleep(1) # Doing stuff
            await interaction.channel.send("```json\n%s```" % splits)
            #await interaction.followup.send("```json\n%s```" % splits)


    except HTTPError as http_err:
        await interaction.response.send_message(f'HTTP error occurred: {http_err}')
    except Exception as err:
        await interaction.response.send_message(f'Other error occurred: {err}')


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
