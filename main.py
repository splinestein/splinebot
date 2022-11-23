# -*- encoding: utf-8 -*-

# Dependencies
import requests
import json
import argparse
import asyncio
import time
import logging as logger

from discord import app_commands, Intents, Client, Interaction, ui, ButtonStyle, Embed, Color, Object
from discord.ext import commands
from configparser import ConfigParser
from requests.exceptions import HTTPError

from setup import MySlashBot


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Splinebot help args.')
    # Args to be added.
    args = parser.parse_args()

    # Fetch token from the config file.
    config = ConfigParser()
    config.read('conf.ini')

    # Run SplineBot.
    client = MySlashBot()
    client.run(config['settings']['token'])
