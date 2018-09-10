'''
Created on Apr 16, 2018

@author: Tiln
'''
# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import math
import random
import re
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os.path
from googlesearch import search
import platform
import json
from operator import itemgetter

import discord
from discord.ext import commands
from discord.ext.commands import Bot

from EggIncBot.otherStuff import HelpMethods
from _ast import Await

import requests
import justext

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Tiln's Egg Inc EggInc", command_prefix="e!", pm_help = False)
client.remove_command('help')

hm = HelpMethods()
asc = ['', '', '', '', '', '', '', '', '    ', '', '', '\n', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', "`", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ' ', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '­', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ' ]
emojAN = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿', '0⃣', '1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣']
#:hash: :exclamation: :question: :ab: :cl: :id: :ng: :ok: :vs: :wc: :bangbang: :interrobang: :new: :sos: :cool: :free: :10: :heavy_plus_sign: :heavy_minus_sign: :heavy_multiplication_x: :heavy_division_sign: :heavy_dollar_sign:
emojmisc = ['🔥', '❗', '❓', '🆎', '🆑', '🆔', '🆖', '🆗', '🆚', '🚾', '‼', '⁉', '🆕', '🆘', '🆒', '🆓', '🔟', '➕', '➖', '✖', '➗', '💲']
#:a: :b: :information_source: :m: :o2: :o: :parking: :negative_squared_cross_mark: :x: :grey_exclamation: :grey_question:
emojdup = ['🅰', '🅱', 'ℹ', 'Ⓜ', '🅾', '⭕', '🅿', '❎', '❌', '❕', '❔']
roles = []
# TUSMb = "​\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n​"

# This is what happens everytime the bot launches. In this case, it prints information like guild count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+str(client.user.id)+') | Connected to '+str(len(client.guilds))+' guilds | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=402730000'.format(client.user.id))
    print('--------')
    return await client.change_presence(activity=discord.Game(name="Egg inc's glitchiness | e!help")) #This is buggy, let us know if it doesn't work.


@client.event
async def on_message(message):
    if not message.guild:
        await client.process_commands(message)
        return
    
    global roles
    if not roles:
        roles = sorted(message.guild.roles, key=lambda x: x.position, reverse=False)
    
    updater = discord.utils.get(roles, name='Updater')
    for x in message.content.split("\n"):
        if x.startswith("e!"):
            command=x.lower().split(" ")[0]
            for y in range(10, -1, -1):
                x = x.replace(" "*(2**y+1), " ")
            message.content=command+x[len(command):]
            await client.process_commands(message)
