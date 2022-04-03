import nextcord
from nextcord.ext import commands
import os
import dotenv

dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN')

client = commands.Bot(command_prefix=['.'])


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename != "VARS.py":
        if filename != "LOGIC.py":
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
