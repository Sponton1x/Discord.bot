import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Administrator(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None, description="Kick a user from guild"):
        await member.kick(reason=reason)
        embed = discord.Embed(description=(f'{member} został wyrzucony za {reason} przez {ctx.author}'),
                              colour=discord.Colour.orange())

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(description=(f'{member.mention} został zbanowany za {reason} przez {ctx.author}'),
                              colour=discord.Colour.orange())

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(description=(f'{user.mention} został unbanowany. ✔️'),
                                      colour=discord.Colour.green())

                await ctx.send(embed=embed)
                return

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(description=(f'Usunięto {amount} wiadomości.'), colour=discord.Colour.orange())
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Administrator(client))
