import discord
import requests
from discord.ext import commands, tasks
import os
from itertools import cycle
from time import sleep

#made by cyclone#
#remove credits = no good "skid"
TOKEN='put discord token here!'
color=0xf4fefe

intents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=intents)

#status#
status = cycle(["Your discord chaning status","2nd one"])


@tasks.loop(seconds=10)
async def changeStatus():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))


@client.event
async def on_ready():
    print("Im ready!")
    changeStatus.start()


#hello command
@client.command()
async def hello(ctx):

    await ctx.send(f'Hello {ctx.author.mention}!')



@client.command()
async def lookup(ctx,requesterUserId):
    jsonreq=requests.get(f"https://users.roblox.com/v1/users/{requesterUserId}").json()
    embed = discord.Embed(title=f"Info", color=color)
    embed.add_field(name="NAME", value=jsonreq['name'], inline=False)
    embed.add_field(name="Display name", value=jsonreq['displayName'], inline=False)
    embed.add_field(name="About Me", value=jsonreq['description'], inline=False)
    embed.add_field(name="Account created", value=jsonreq['created'], inline=False)
    embed.add_field(name="Roblox ID", value=jsonreq['id'], inline=False)
    embed.add_field(name="Account Ban", value=jsonreq['isBanned'], inline=False)
    embed.set_footer(text="Made by cyclone")
    await ctx.send(embed=embed)
    return



@client.command()
async def followers(ctx, id):
    request=requests.get(f"https://friends.roblox.com/v1/users/{id}/followers/count").json()
    embed = discord.Embed(title=f"Followers count", color=color)
    embed.add_field(name="Amount of Followers", value=request['count'], inline=False)
    embed.set_footer(text="Made by cyclone")
    await ctx.send(embed=embed)
    return


@client.command()
async def declineall(ctx):
    request=requests.post(f"https://friends.roblox.com/v1/user/friend-requests/decline-all").json()
    embed = discord.Embed(title=f"Decline Friend Request", color=color)
    embed.add_field(name="SuccessFully Declined All Request", value="Check your friend request", inline=False)
    embed.set_footer(text="Made by cyclone")
    await ctx.send(embed=embed)
    return


###more commands soon!

client.run(TOKEN)
