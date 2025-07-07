import asyncio
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from datetime import datetime
from discord.ext import commands, tasks
import datetime
import pytz

india = pytz.timezone("Asia/Kolkata")

SERVERID = 898241953559359529
CHANNELID = 898241954234650677
"""
#setting up the discord dev account !!
# sign in or sign up for the account"""

CLOUD :str = "AWS"
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
print(f"Token loaded: {token is not None}") #personall checks


handler = logging.FileHandler(filename='discord.log', encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents = intents )



"""
automated message def based on the time of the day
"""
@tasks.loop(minutes=1)
async def daily_message():
    now = datetime.datetime.now(india)
    channel = bot.get_channel(CHANNELID)  # channel ID
    if now.hour == 14 and now.minute == 21:  # time military
        print("got the id")
        try :
            await channel.send("☀️ afternoon, warriors! ")
        except Exception as e:
            print(e, "is the issue")
    elif now.hour == 9 and now.minute == 00:
        print(f"ID-time {now.hour}")
        try :
            await channel.send("☀️ Morning, warriors! ")
        except Exception as e:
            print(e, "is the issue")
    else : pass

@bot.event
async def on_ready():
    print(f" ✅ Wake the fuck up, samurai. We got a city to burn — {bot.user.name}")
    daily_message.start()  #  task loop starts here


# @bot.event  remove this
# async def on_ready():
#     print(f"✅ Bot is online as {bot.user}")
#     daily_message.start()  # ✅ Start the task loop here

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the arena, warrior: {member.name}")

@bot.event
async def on_message(message):
    try:
        if message.author == bot.user:
            return
        msg = message.content.lower()
        SWEAR_WORDS = ['shit', 'fuck', 'gay', 'slut', 'dick', 'pussy', 'lanja', 'modda', 'puka']
        if any(word in msg for word in SWEAR_WORDS):
            await message.delete()
            await message.channel.send(f"{message.author.mention} bitch don't use bad words! >> ")
    except Exception as e:
        print(f"Error in on_message: {e}")
    finally:
        await bot.process_commands(message)


@bot.command
async def hello(ctx):
    await ctx.send(f"Hey {ctx.author.mention} Darling!!")

@bot.command()
async def spec(ctx):
    await ctx.send(f"  {CLOUD } all rights reserved @2025  ")

@bot.command()
async def everyone(ctx):
    await ctx.send(f"@everyone everyone listen up this bitch {ctx.author.mention} has something to say! ")
@bot.command()
async def onlinewho(ctx):
    await ctx.send(f" @here all online folks need your attention on this : ")

@bot.command()
async def listcommands(ctx):
    await ctx.send(" \n All \n The \n Commands \n as follows :")
# @bot.command()
# async def spec(ctx):
#     await ctx.send(f" > {CLOUD} <")
# @bot.command()
# async def spec(ctx):
#     await ctx.send(f" > {CLOUD} <")
# @bot.command()
# async def spec(ctx):
#     await ctx.send(f" > {CLOUD} <")
# @bot.command()
# async def spec(ctx):
#     await ctx.send(f" > {CLOUD} <")
# @bot.command()
# async def spec(ctx):
#     await ctx.send(f" > {CLOUD} <")
# @bot.command()
# async def spec(ctx):
#     await ctx.send(f" > {CLOUD} <")
# @bot.command()
# async def spec(ctx):
#     await ctx.send(f" > {CLOUD} <")



@bot.command
async def checkroutesingeltonship1(context):
    await context.send(f" all clear! {context.author.mention}!")



@bot.command()
async def whatsthetime(ctx):
    current_time = datetime.now().strftime("%I:%M %p")
    await ctx.send(f"Hey {ctx.author.mention}, the time is {current_time} ⏰")


bot.run(token, log_handler = handler, log_level= logging.DEBUG)
