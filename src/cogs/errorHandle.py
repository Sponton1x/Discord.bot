import traceback
from discord.ext import commands
import discord

TEXT = "Exception"

class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
            if isinstance(error, commands.CommandOnCooldown):
                msg = 'Cooldown is on{:.2f}s.'.format(error.retry_after)
                em13 = discord.Embed(title=f"{TEXT}",description=msg,color=discord.Color.red())
                await ctx.send(embed=em13)

            if isinstance(error, commands.MissingRequiredArgument):
                msg = 'Unable arguments this cmd.'
                em13 = discord.Embed(title=f"{TEXT}",description=msg,color=discord.Color.red())
                await ctx.send(embed=em13)

            if isinstance(error, commands.MissingPermissions):
                msg3 = "You don't have permission for this cmd"
                em15 = discord.Embed(title=f"{TEXT}",description=msg3, color=discord.Color.red())
                await ctx.send(embed=em15)

            if isinstance(error, commands.CommandNotFound):
                msg4 = "Cmd not found"
                em16 = discord.Embed(title=f"{TEXT}", description=msg4,color=discord.Color.red())
                await ctx.send(embed=em16)


async def setup(client):
    await client.add_cog(Errors(client))
