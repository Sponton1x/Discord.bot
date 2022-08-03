import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions, BadArgument

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["giverole", "addr"])
    @commands.guild_only()
    @has_permissions(manage_roles = True)
    async def addrole(self, ctx, member : discord.Member = None, role : discord.Role = None,*,reason = None):
        if member is None:
            embed = discord.Embed(title = "Addrole Failed!", color= ctx.author.color)
            embed.add_field(name = "Powód:", value = "Spinguj członka któremu chcesz przyznać role")
            embed.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        if role is None:
            embed = discord.Embed(title = "Nieprawidłowe dodanie roli!", color= ctx.author.color)
            embed.add_field(name = "Powód:", value = "Spinguj role".format(member.mention))
            embed.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        try:
            addRole = True
            for role_ in member.roles:
                if role_ == role:
                    addRole = False
                    break
            if not addRole:
                embed = discord.Embed(title = " Add Role Failed!", color= ctx.author.color)
                embed.add_field(name = "Reason:", value = "Nie mogę dodać roli!".format(member.mention))
                embed.add_field(name = "Dlaczego?",value = f"{member.mention} już posiada {role.mention}, więc...")
                embed.set_footer(text = "-_-")
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                em = discord.Embed(title=  " Add Role Successful!", color = ctx.author.color, description = f"Dodałem {member.mention} role {role.mention}")
                em.add_field(name = "Powód:", value = f"`{reason}`")
                em.add_field(name = "Użytkownik:", value = f"{member.mention}")
                em.add_field(name = "Rola:", value = f"{role.mention}", inline = True)
                em.add_field(name ="Moderator:", value = f"{ctx.author.mention}", inline = False)
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = em)
                await member.add_roles(role)
                return
        except:
            embed = discord.Embed(title = "Dodanie roli nieprawidłowe!", color= ctx.author.color)
            embed.add_field(name = "Reason:", value = "Nie mogę dodać roli".format(member.mention))
            embed.add_field(name = "Dlaczego?",value = "Ta rola jest wyżej niż moja, nie mam uprawnień")
            embed.set_footer(text = "-_-, nie mam uprawnień")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
    
    @commands.command(aliases=["takerole", "remover"])
    @commands.guild_only()
    @has_permissions(manage_roles = True)
    async def removerole(self, ctx, member : discord.Member = None, role : discord.Role = None,*,reason = None):
        if member is None:
            embed = discord.Embed(title = "Zdjęcie roli nieprawidłowe!", color= ctx.author.color)
            embed.add_field(name = "Powód:", value = "Nie podałeś użytkownika któremu mam nadać role!")
            embed.set_footer(text = "-_-")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        if role is None:
            embed = discord.Embed(title = "Zdjęcie roli nieprawidłowe!", color= ctx.author.color)
            embed.add_field(name = "Powód:", value = "Nie określiłeś roli którą mam nadać!".format(member.mention))
            embed.set_footer(text = "-_-")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        try:
            roleRemoved = False
            for role_ in member.roles:
                if role_ == role:
                    await member.remove_roles(role)
                    roleRemoved = True
                    return
            if not roleRemoved:
                embed = discord.Embed(title = "Zdjęcie roli nieprawidłowe!", color= ctx.author.color)
                embed.add_field(name = "Powód:", value = "Nie mogę usunąć roli{}!".format(member.mention))
                embed.add_field(name = "Dlaczego?",value = f"{member.mention} nie posiada {role.mention}, więc co mam robić?")
                embed.set_footer(text = "-_-")
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                em = discord.Embed(title=  "Zdjęcie roli poprawne!", color = ctx.author.color, description = f"Odebrałem role {role.mention} użytkownikowi {member.mention}")
                em.add_field(name = "Powód:", value = f"`{reason}`")
                em.add_field(name = "Użytkownik:", value = f"{member.mention}")
                em.add_field(name = "Rola:", value = f"{role.mention}", inline = True)
                em.add_field(name ="Moderator:", value = f"{ctx.author.mention}", inline = False)
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = em)
                return
        except:
            embed = discord.Embed(title = "Zdjęcie roli nieprawidłowe!", color= ctx.author.color)
            embed.add_field(name = "Powód:", value = "Nie mogę odebrać roli!".format(member.mention))
            embed.add_field(name = "Dlaczego?",value = "Ta rola jest wyżej niż moja, nie mam uprawnień!")
            embed.set_footer(text = "-_-, nie mam uprawnień")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def createrole(self, ctx, *, name = "NieznanaRola"):
        role=  await ctx.guild.create_role(name = name)
        em = discord.Embed(title = "Rola Stworzona", color = ctx.author.color, description = f"Rola {role.mention} została poprawnie utworzona!")
        em.add_field(name = "Rola:", value = f"{role.mention}")
        em.add_field(name ="Moderator:", value = f"{ctx.author.mention}")
        em.set_footer(text = "Dobra praca z tworzniem ról!")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)


    @commands.command(aliases=["delrole"])
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def deleterole(self, ctx, *, role: discord.Role):
        em = discord.Embed(title = "Rola Usunięta", color = ctx.author.color, description = f"Rola {role.mention}została poprawne usunięta!")
        em.add_field(name = "Rola:", value = f"{role.mention}")
        em.add_field(name ="Moderator:", value = f"{ctx.author.mention}")
        em.set_footer(text = "o wow")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

        await role.delete(reason = f"{ctx.author.name} pytałem o to!")
 

    @commands.command()
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def lock(self, ctx, *, reason = None):
        channel = ctx.channel
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)
        em = discord.Embed(title = f"Kanał został zablokowany!", color = discord.Color.green(), description = f"Kanał {channel.mention} zaostał poprawnie zablokowany!")
        em.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
        em.add_field(name = "Powód:", value = f"`{reason}`")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.channel.send(embed = em)



    @commands.command()
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def unlock(self, ctx, *, reason = None):
        channel = ctx.channel
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)
        em = discord.Embed(title = f"Kanał został odblokowany!", color = discord.Color.green(), description = f"Kanał{channel.mention} został poprawnie odblokowany!")
        em.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
        em.add_field(name = "Powód:", value = f"`{reason}`")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.channel.send(embed = em)

    @commands.command()
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def setdelay(self, ctx, amount = 5, *, reason = None):
        if amount > 6000:
            await ctx.channel.send("Liczba niższa niż 6000!")
            return
        try:
            amount = int(amount)
        except:
            em = discord.Embed(title = "Niepoprawnie ustawione opóżnienie!", color = ctx.author.color)
            em.add_field(name = "Powód:", value = "Wartość musi być liczbą człkowitą")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
            return
        
        if ctx.channel.slowmode_delay != amount:
            await ctx.channel.edit(slowmode_delay=amount)
        else:
            embed = discord.Embed(title = "Niepoprawnie ustawione opóżnienie!", color = ctx.author.color)
            embed.add_field(name = "Powód:", value = f"Ten kanał ma już opóżnienie, oraz wynosi `{amount}`!")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        em = discord.Embed(title = "zmienione ustawienia kanału", color = ctx.author.color)
        em.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
        em.add_field(name = "Powód:", value = f"`{reason}`")
        em.add_field(name=  "Opis", value = f"Teraz kanał ma opóżnienie na\n {amount}", inline = False)
        em.add_field(name = "Slowmode", value = f"`{amount} sekund`")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

def setup(client):
    client.add_cog(Moderation(client))