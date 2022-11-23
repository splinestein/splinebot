# -*- encoding: utf-8 -*-

from discord.ext import commands
from discord import app_commands, Interaction, Color, Embed

from views import SimpleEmbed, SimpleButton
from setup import logger


class CommandsCog(commands.Cog):
    """ A cog is a collection of commands, listeners, and optional state to help group commands together. """
    def __init__(self, bot: commands.Bot) -> None:
        """ Initialize the cog. """
        self.bot = bot

    @app_commands.command(name="ping", description="Ping the bot, check if it works.")
    async def _ping(self, interaction: Interaction):
        """ Pings the bot. """
        await interaction.response.send_message("Pong!")

    @app_commands.command(name="say", description="Make the bot say something.")
    @app_commands.describe(say="Write something for the bot to say.")
    async def _say(self, interaction: Interaction, say: str):
        """ Makes the bot respond with what the user wrote. """
        await interaction.response.send_message("You wrote %s" % say)


    @app_commands.command(name='get-request', description='Make a GET request to any API.')
    @app_commands.describe(url="URL / Endpoint / API")
    async def _get_request(self, interaction: Interaction, url: str) -> None:
        """ Makes a GET request to a URL and prints the response. """

        embedClass = SimpleEmbed()
        embedResult = embedClass.simple(
            color=Color.from_rgb(225, 198, 153), author="GET Request.", field=url, value="Do you confirmmmmm?")
        await interaction.channel.send(embed=embedResult)

        # Prompt confirmation.
        buttonClass = SimpleButton()
        buttonClass.url = url
        await interaction.response.send_message(view=buttonClass)