#!/bin/python3

# This file will contain the functions which include :
# 1. Extracting message from discord and returning their strings
# 2. Mapping unicode characters with certain commonly used commands like starting a listening port, executing a brute force attack
# 3. Returning the Output with the original command
# 4. Downloading images and gifs and calculating their md5sum followed by mapping them to specific commands like (2)
# 5. More
#
# Note :
# Call all Functions using threads (Use Low Level Threading Like : start_new_thread)
# Store all downloaded media in /tmp       
# Use Asyncio ?


import discord
#import requests
#import json
#import random
from discord.ext import commands
import subprocess
#from decouple import config
import os
#import youtube_dl
#import time
import asyncio

'''
#try add this 
intents=discord.Intents.all()
#if the above don't work, try with this
#intents = discord.Intents.default()
#intents.members=True

client=discord.Client(intents=intents)
'''

ID=int(824362867657801779)

bot=commands.Bot(command_prefix="!")

def md5sum(a):
    os.chdir('/home/vader/Downloads/')
    
    args=f"md5sum {a}"
    #Shell=True means the args command is executed by using a shell. The stdout(output) and stderr(error) pipes are combined as per subprocess documentation
    process= subprocess.Popen(args,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output= process.stdout.read().decode()
    s=output.split(" ")
    return s[0]
    

#Bot activation message while logging in
@bot.event
async def on_ready():
     print("You have logged in as {0}".format(bot.user))
     channel=bot.get_channel(ID)
     await channel.send("Welcome back Mr.Anderson!")

    #We cannot trigger the bot.command instructions wihout writing this line in case of bot.event
     await bot.process_commands()

#A casual hello command for returning a pre-defined message
@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    else:
        if message.content.startswith("!hello"):
            await message.channel.send("Welcome to the matrix.")

        #Calculating the md5sum of any image sent to the server
        if message.content.startswith("!attach"):
            attachments=message.attachments
            attach=attachments[0].url
            await message.channel.send(attach)

            '''
            "Download attach in a specific folder and name the image as imageee.jpg."
            #await message.channel.send(file=discord.File('/path/to/imageee.jpg'))
            output2=md5sum(/path/to/imageee.jpg)
            if output2 in dictionary.keys():
                command=str(dictionary[output2])
                process2= subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                output3= process2.stdout.read().decode()
                
                await message.channel.send(output3)
            else:
                await message.channel.send("The md5sum is not present in the dictionary.")
        '''
    #We cannot trigger the bot commands wihout writing this line in case of bot.event
    await bot.process_commands(message)

#Taking any number of words as arguements and printing them
@bot.command()
async def print(ctx, *args):
    output=""
    for arg in args:
        output=output + " " + arg
    await ctx.channel.send(output)

'''
#Calculating the md5sum of any image sent to the server
@bot.command()
async def image(ctx, arg):
    "Download arg in a specific folder and name the image arg as imageee.jpg."
    output2=md5sum(imageee.jpg)

    if output2 in dictionary.keys():
        command=str(dictionary[output2])
        process2= subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output3= process2.stdout.read().decode()
        
        await ctx.channel.send(output3)
    else:
        await ctx.channel.send("The md5sum is not present in the dictionary.")
'''

bot.run("TOKEN")