#     elif str(message.channel) == "role_submissions":
#         imagext = message.content.split(".")[-1]
#         if message.attachments:
#             await hm.images(message.attachments[0].get('url'), message, client)
#         elif imagext == "png" or imagext == "jpg" or imagext == "jpeg":
#             await hm.images(message.content, message, client)    
    if (message.channel.permissions_for(message.author).manage_roles or updater in message.author.roles) and not message.content.startswith("e!"):
        if (message.channel.name == "leaderboard-submissions" or message.channel.name == "bot"):
            com = message.content.split("\n")
            user = ""
            for x in com:
                if "#" in x:
                    user = x.strip()
                elif "," in x and user:
                    if len(x) == 5:
                        await hm.updatelb("oom.txt", user, x, client, await client.get_channel(455385893537185806).get_message(457715280152363018))
                        hm.updatetoEOTW(message.author)
                    elif len(x) < 10:
                        await hm.updatelb("drones.txt", user, x, client, await client.get_channel(455385893537185806).get_message(457715344367288331))
                        hm.updatetoEOTW(message.author)
                    elif len(x) > 14:
                        await hm.updatelb("souleggs.txt", user, x, client, await client.get_channel(455385893537185806).get_message(457715345546018828))
                        hm.updatetoEOTW(message.author)
                elif user:
                    await hm.updatelb("prestiges.txt", user, x, client, await client.get_channel(455385893537185806).get_message(457715346615566338))
                    hm.updatetoEOTW(message.author)
        elif str(message.channel) == "role-submissions" and (message.content.startswith("+") or message.content.startswith("-")):
            time = message.created_at
            pref = message.content[0]
            eggs = discord.utils.get(roles, name="Eggs")
            offset = eggs.position
            cmc = message.content.split(" ")
            
            num = int(cmc[0][1:])
            if num > 28:
                num = 3*(int(cmc[0][1])) + int(cmc[0][2]) - 2
            muid = 0
            if len(cmc) > 1:
                if cmc[1].isdigit():
                    if int(cmc[1]) > 1000000000:
                        muid = cmc[1]
            if not muid:
                mes = 0
                async for x in message.channel.history():
                    p = re.compile("https?:\\/\\/.+\\.(?:png|jpg|jpeg)")
                    if x.attachments or p.match(x.content):
                        mes = x
                        break
                if not mes:
                    return
            else:
                try:
                    mes = await message.channel.get_message(muid)
                except discord.errors.NotFound:
                    try:
                        memfrid = message.guild.get_member(muid)
                        print(memfrid.name)
                        found = False
                        async for x in message.channel.history():
                            p = re.compile("https?:\\/\\/.+\\.(?:png|jpg|jpeg)")
                            if x.author == memfrid and (x.attachments or p.match(x.content)):
                                mes = x
                                found=True
                                break
                        if not found:
                            print("Not found")
                            return
                    except discord.errors.NotFound:
                        await message.channel.send("Bad ID")
                        return
            auth = mes.author
            
            
            prev = eggs
            for x in range(offset, offset+31):
                if roles[x] in auth.roles:
                    prev = roles[x]
            if num > 28 + offset:
                await message.channel.send("Too far.")
                return
            if not num == 0:
                new = discord.utils.get(roles, position=(num+offset))
            else: new = prev
            start = str(message.author.name)
            if not new == prev:
                authroles = auth.roles
                authroles.remove(prev)
                authroles.append(new)
                await auth.edit(roles=authroles)
            else: num = 0
            await mes.delete()
                
            resptime = (time - mes.created_at).total_seconds()
            mid = " has determined that the submission by " + str(auth)
            altmid = " has determined that the submission by " + str(auth.mention)
            end = "\n"+start+" took approximately " + str(resptime) + " seconds to take care of " + mes.author.name + "'s submission."
            new = new.name
            prev = prev.name
            if num == 0 and pref == "+":
                await message.channel.send(start + mid + " does not increase their role("+new+")." + end)
                await client.get_channel(455486044490694696).send(start + altmid + " does not increase their role("+new+")." + end)
            elif pref == "+":
                await message.channel.send(start + " has approved the submission by " + str(auth.name) + " which increased their role from " + prev + " to " + new + "." + end)
                await client.get_channel(455486044490694696).send(start + " has approved the submission by " + str(auth.mention) + " which increased their role from " + prev + " to " + new + "." + end)
            elif num == 0 and pref == "-":
                await message.channel.send(start + mid + " is unreadable("+new+")." + end)
                await client.get_channel(455486044490694696).send(start + altmid + " is unreadable("+new+")." + end)
            elif pref == "-":
                await message.channel.send(start + mid + " decreases their role from " + prev + " to " + new +"." + end)
                await client.get_channel(455486044490694696).send(start + altmid + " decreases their role from " + prev + " to " + new +"." + end)
            await message.delete()
            hm.updatetoEOTW(message.author)
    else:
        m = message.content.lower()
        if ((len(message.content) == 1 and message.content in asc) or m.endswith("no u") or "no u*" in m or "no u " in m or "triple gay" in m):
            await message.delete()
#         elif "egg" in m and (str(message.author) == "DiamondSphinx#0818" or str(message.author) == "⎝▂▃▅▆▇█╠RHEEEEEEEEEEEEEE╣█▇▆▅▃▂⎠#4668" or str(message.author) == "ƝØ#6436"):
#             await client.add_reaction(message, "🥚")
    


