import discord
from discord.ext import commands

class Other(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def modmail(ctx, *, message=None):
        author = ctx.author
        if message == None:
            return await ctx.reply('Please type things to send this mail to the staff!')
        if isinstance(ctx.channel, discord.channel.DMChannel):
            channel = client.get_channel(916052253603934229)
            embed = discord.Embed(title=f"We found a new mail! 📧" ,description=f"**{message}**" ,color=0x8CFED8)
            embed.add_field(name="id",value=author.id)
            embed.set_thumbnail(url=f"{author.avatar_url}")
            await channel.send(embed=embed)
        else:
            return await ctx.reply("> Sorry but this command only works on my dm :)")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def responde(ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(f"**{ctx.message.author} Responded =>** {content}")

def setup(client):
    client.add_cog(Other(client))
