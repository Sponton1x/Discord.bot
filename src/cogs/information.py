import discord
from discord.ext import commands
import random
import datetime

class Information(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["guild", "guildinfo", "si"])
    async def serverinfo(self, ctx):

        findbots = sum(1 for member in ctx.guild.members if member.bot)
        roles = sum(1 for role in ctx.guild.roles)

        embed = discord.Embed(title = 'Infomation about ' + ctx.guild.name + '.', colour = ctx.author.color)
        embed.set_thumbnail(url = str(ctx.guild.icon_url))
        embed.add_field(name = "Guild's nazwa: ", value = ctx.guild.name)
        embed.add_field(name = "Guild's właściciel: ", value = str(ctx.guild.owner))
        embed.add_field(name = "Guild's stopień weryfikacji: ", value = str(ctx.guild.verification_level))
        embed.add_field(name = "Guild's id: ", value = f"`{ctx.guild.id}`")
        embed.add_field(name = "Guild's liczba członków: ", value = f"{ctx.guild.member_count}")
        embed.add_field(name="Bots", value=f"`{findbots}`", inline=True)
        embed.add_field(name = "Guild Stworzono: ", value = str(ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.add_field(name = "Liczba roli:", value = f"`{roles}`")
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

        await ctx.send(embed =  embed)

    @commands.command(aliases = ["ci"])
    async def channelinfo(self, ctx, channel : discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel

        em = discord.Embed(title = f"Informacje o {channel.name}", color = ctx.author.color, description = f"Here is an insight into {channel.mention}")
        em.add_field(name = "ID:", value = f"`{channel.id}`")
        em.add_field(name = "Nazwa:", value = f"`{channel.name}`")
        em.add_field(name = "Server należy do:", value = f"{channel.guild.name}", inline = True)

        try:
            em.add_field(name = "Kategoria ID:", value = f"`{channel.category_id}`", inline = False)
        except:
            pass
        em.add_field(name = "Temat:", value = f"`{channel.topic}`")
        em.add_field(name = "Slowmode:", value = f"`{channel.slowmode_delay}`", inline = True)

        em.add_field(name = "Kto może zobaczyć kanał:", value = f"`{len(channel.members)}`", inline = False)
        em.add_field(name = "Czy NSFW:", value = f"`{channel.is_nsfw()}`")
        em.add_field(name = "Czy News:", value = f"`{channel.is_news()}`", inline = True)

        em.set_footer(text = f"Wywołane przez {ctx.author.name}", icon_url = ctx.author.avatar_url)
        em.set_thumbnail(url = str(ctx.guild.icon_url))
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

        await ctx.send(embed = em)

    @commands.command(aliases = ["ui"])
    async def userinfo(self, ctx, member : discord.Member = None):
        if member == None:
            member = ctx.author
        pos = sum(m.joined_at < member.joined_at for m in ctx.guild.members if m.joined_at is not None)
        roles = [role for role in member.roles]
        embed = discord.Embed(title = "👨 Info", color = discord.Color.random(), description = f"Informacje o: {member.name}")
        embed.add_field(name = "Nickname", value = member.nick or None)
        embed.add_field(name = "Stopień weryfikacji", value = member.pending)
        embed.add_field(name = "Status:", value = member.raw_status)
        if member.mobile_status:
            device = "Mobile"
        elif member.desktop_status:
            device = "Desktop"
        elif member.web_status:
            device=  "Web"
        embed.add_field(name = "discord Urządzenie:", value = device)
        embed.add_field(name = "Color", value = member.color)
        embed.add_field(name = "wzmianka:", value = member.mention)
        embed.add_field(name = "Top Role:", value = member.top_role.mention)
        embed.add_field(name = "Voice State:", value = member.voice or None)
        embed.set_footer(icon_url=member.avatar_url, text=f'Wywołane przez: {ctx.author.name}')
        await ctx.send(embed=embed)


    @commands.command(aliases = ["bi"])
    async def botinfo(self, ctx):
        embed = discord.Embed(title = "Botinfo", color = ctx.author.color,)
        embed.add_field(name = "Pierwsze uruchomienie:", value = "1 / 10 / 2020")
        embed.add_field(name = "Zaczęto Prace:", value = "26 / 9 / 2020")
        embed.add_field(name = f"Stwórca", value = f"Sponton#4170")
        embed.add_field(name = "Servery:", value = f'`{len(self.client.guilds)}`')
        embed.add_field(name = "Użytkownicy:", value = f'`{len(self.client.users)}`')
        await ctx.send(embed = embed)

async def setup(client):
    await client.add_cog(Information(client))