@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.message.channel) == "role_submissions":
        start = str(user.name)
        r = reaction.emoji
        mid = " has determined that the submission by " + str(reaction.message.author.name) + "#" + str(reaction.message.author.discriminator)
        altmid = " has determined that the submission by " + str(reaction.message.author.mention)
        role = str(hm.get_farmer_role(roles, reaction.message))
        if str(r) == "👍":
            await reaction.message.channel.send(reaction.message.channel, start + " has approved the submission by " + str(reaction.message.author.name) + "#" + str(reaction.message.author.discriminator) + " which increased their role to " + role + ".")
            await reaction.message.channel.send(client.get_channel(446871052434276352), start + " has approved the submission by " + str(reaction.message.author.mention) + " which increased their role to " + role + ".")
            await reaction.message.delete()
        elif str(r) == "👎":
            await reaction.message.channel.send(reaction.message.channel,  start + mid + " does not increase their role("+role+").")
            await reaction.message.channel.send(client.get_channel(446871052434276352),  start + altmid + " does not increase their role("+role+").")
            await reaction.message.delete()
        elif str(r) == "⬇":
            await reaction.message.channel.send(reaction.message.channel, start + mid + " decreases their role to " + role)
            await reaction.message.channel.send(client.get_channel(446871052434276352), start + altmid + " decreases their role to " + role)
            await reaction.message.delete()
        elif str(r) == "🤦" or str(r) == "🤷":
            await reaction.message.channel.send(reaction.message.channel, start + mid + " is unreadable("+role+").")
            await reaction.message.channel.send(client.get_channel(446871052434276352), start + altmid + " is unreadable("+role+").")
            await reaction.message.delete()
    elif str(reaction.message.channel) == "events":
        await user.add_roles(discord.utils.get(roles, name="Events"))


@client.event
async def on_member_join(member):
    Eggs = discord.utils.get(member.guild.roles, name="Eggs")
    await member.add_roles(Eggs)


@client.command(pass_context=True)
async def ping(ctx):
    if not str(ctx.message.author) == "Tiln#0416":
        msg = await ctx.channel.send("Pong!")
        time = math.trunc((msg.timestamp - ctx.message.timestamp).total_seconds() * 1000)
        await msg.edit(content="Pong! `" + str(time) + " ms`")
    elif str(ctx.message.author) == "Tiln#0416":
        
        #await ctx.channel.send("```/*Base Format*/\n01 Bob#0000\n   0\n```")
#       twhr = ["🇹", "🇮", "🇱", "🇳", "🇼", "🇦", "🇸", "🇭", "🇪", "🇷", "3⃣", discord.utils.get(client.get_all_emojis(), name="tiln")]
#       for x in twhr:
#           await client.add_reaction(test, x)
#       logs = yield from client.logs_from(ctx.channel)        
            
        farmroles = []
        eb = []
        
        farmers = hm.farmers_l(roles)
        ml = ctx.guild.members
        larnum = 0
        total = 0
        acf = []
        torev = []
        orderednums = []
        farmernum = 27
        for f in reversed(farmers):
            num = 0
            for m in ml:
                if f in m.roles and m not in acf:
                    num += 1
                    acf.append(m)
            if num:
                torev.append(str(f) + " "*(16-len(str(f))) + str(num))
                farmroles.append(str(f).replace("farmer", ""))
                eb.append(num)
                orderednums.append(farmernum)
                if num > larnum:
                    larnum = num
            total += num
            farmernum -= 1
        s = "```"
        torev = reversed(torev)
        for x in torev:
            s += x + "\n"
        s += "Total: " + str(total) + "```"
        
        
        
        egg = discord.utils.get(roles, name="Eggs")
        chicken = discord.utils.get(roles, name="Chickens")
        gig3 = discord.utils.get(roles, name="Gigafarmer III")
