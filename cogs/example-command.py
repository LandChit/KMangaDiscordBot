import nextcord
from nextcord.ext import commands


class ExampleCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # you can remove this if you want to
    @commands.Cog.listener()
    async def on_ready(self):
        print(__name__[5:])

    # -----------------------------------

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.client.latency*1000)}ms')


def setup(client):
    client.add_cog(ExampleCommands(client))
