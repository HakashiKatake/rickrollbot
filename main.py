import discord 
import asyncio
import os
import random
import time
import ffmpeg
from discord.ext import commands
from threading import Thread
from discord.ext.commands import Bot
from flask import Flask
from discord import User
from discord import Embed, Member
from keep_alive import keep_alive

bot = commands.Bot(command_prefix = ["r", "R"])

@bot.command(aliases=['Dmroll'])
async def dmroll(ctx, *,  member : discord.Member=None):
  await ctx.message.delete()

  embed = discord.Embed(title=f'{member.name} You just got rickrolled!', description="""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""")
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/874897094329114704/fb4c1cfde7339cb44d604d921f2c2b9a.webp?size=1024")
  embed.set_footer(text="Made by Hakashi Katake")
  await member.send(embed=embed, tts=True)
  
@bot.command()
async def gifroll(ctx, *, member : discord.Member):
  await member.send(f"you just got rickrolled boi https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983 ")


@bot.command()
async def vcroll(ctx):
  voicetrue = ctx.author.voice
  if voicetrue is None:
        return await ctx.send("You're not connected to a voice channel")
  voice = await ctx.author.voice.channel.connect()
  voice.play(discord.FFmpegPCMAudio('./mp3s/Rick_Astley.mp3'))
  counter = 0
  duration = 18   # In seconds
  while not counter >= duration:
    await asyncio.sleep(1)
    counter = counter + 1
  await voice.disconnect()


@bot.command()
async def ttsroll(ctx):
  await ctx.channel.send("""Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""", tts=True)




@bot.command()
async def invite(ctx):
    masked_link_embed = discord.Embed(
    title='Want to Rickroll your friends, family or a discord server?',
    description="Here invite me and RickRoll all of them. -> [Invite me]( https://discord.com/oauth2/authorize?client_id=874897094329114704&scope=bot&permissions=8052539255)",
    color=0x95a5a6,
    timestamp=ctx.message.created_at)
    masked_link_embed.add_field(name="Currently under development", value="You can support me by clicking this link. -> [click here to support me](http://hyperurl.co/customURLredirect)")
    masked_link_embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/874897094329114704/fb4c1cfde7339cb44d604d921f2c2b9a.webp?size=1024"),
    masked_link_embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"{ctx.author.name}")
    await ctx.send(embed=masked_link_embed)   

@bot.command()
async def nitro(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Someone Just Droped A Free Nitro!", description="Here your nitro link, claim it before someone else claims it. be quick! -  ||https://dis.cord.gifts/4WgE6BHNX8wQo7sy||", color=0xe91e63,timestamp=ctx.message.created_at)
  embed.set_thumbnail(url="https://d33wubrfki0l68.cloudfront.net/af917b75e7f1f34ad53088863e88d46cdd821d04/eaa84/assets/nitro.png")
  embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"{ctx.author.name}")
  await ctx.send(embed=embed)

  
@bot.command()
async def vbucks(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Someone Just Droped Free V-BUCKS!", description="Here your v-bucks link, claim it sign into your epic games account and get the free v-bucks. be quick! -  ||<https://www.tomorrowtides.com/free-v-bucks36.html>||", color=0xe91e63,timestamp=ctx.message.created_at)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866875447580819477/874992684576686130/fortn.png")
  embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"{ctx.author.name}")
  await ctx.send(embed=embed)  





@bot.command()
async def howtoroll(ctx):
  embed = discord.Embed(title="Want to create your own RickRoll?",description="[Click here to make your own RickRoll](https://www.wikihow-fun.com/Rick-Roll-Someone) and yes it's not a rickroll, you can trust me on this one.", timestamp=ctx.message.created_at)
  embed.add_field(name="Want to rickroll your server members?", value="[click here to invite me](https://discord.com/oauth2/authorize?client_id=874897094329114704&scope=bot&permissions=8052539255)")
  embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/874897094329114704/fb4c1cfde7339cb44d604d921f2c2b9a.webp?size=1024")
  embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"{ctx.author.name}")

  await ctx.send(embed=embed)








@bot.event
async def on_ready():
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'And RickRolling {servers} servers and {members} members'
    ))



DISCORD_TOKEN = os.getenv("bot_token")
intents = discord.Intents.all()

keep_alive()
token = os.environ.get("bot_token")
bot.run(token)