#         for m in ml:
#             for f in farmers:
#                 if egg in m.roles and f in m.roles:
#                     await client.remove_roles(m, egg)
#                     print(m)

        num2 = 0
        for m in ml:
            if egg not in m.roles and chicken not in m.roles:
                gonnaadd = True
                for f in farmers:
                    if f in m.roles:
                        gonnaadd = False
                if gonnaadd and not m.bot:
                    await m.add_roles(egg)
                    num2+=1
                    print(num2)
            for f in farmers:
                if f in m.roles and (egg in m.roles or chicken in m.roles):
                    await m.remove_roles([egg, chicken])
                    num2+=1
                    print(num2)
                    break
            for f in farmers[12:15]:
                if discord.utils.get(roles, name=f) in m.roles and gig3 not in m.roles:
                    await m.add_roles(gig3)
        await ctx.message.delete()
#         emoj = "#⃣ 🆎 🆑 🆔 🆖 🆗 🆘 🆚 🚾 ❗ ‼ ❓ ⁉ 🆒 🆕 🆓".split(" ")
#         st = ""
#         for x in emoj:
#             st += "'"+x+"', "
#         print(st)
        
#         async for x in client.logs_from(client.get_channel(430497503469633536)):
#             if x.attachments:
#                 await hm.images(x.attachments[0].get('url'), client)
        
#     if ctx.message.mentions:
#         print(ctx.message.mentions[0])
    
    #await client.http.edit_message(message_id, channel_id, content)
    
    
@client.command(pass_context=True)
async def help(ctx):
    com = ctx.message.content.lower().split(" ")
    base = False
    s = ""
    if len(com)>1:
        c = com[1]
        if c == "calc" or c == "Calc":
            await ctx.channel.send("```e!"+c+" <Soul Eggs> <Prophecy Eggs> <Soul Food Research Level> <Prophecy Bonus Research Level>\nor\ne!"+c+" <Soul Eggs> <Prophecy Eggs>\n<> Means optional (yes that does mean everything is optional)```")
        elif c == "ulb":
            await ctx.channel.send("```e!"+c+" leaderboard Member(ascii characters only) score```")
        elif c == "contract":
            await ctx.channel.send("```e!"+c+" [egg laying rate(stats)] [internal hatchery rate(stats)] [time left in contract(contract page)] [farm population(stats)] <your current eggs produced(contract top layers)>(or 0) <internal hatchery calm upgrades>(or 20) <maximum hab capacity>(or 189*10^7) <maximum shipping rate>(or 311462*10^6*17)\n<> means optional\nExample: e!contract 316.804b 6440 12d11h10m35s 168m 342t 20 1.89b 5.295t```")
        elif c == "nick":
            await ctx.channel.send("e!"+c+" nick")
        else: await ctx.channel.send("e!"+c+" is not currently a command.")
    else: base = True
    if base:
        updater = discord.utils.get(roles, name='Updater')
        s += "```e!help Displays this command\ne!calc calculates earnings bonus\ne!contract calculates how well you are doing for your contract\n"
        if ctx.channel.permissions_for(ctx.message.author).manage_roles or updater in ctx.message.author.roles:
            s += "e!ulb updates the specified leaderboard\n"
        s += "e!help [command] for help on that command```"
        await ctx.channel.send(s)
   

