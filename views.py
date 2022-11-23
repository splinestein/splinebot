# -*- encoding: utf-8 -*-

from discord import app_commands, Intents, Client, Interaction, ui, ButtonStyle, Embed, Color, Object
from requests.exceptions import HTTPError

class SimpleEmbed():
    def __init__(self):
        super().__init__()

    def simple(self, color, author, field, value):
        """ Creates a simple embed. Color.from_rgb(225, 198, 153)"""
        embed = Embed(color=color)
        embed.set_author(name=author)
        embed.add_field(name=field, value=value)
        return embed


class SimpleButton(ui.View):
    def __init__(self):
        super().__init__()
        self.url = ""

    @ui.button(label="Send", style=ButtonStyle.green)
    async def send_get(self, interaction: Interaction, button: ui.Button):
        """ Once the button has been pressed, this gets executed. """

        try:
            response = requests.get(self.url)
            response.raise_for_status()

            jsonResponse = response.json()
            paragraph = json.dumps(jsonResponse, indent=4).strip()

            SPLIT_AT_LEN = 1988

            formatting = [paragraph[i: i + SPLIT_AT_LEN] for i in range(0, len(paragraph), SPLIT_AT_LEN)]

            for splits in formatting:
                await asyncio.sleep(1) # Doing stuff
                await interaction.channel.send("```json\n%s```" % splits)

            await interaction.response.send_message(f'HTTP success: {response.status_code}')

        except HTTPError as http_err:
            await interaction.response.send_message(f'HTTP error occurred: {http_err}')

        except Exception as err:
            await interaction.response.send_message(f'Other error occurred: {err}')
