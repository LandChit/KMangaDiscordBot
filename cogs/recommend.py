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


class Recommend(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.count = 0
        
        
    # you can remove this if you want to
    @commands.Cog.listener()
    async def on_ready(self):
        print(__name__[5:])

    # -----------------------------------

    
    
    # main command
    @nextcord.slash_command(description='recommendations', guild_ids=vrs.GUILD_ID)
    async def recommend(self, interaction: Interaction):
        ...

    # comics
    @recommend.subcommand(description='recommends comics')
    async def comics(
        self,
        interaction: Interaction,
        tags: str = SlashOption(description='tags/genre seperate by using \',\'', required=False),
    ):
        path = './database/comic/'
        if tags != None:
            files = lgc.checktags(path,tags)
        else:
            files = os.listdir(path)
        try:
            final = random.choice(files)
        except IndexError:
            final = None
        print(final)
        

    # manhwa/manhwua
    @recommend.subcommand(description='recommends manhwa/manhwua')
    async def manhwa(
        self,
        interaction: Interaction,
        tags: str = SlashOption(description='tags/genre seperate by using \',\'', required=False),
    ):
        await interaction.response.send_message('first sub command')

    # manga
    @recommend.subcommand(description='recommends manga')
    async def manga(
        self,
        interaction: Interaction,
        tags: str = SlashOption(description='tags/genre seperate by using \',\'', required=False),
    ):
        await interaction.response.send_message('first sub command')


def setup(client):
    client.add_cog(Recommend(client))
