import os
import asyncio
import json
import datetime
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents().all()
guild = discord.Guild


client = commands.Bot(command_prefix = ".")
client.remove_command("help")


@client.event
async def on_command_error(ctx,error):

    if isinstance(error, commands.CommandOnCooldown):
        msg = 'Nadal jest cooldown, spróbuj ponownie za {:.2f}s.'.format(error.retry_after)
        em13 = discord.Embed(title="Błąd",description=msg,color=discord.Color.red())
        await ctx.send(embed=em13)

    if isinstance(error, commands.MissingRequiredArgument):
        msg = 'Niepoprawny argument tej komendy.'
        em13 = discord.Embed(title="Błąd",description=msg,color=discord.Color.red())
        await ctx.send(embed=em13)

    if isinstance(error, commands.MissingPermissions):
        msg3 = "Nie masz uprawnień do tej komendy"
        em15 = discord.Embed(title="Błąd",description=msg3, color=discord.Color.red())
        await ctx.send(embed=em15)

    if isinstance(error, commands.CommandNotFound):
        msg4 = "Nie znaleziono komendy"
        em16 = discord.Embed(title="Błąd", description=msg4,color=discord.Color.red())
        await ctx.send(embed=em16)

@client.event
async def on_ready():
    print("----------------------------------------")
    print(f'{client.user} połączył się z Discordem!')
    print("----------------------------------------")
    await client.change_presence(activity=discord.Game(name="Change Prefix is available!"))

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                client.load_extension(f'cogs.{filename[:-3]}')
                print(f'✔️ Loaded {filename}')
            except Exception as e:
                print(f'❌ Failed to load {filename}')
                print(f'[ERROR] {e}')
    print("----------------------------------------")

keep_alive()

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help Command", description="Uźyj .help <komenda> aby dowiedzieć się więcej", colour=discord.Colour.blue())
    em.add_field(name="🛡️  Administrator", value="ban, mute, kick, clear, changeprefix ", inline=False)
    em.add_field(name=":information_source:  Info", value="ping, botinfo, userinfo, serverinfo", inline=False)
    em.add_field(name="🔧 Zarządzanie rolami", value="addrole, removerole , createrole , deleterole",inline=False)
    em.add_field(name="🎚️ Zarządzanie kanałami", value="setdelay, lock, unlock",inline=False)
    em.add_field(name="4Fun",value="track")
    em.add_field(name='Pomoc',value="support, modmail")
    await ctx.send(embed=em)

@help.command()
async def kick(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy kick",description="Wyrzuca osoby z danego serwera")
  em01.add_field(name="**Użycie**",value=".kick <member> [reason]",inline=False)
  em01.add_field(name="Aliansy" , value="k")
  await ctx.send(embed=em01)

@help.command()
async def ban(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy ban",description="Banuje osoby z danego serwera")
  em01.add_field(name="**Użycie**",value=".ban <member> [reason]",inline=False)
  em01.add_field(name="Aliansy" , value="b")
  await ctx.send(embed=em01)

@help.command()
async def mute(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy mute",description="Mutuje osoby z danego serwera")
  em01.add_field(name="**Użycie**",value=".mute <member> [reason]",inline=False)
  em01.add_field(name="Aliansy" , value="m")
  await ctx.send(embed=em01)

@help.command()
async def modmail(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy modmail",description="wysyła mail do moderacji bota")
  em01.add_field(name="**Użycie**",value=".modmail [reason]",inline=False)
  await ctx.send(embed=em01)

@help.command()
async def purge(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy purge",description="Czyści wiadomości z kanału")
  em01.add_field(name="**Użycie**",value=".purge <amount>",inline=False)
  em01.add_field(name="Aliansy" , value="clear")
  await ctx.send(embed=em01)

@help.command()
async def botinfo(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy botinfo",description="Pokazuje informacje o bocie")
  em01.add_field(name="**Użycie**",value=".botinfo",inline=False)
  em01.add_field(name="Aliansy" , value="bi")
  await ctx.send(embed=em01)

@help.command()
async def userinfo(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy userinfo",description="Pokazuje informacje o użytkowniku")
  em01.add_field(name="**Użycie**",value=".userinfo <id/ping user>",inline=False)
  em01.add_field(name="Aliansy" , value="ui")
  await ctx.send(embed=em01)

@help.command()
async def serverinfo(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy serverinfo",description="Pokazuje informacje o serwerze")
  em01.add_field(name="**Użycie**",value=".serverinfo",inline=False)
  em01.add_field(name="Aliansy" , value="guild, guildinfo, si")
  await ctx.send(embed=em01)

@help.command()
async def createrole(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy createrole",description="Tworzy role")
  em01.add_field(name="**Użycie**",value=".createrole <reason>",inline=False)
  em01.add_field(name="Aliansy" , value="crerole ")
  await ctx.send(embed=em01)

@help.command()
async def deleterole(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy deleterole",description="Kasuje role")
  em01.add_field(name="**Użycie**",value=".deleterole <reason>",inline=False)
  em01.add_field(name="Aliansy" , value="delrole ")
  await ctx.send(embed=em01)

@help.command()
async def addrole(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy addrole",description="Daje role użytkownikowi")
  em01.add_field(name="**Użycie**",value=".addrole <id/ping user> <role_id>",inline=False)
  em01.add_field(name="Aliansy" , value="addrr, giverole")
  await ctx.send(embed=em01)

@help.command()
async def removerole(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy removerole",description="Odbiera role użytkownikowi")
  em01.add_field(name="**Użycie**",value=".removerole <id/ping user> <role_id>",inline=False)
  em01.add_field(name="Aliansy" , value="remover , takerole ")
  await ctx.send(embed=em01)

@help.command()
async def gstart(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy gstart",description="Tworzenie giveawayu")
  em01.add_field(name="**Użycie**",value=".gstart",inline=False)
  await ctx.send(embed=em01)

@help.command()
async def track(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy track",description="Sprawdzienie czy ktoś słucha spotify")
  em01.add_field(name="**Użycie**",value=".track",inline=False)
  await ctx.send(embed=em01)

@help.command()
async def lock(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy lock",description="Blokowanie kanału")
  em01.add_field(name="**Użycie**",value=".lock",inline=False)
  await ctx.send(embed=em01)

@help.command()
async def unlock(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy unlock",description="Odblokowanie kanałuy")
  em01.add_field(name="**Użycie**",value=".unlock",inline=False)
  await ctx.send(embed=em01)

@help.command()
async def setdelay(ctx):
  em01 = discord.Embed(title="Pomoc dot komendy setdelay",description="Ustawienie delay na kanał")
  em01.add_field(name="**Użycie**",value=".track",inline=False)
  await ctx.send(embed=em01)

@client.command()
async def modmail(ctx, *, message=None):
   author = ctx.author
   if message == None:
      return await ctx.reply('> Please type things to send this mail to the staff!')
   if isinstance(ctx.channel, discord.channel.DMChannel):
     channel = client.get_channel(916052253603934229)
     embed = discord.Embed(title=f"We found a new mail! 📧" ,description=f"**{message}**" ,color=0x8CFED8)
     embed.add_field(name="id",value=author.id)
     embed.set_thumbnail(url=f"{author.avatar_url}")
     await channel.send(embed=embed)
   else:
     return await ctx.reply("> Sorry but this command only works on my dm :)")

@client.command()
@commands.has_permissions(administrator=True) # Premission #
async def responde(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(f"**{ctx.message.author} Responded =>** {content}")


client.run("token")