@client.command(pass_context=True)
async def calc(ctx):
    farmers = hm.farmers_l(roles)
    cmcs = ctx.message.content.split(" ")
    if len(cmcs) == 1:
        ctx.message.content = "e!help calc"
        await client.process_commands(ctx.message)
        return
    amnt = len(cmcs) - 1
    if amnt > 0:
        SE = int(cmcs[1].replace(",", ""))
    else: SE = 1
    if amnt > 1:
        PE = int(cmcs[2].replace(",", ""))
    else: PE = 0
    threemen = False
    if ctx.message.mentions and amnt == 3:
        threemen = True
        
    sto = ""
    if PE > 5000:
        sto += "Infinifarmer"
        await ctx.channel.send(sto + "\nEarnings bonus: Too dang high")
    else:
        if amnt > 2 and not threemen:
            SERL = int(cmcs[3])
        else: SERL = 140
        if amnt > 3 and not threemen:
            PERL = int(cmcs[4])
        else: PERL = 5
        SE = abs(SE) % (2**64)
        PE = abs(PE)
        if SERL > 140 or SERL < 0: SERL = 140
        if PERL > 5 or PERL < 0: PERL = 5
        BPE = round((.1 + SERL*.01) * (1.05 + PERL*.01)**PE, 6)
        num = round(BPE * SE, 2)
        le = math.trunc(math.log10(num) + 1 or 1)
        st = hm.get_pref(le)
        SEneed = math.ceil(10**(le) // (1.05 + PERL*.01)**PE // (.1 + SERL*.01))
        if not st:
            sto += "Infinifarmer"
        else: 
            if ((le - 1)%3 + 1 == 1):
                sto += st + "armer"
            elif ((le - 1)%3 + 1 == 2):
                sto += st + "armer II"
            elif ((le - 1)%3 + 1 == 3):
                sto += st + "armer III"
        role = discord.utils.get(roles, name=sto)
        sto += "\nEarnings bonus: " + str("{:,}".format(num)) + "\nBonus per soul egg: " + str(BPE) + "\nTotal SE needed for next rank: " + str("{:,}".format(SEneed))
        await ctx.channel.send(sto)
    if amnt > 4 or threemen:
        rta = []
        rta.append(role)
        await hm.updateroles(ctx, rta, farmers, client)
        
        
@client.command(pass_context=True)
async def contract(ctx):
    #egg laying rate, internal hatchery rate, time left, current chickens, your eggs laid, internal hatchery calm
    cmc = ctx.message.content.lower().replace(",", "")
    for x in range(11, -1, -1):
        cmc = cmc.replace(" "*(2**x+1), " ")
    cmc = cmc.split(" ")[1:]
    if len(cmc) == 0:
        ctx.message.content = "e!help contract"
        await client.process_commands(ctx.message)
        return
    
    mil = 10**6
    bil = 10**9
    tril = 10**12
    quad = 10**15
    quint = 10**18
    try:
        if cmc[0][-1] == "m":
            elr = math.trunc(float(cmc[0][:-1])/60*mil)
        elif cmc[0][-1] == "b":
            elr = math.trunc(float(cmc[0][:-1])/60*bil)
        elif cmc[0][-1] == "t":
            elr = math.trunc(float(cmc[0][:-1])/60*tril)
        else: elr = int(cmc[0])//60
        ihr = int(cmc[1])//60
        
        tl = 0
        for x in range(len(cmc[2])):
            if cmc[2][x] == "d":
                tl += int(cmc[2][:x])*24*3600
                cmc[2] = cmc[2][(x+1):]
                break
        for x in range(len(cmc[2])):
            if cmc[2][x] == "h":
                tl += int(cmc[2][:x])*3600
                cmc[2] = cmc[2][(x+1):]
                break
        for x in range(len(cmc[2])):
            if cmc[2][x] == "m":
                tl += int(cmc[2][:x])*60
                cmc[2] = cmc[2][(x+1):]
                break
        tl += int(cmc[2].replace("s", "") or 0)
        
        if cmc[3][-1] == "k":
            cc = math.trunc(float(cmc[3][:-1])*1000)
        elif cmc[3][-1] == "m":
            cc = math.trunc(float(cmc[3][:-1])*mil)
        elif cmc[3][-1] == "b":
            cc = math.trunc(float(cmc[3][:-1])*bil)
        else: cc = int(cmc[3])
        
        el = 0
        if len(cmc) > 4:
            if cmc[4][-1] == "k":
                el = math.trunc(float(cmc[4][:-1])*1000)
            elif cmc[4][-1] == "m":
                el = math.trunc(float(cmc[4][:-1])*mil)
            elif cmc[4][-1] == "b":
                el = math.trunc(float(cmc[4][:-1])*bil)
            elif cmc[4][-1] == "t":
                el = math.trunc(float(cmc[4][:-1])*tril)
            elif cmc[4][-1] == "q":
                el = math.trunc(float(cmc[4][:-1])*quad)
            else: el = int(cmc[4])
        
        if len(cmc) > 5:
            ihc = int(cmc[5])
        else: ihc = 20
        if ihc > 20 or ihc < 0:
            ihc = 20
            
        maxh = 189*10**7
        if len(cmc) > 6:
            if cmc[6][-1] == "m":
                maxh = math.trunc(float(cmc[6][:-1])*mil)
            elif cmc[6][-1] == "b":
                maxh = math.trunc(float(cmc[6][:-1])*bil)
            else: maxh = int(cmc[6])
            
        maxsr = 311462*10**6*17
        if len(cmc) > 7:
            if cmc[7][-1] == "m":
                maxsr = math.trunc(float(cmc[7][:-1])*mil)
            elif cmc[7][-1] == "b":
                maxsr = math.trunc(float(cmc[7][:-1])*bil)
            elif cmc[7][-1] == "t":
                maxsr = math.trunc(float(cmc[7][:-1])*tril)
            else: maxsr = math.trunc(float(cmc[7]))
        
    except IndexError:
        await ctx.channel.send("Too few arguments.")  
        return
    except ValueError:
        await ctx.channel.send("Wrong number formatting.")   
        return
        
    elrpc = elr / cc
    if tl > 2*30*24*3600:
        return
    for _11 in range(tl):
        if cc > maxh:
            cc = maxh
        if cc*elrpc > maxsr:
            el += maxsr
        else: el += cc*elrpc
        cc += ihr*4*(ihc/10+1)
    
    fel = ""
    if el > quint:
        fel = str("{:.3f}".format(el/quint)) + "Q"
    elif el > quad:
        fel = str("{:.3f}".format(el/quad)) + "q"
    elif el > tril:
        fel = str("{:.3f}".format(el/tril)) + "T"
    elif el > bil:
        fel = str("{:.3f}".format(el/bil)) + "B"
    elif el > mil:
        fel = str("{:.3f}".format(el/mil)) + "M"
    await ctx.channel.send("You will have produced approximately " + fel + " eggs by the time the given time period ends.")
    


@client.command(pass_context=True)
async def ulb(ctx):
    updater = discord.utils.get(roles, name='Updater')
    com = ctx.message.content.split(" ")
    if ctx.channel.permissions_for(ctx.message.author).manage_roles or updater in ctx.message.author.roles:
        if len(com) == 4:
            s = ""
            if com[1] == "prestiges":
                await hm.updatelb("prestiges.txt", com[2], com[3], 457715280152363018, client, ctx.message)
            elif com[1] == "oom":
                await hm.updatelb("oom.txt", com[2], com[3], 457715344367288331, client, ctx.message)
            elif com[1] == "se":
                await hm.updatelb("souleggs.txt", com[2], com[3], 457715345546018828, client, ctx.message)
            elif com[1] == "drones":
                await hm.updatelb("drones.txt", com[2], com[3], 457715346615566338, client, ctx.message)
            else: s += "Invalid category"
#             ackr = ["🇦", "🇨", "🇰", "🇳", "🇴", "🇼", "🇱", "🇪", "🇩", "🇬", "🇮", "🆖"]
            invr = ["🇮", "🇳", "🇻", "🇦", "🇱", 'ℹ', "🇩", "🚫", "🇨", "🅰", "🇹", "🇪", "🇬", "🇴", "🇷", "🇾"]
            if s: 
                for x in invr:
                    await ctx.message.add_reaction(x)
#             else:
#                 for x in ackr:
#                     await ctx.message.add_reaction(x)
        else: await ctx.channel.send("Please format it as " + com[0] + " category member score")
    else: await ctx.channel.send("You don't have permission to use that command :sweat_smile: ")


@client.command(pass_context = True)
async def nick(ctx):
    s = ctx.message.content.split(" ", 1)[1]
    for x in s:
        if x not in asc:
            s = s.replace(x, "")
    if len(s) < 1: return
    await ctx.message.author.edit(nick=s)
#     if s == "Tiln":
#         await client.add_roles(ctx.message.author, discord.utils.get(roles, name="Tiln"))
#     else:
#         await client.remove_roles(ctx.message.author, discord.utils.get(roles, name="Tiln"))
    await ctx.message.delete()


@client.command(pass_context = True)
async def role(ctx):
    eb = ctx.message.content.split(" ")[1].replace(",", "")
    farmers = hm.farmers_l(roles)
    if eb.endswith("%"):
        eb = eb[:-3]
    await ctx.channel.send(farmers[len(eb)-1])
    

@client.command(pass_context = True)
async def killbot(ctx):
    if str(ctx.message.author) == "Tiln#0416":
        await ctx.message.delete()
        await client.logout()


@client.command(pass_context = True)
async def getlbs(ctx):
    updater = discord.utils.get(roles, name='Updater')
    if ctx.channel.permissions_for(ctx.message.author).manage_roles or updater in ctx.message.author.roles:
        await hm.getleaderboards(client, discord.utils.get(ctx.guild.channels, id=455385893537185806))


@client.command(pass_context = True)
async def wiki(ctx):
    response = search(ctx.message.content.split(" ", 1)[1] + " site:http://egg-inc.wikia.com")
    s = ""
    for x in response:
        s += "<" + x + ">\n"
        resp = requests.get(x)
        paragraphs = justext.justext(resp.content, justext.get_stoplist("English"))
        for y in paragraphs:
            if len(y.text) > 50:
                s += y.text
                break
        break
    await ctx.channel.send(s)

@client.command(pass_context = True)
async def getupdaterlb(ctx):
    file = open('updaters.json', 'r+')
    updaters = json.load(file)
    s = "```"
    for k, v in sorted(updaters.items(), key = itemgetter(1), reverse = True):
        s += k + ": " + str(v) + "\n"
    await ctx.channel.send(s + "```")
    
@client.command(pass_context = True)
async def graph(ctx):
    farmroles = []
    eb = []
    
    farmers = []
    farmers.append(discord.utils.get(roles, name="Eggs"))
    for x in hm.farmers_l(roles):
        farmers.append(x)
    ml = ctx.guild.members
    larnum = 0
    total = 0
    acf = []
    torev = []
    orderednums = []
    farmernum = 28
    for f in reversed(farmers):
        num = 0
        for m in ml:
            if f in m.roles and m not in acf:
                num += 1
                acf.append(m)
        if num:
            torev.append(str(f) + " "*(16-len(str(f))) + str(num))
            farmroles.append(str(f).replace("farmer", ""))
            eb.append(num)
            orderednums.append(farmernum)
            if num > larnum and farmernum > 1:
                larnum = num
        total += num
        farmernum -= 1
    s = "```"
    torev = reversed(torev)
    for x in torev:
        s += x + "\n"
    s += "Total: " + str(total) + "```"
    orderednums = list(reversed(orderednums))
    eb = list(reversed(eb))
    if eb[0] > larnum: eb[0] = larnum
    farmroles = list(reversed(farmroles))
    
    #plt.subplots()
    #ax.yaxis.set_major_formatter(formatter)
    fig = plt.figure()
    bars = plt.bar(orderednums, eb)
    prop = fm.FontProperties(fname='portlligatslab-regular.ttf')
    plt.xticks(orderednums, farmroles, rotation=45, va='baseline', ha='right', fontsize=9, fontproperties=prop)
    plt.yticks(np.arange(-1, larnum+larnum//25, step=larnum//25), fontsize=9, fontproperties=prop)
    colors = ["#bfbfbf", "#ffa64d", "#ff7f00", "#b35900", "#ffff00", "#b3b300", "#666600", "#4dff4d", "#00ff00", "#00b300", "#00ffff", "#00b3b3", "#006666", "#9999ff", "#4d4dff", "#007fff", "#ce98e7", "#b361da", "#9c30cf", "#ff00f0", "#c300b0", "#9f0090"]
    for x in range(len(eb)):
        bars[x].set_color(colors[x])        
    fig.savefig("graph.png")
    await ctx.channel.send(file=discord.File("graph.png"), content=s)

file = open(os.path.dirname(__file__) + "/../eitok.txt")
client.run(file.readline())
file.close



