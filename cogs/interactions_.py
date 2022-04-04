import os
import random
from discord import SlashOption
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from . import LOGIC as lgc
from . import VARS as vrs

# make sure to go on your aplication settings 'OAuth2 URL generator'
# and enable aplications.commands
# re-invite your bot if already joined


class Interactions_(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.count = 0
        self.color = 0x990300

    # you can remove this if you want to
    @commands.Cog.listener()
    async def on_ready(self):
        print(__name__[5:])

    # -----------------------------------

    # main command
    @nextcord.slash_command(description="suggestions", guild_ids=vrs.GUILD_ID)
    async def add(self, interaction: Interaction):
        ...

    # comics
    @add.subcommand(name="comics", description="suggests comics")
    async def comics(
        self,
        interaction: Interaction,
        suggestion: str = SlashOption(
            description="title"
        ),
    ):
        with open('./suggest/satisfied.txt') as fb:
            fb = fb.read()
            if suggestion not in fb:
                with open('./suggest/comic.txt', 'a')as f:
                        f.write(suggestion)
                        await interaction.response.send_message('thank you for suggesting, we will review your suggestion', delete_after=5)
            else:
                await interaction.response.send_message('already satisfied', delete_after=5)


    # manhwa/manhwua
    @add.subcommand(name="manhwa", description="suggests manhwa/manhwua")
    async def manhwa(
        self,
        interaction: Interaction,
        suggestion: str = SlashOption(
            description="title"
        ),
    ):
        with open('./suggest/satisfied.txt') as fb:
            fb = fb.read()
            if suggestion not in fb:
                with open('./suggest/manhwa.txt', 'a')as f:
                        f.write(suggestion)
                        await interaction.response.send_message('thank you for suggesting, we will review your suggestion', delete_after=5)
            else:
                await interaction.response.send_message('already satisfied', delete_after=5)


    # manga
    @add.subcommand(name="manga", description="suggests manga")
    async def manga(
        self,
        interaction: Interaction,
        suggestion: str = SlashOption(
            description="title"
        ),
    ): 
        with open('./suggest/satisfied.txt') as fb:
            fb = fb.read()
            if suggestion not in fb:
                with open('./suggest/manga.txt', 'a')as f:
                        f.write(suggestion)
                        await interaction.response.send_message('thank you for suggesting, we will review your suggestion', delete_after=5)
            else:
                await interaction.response.send_message('already satisfied', delete_after=5)



def setup(client):
    client.add_cog(Interactions_(client))
