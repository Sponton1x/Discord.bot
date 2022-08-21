import os
import asyncio
from aiohttp import ClientConnectorError
from discord.ext import commands
from discord import Intents

TOKEN = "token"
CLIENT_ID = id_bota


intents = Intents.all()
intents.typing = False
intents.presences = False

client = commands.Bot(
command_prefix=".", intents=intents,
case_insensitive=True, application_id=CLIENT_ID)

client.remove_command("help")

@client.event
async def on_ready(client=client):
    print(f"Hello There {round(client.latency*1000)}ms")
    await client.change_presence(activity=discord.Game(name="MAybe Change!"))


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
              await client.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e:
              print(e)


async def main():
    async with client:
        try:
            await load_extensions()
            await client.start(TOKEN)
        except ClientConnectorError:
            print("Bot cannot connect to host")
        except Exception as e:
            print(e)


asyncio.run(main())
