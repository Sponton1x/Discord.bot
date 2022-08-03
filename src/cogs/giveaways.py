import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
import random

class Giveaways(commands.Cog):
    def __init__(self, client):
        self.client = client

    def convert(self, time):
        pos = ["s","m","h","d"]

        time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def gstart(self, ctx):
        question1 = discord.Embed(title=  "<a:giveaway:797783000820875274> Giveaway Question #1", color = ctx.author.color)
        question1.add_field(name = "Question:", value = f"Which channel would you like this giveaway in? Mention it properly!")
        question1.add_field(name = "Channel Mention Example:", value =f"Mention a channel like {ctx.channel.mention}")
        question1.set_footer(text = "Don't fail the questions!")
        question1.set_thumbnail(url = ctx.author.avatar_url)
        
        question2 = discord.Embed(title=  "<a:giveaway:797783000820875274> Giveaway Question #2", color = ctx.author.color)
        question2.add_field(name = "Question:", value = f"How long would you like this giveaway to last? ")
        question2.add_field(name = "Time Example:", value =f"Mention your number first and then type a unit.\nUnits: (s|m|h|d)")
        question2.set_footer(text = "Don't fail the questions!")
        question2.set_thumbnail(url = ctx.author.avatar_url)

        question3 = discord.Embed(title=  "<a:giveaway:797783000820875274> Giveaway Question #3", color = ctx.author.color)
        question3.add_field(name = "Last Question:", value = f"What is the prize of this giveaway?")
        question3.set_footer(text = "Don't fail the questions!")
        question3.set_thumbnail(url = ctx.author.avatar_url)

        errorEmbed1 = discord.Embed(title = '<:fail:761292267360485378> Giveaway Failed', color = ctx.author.color)
        errorEmbed1.add_field(name = "Reason:", value = "You did not mention a channel properly")
        errorEmbed1.add_field(name = "Channel:", value = f"{ctx.channel.mention}")

        errorEmbed2 = discord.Embed(title = '<:fail:761292267360485378> Giveaway Failed', color = ctx.author.color)
        errorEmbed2.add_field(name = "Reason:", value = "You did not mention the time properly!")
        errorEmbed2.add_field(name = "Channel:", value = f"Write a number and then units (s|m|h|d)")

        timeDelay = discord.Embed(title = '<:fail:761292267360485378> Giveaway Failed', color = ctx.author.color)
        timeDelay.add_field(name = "Reason:", value = "You did not answer in time!")
        timeDelay.add_field(name = "Next Steps:", value = "Make sure you answer in 45 seconds")

        questions = [question1, question2, question3]
        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
            await ctx.send(embed = i)

            try:
                msg = await self.client.wait_for('message', timeout=45.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send(embed = timeDelay)
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.send(embed = errorEmbed1)
            return

        channel = self.client.get_channel(c_id)
        time = self.convert(answers[1])

        if time == -1:
            await ctx.send(embed = errorEmbed2)
            return
        elif time == -2:
            await ctx.send(f"The time must be an integer. Please enter an integer next time")
            return

        prize = answers[2]
        
        # send a message for the user to know the giveaway started!
        await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")
        # now send the embed in the channel!
        embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)
        embed.add_field(name = "Hosted by:", value = ctx.author.mention)
        embed.set_footer(text = f"Ends {answers[1]} from now!")
        my_msg = await channel.send(embed = embed)
        # and then add the reactions
        await my_msg.add_reaction("🎉")
        # sleep for the time!
        await asyncio.sleep(time)
        # and then fetch it back
        new_msg = await channel.fetch_message(my_msg.id)
        # get a list of users
        users = await new_msg.reactions[0].users().flatten()
        # make sure the bot doesn't win
        users.pop(users.index(self.client.user))
        # now have some checks
        if len(users) == 0:
            em = discord.Embed(title = '<:fail:761292267360485378> Giveaway Failed', color = ctx.author.color)
            em.add_field(name = "Reason:", value = "No one joined D:")
            em.add_field(name = "Next steps:", value = "Dont make a giveaway which you don't enter!")
            await channel.send(embed = em)
            return
        # simply picka random user
        winner = random.choice(users)
        # edit embed to show winner
        newembed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)
        newembed.add_field(name = "Hosted by:", value = ctx.author.mention)
        # now do winers gizmo
        newembed.add_field(name = "Winner", value = f"{winner.mention}")
        newembed.set_footer(text = f"Ends {answers[1]} from now!")
        await my_msg.edit(embed = newembed)
        await channel.send(f"Congratulations! {winner.mention} won {prize}!\nURL: {my_msg.jump_url}")

    @gstart.error
    async def gstart_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title = "<:fail:761292267360485378> Giveaway failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = "`Administrator Permission is missing!`")
            embed.add_field(name = "Ideal Solution:", value = "Get the perms, lmao!")
            embed.set_footer(text = 'Bot Made by NightZan999#0194')
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command(aliases=['greroll'])
    @has_permissions(manage_guild = True)
    async def reroll(self,ctx, channel : discord.TextChannel, id_ : int):
        try:
            new_msg = await channel.fetch_message(id_)
        except:
            await ctx.send("The id was entered incorrectly.\nNext time mention a channel and then the id!")
            return

        if new_msg.author != self.client.user:
            em = discord.Embed(title=  '<:fail:761292267360485378> Reroll Failed', color = ctx.author.color, description = f"<:fail:761292267360485378> This message ([Jump URL]({new_msg.jump_url})) is not a giveaway hosted by the empire!")
            em.add_field(name = "Reason:", value = "The message you tried to reroll isn't a giveaway hosted by me")
            em.add_field(name ="How to reroll then?", value = "Take the ID of a message that is hosted by me, not some other bots!")
            return await ctx.send(embed = em)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)
        await channel.send(f"Congratulations! The new winner is {winner.mention}!")
        try:
            await channel.send(f"URL: {new_msg.jump_url}")
        except:
            pass

    @reroll.error
    async def reroll_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title = "<:fail:761292267360485378> Reroll failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = "`Manage Server is missing!`")
            embed.add_field(name = "Ideal Solution:", value = "Get the perms, lmao!")
            embed.set_footer(text='Bot Made by NightZan999#0194')
            await ctx.send(embed = embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title = "<:fail:761292267360485378> Reroll failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = "`You entered the ID or Channel wrongly!`")
            embed.add_field(name = "Usage:", value = '```diff\n+ imp reroll #giveaways <messageId> moderator won giveaway\n- imp reroll <messageID>\n```')
            embed.set_footer(text='Bot Made by NightZan999#0194')
            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Giveaways(client))