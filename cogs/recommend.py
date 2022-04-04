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
        self.color = 0x82CAA4

    # you can remove this if you want to
    @commands.Cog.listener()
    async def on_ready(self):
        print(__name__[5:])

    # -----------------------------------

    # main command
    @nextcord.slash_command(description="recommendations", guild_ids=vrs.GUILD_ID)
    async def recommend(self, interaction: Interaction):
        ...

    # comics
    @recommend.subcommand(name="comics", description="recommends comics")
    async def comics(
        self,
        interaction: Interaction,
        tags: str = SlashOption(
            description="tags/genre seperate by using ','", required=False
        ),
    ):
        path = "./database/comic/"
        if tags != None:
            files = lgc.checktags(path, tags.lower)
        else:
            files = os.listdir(path)
            tags = 'None Picked'
        try:
            pick = random.choice(files)
            print(pick)

            final = lgc.get(path + pick)

            em = nextcord.Embed(
                title='Comic Recommendation',
                description=final,
                color=self.color,
            )
            em.set_footer(text='tags satisfied: '+tags)
            await interaction.response.send_message(embed=em)
            
        except IndexError:
            await interaction.response.send_message(
                "```\nA comic with those parameters cant be found```",
                delete_after=10,
            )

    # manhwa/manhwua
    @recommend.subcommand(name="manhwa", description="recommends manhwa/manhwua")
    async def manhwa(
        self,
        interaction: Interaction,
        tags: str = SlashOption(
            description="tags/genre seperate by using ','", required=False
        ),
    ):
        path = "./database/manhwa/"
        if tags != None:
            files = lgc.checktags(path, tags.lower())
        else:
            files = os.listdir(path)
            tags = 'None Picked'

        try:
            pick = random.choice(files)
            print(pick)

            final = lgc.get(path + pick)

            em = nextcord.Embed(
                title='Manhwa Recommendation',
                description=final,
                color=self.color,
            )
            em.set_footer(text='tags satisfied: '+tags)
            await interaction.response.send_message(embed=em)

        except IndexError:
            await interaction.response.send_message(
                "```\nA manhwa with those parameters cant be found```",
                delete_after=10,
            )

    # manga
    @recommend.subcommand(name="manga", description="recommends manga")
    async def manga(
        self,
        interaction: Interaction,
        tags: str = SlashOption(
            description="tags/genre seperate by using ','", required=False
        ),
    ):
        path = "./database/manga/"
        if tags != None:
            files = lgc.checktags(path, tags.lower())
        else:
            files = os.listdir(path)
            tags = 'None Picked'

        try:
            pick = random.choice(files)
            print(pick)

            final = lgc.get(path + pick)

            em = nextcord.Embed(
                title='Manga Recommendation',
                description=final,
                color=self.color,
            )
            em.set_footer(text='tags satisfied: '+tags)
            await interaction.response.send_message(embed=em)

        except IndexError:
            await interaction.response.send_message(
                "```\nA manga with those parameters cant be found```",
                delete_after=10,
            )


def setup(client):
    client.add_cog(Recommend(client))
