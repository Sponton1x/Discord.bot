import discord
from discord.ext import commands

class Spotify(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def track(self ,ctx, user:discord.Member=None):
        user = user or ctx.author
        spotify_results = next((activity for activity in user.activities if isinstance(activity,discord.Spotify)),None)

        if spotify_results is None:
            await ctx.send(f"{user.name} don't listening Spotify.")

        await ctx.send(f"https://open.spotify.com/track/{spotify_results.track_id}")

def setup(client):
    await client.add_cog(Spotify(client))
