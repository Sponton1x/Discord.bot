import discord
from discord.ext import commands
import asyncio


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed()
        for cmd in self.client.commands:
          embed.add_field(name=cmd.name, value="aliases: "+" ".join(cmd.aliases))
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Help(client))
