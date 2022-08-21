import discord
from discord.ext import commands

class Suggest(commands.Cog):

        def __init__(self, client):
            self.client = client

        @commands.command()
        async def suggest(self,ctx,content ):
            embed = discord.Embed(title="Propozycja", description=f"{content}")
            embed.add_field(name="ID",value=ctx.author.id)
            embed.set_footer(text=f"od {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.add_reaction("😀")
            await ctx.add_reaction("😐")
            await ctx.add_reaction("😟")

async def setup(client):
    await client.add_cog(Suggest(client))
