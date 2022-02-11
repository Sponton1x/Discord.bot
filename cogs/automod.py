import discord
from discord.ext import commands
import datetime

class AutoMod(commands.Cog):
  
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def on_member_join(member):
      now = datetime.datetime.now()
      diff = now - member.created_at
      if diff.total_seconds() < 86400:
          await member.send("Due to an influx of raids, your account has been deemed to young to join this server.")
          await member.kick()

def setup(client):
    client.add_cog(AutoMod(client))