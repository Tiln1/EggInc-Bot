'''
Created on Apr 16, 2018

@author: Tiln
'''
import math
import re
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os.path
from googlesearch import search
import platform
import json
from operator import itemgetter
import sys
import time
import io
import traceback

import discord
from discord.ext import commands  # @UnusedImport @UnresolvedImport
from discord.ext.commands import Bot  # @UnresolvedImport

from otherStuff import HelpMethods  # @UnresolvedImport
import egginc as pb  # @UnresolvedImport

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
adchannels = [455385719301472286, 483361731330965504, 'farmers', 'gigafarmer', 'gigafarmer2', 'gigafarmer3', 'terafarmer', 'terafarmer2', 'terafarmer3', 'petafarmer', 563750232152604682, 563750717865852959, 'exafarmer', 578494692027662338]
coopchannels = ['bot-commands', 492045780392214529, 491847137684881408, 487881967149514772, 455549577668460575, 568175940866408448]
# TUSMb = "​\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\455512567004004353, 518322035349389334, 490500048283500544, n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n​"

# This is what happens everytime the bot launches. In this case, it prints information like guild count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+str(client.user.id)+') | Connected to '+str(len(client.guilds))+' guild | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=402730000'.format(client.user.id))
    print('--------')
    #await hm.loopIDtasks(client.get_guild(455380663013736479))
    return await client.change_presence(activity=discord.Game(name="with Egg Inc's glitchiness | e!help"))


@client.event
async def on_message(message):
    if not message.guild:
        await client.process_commands(message)
        return
    
    global roles
    if not roles:
        roles = sorted(message.guild.roles, key=lambda x: x.position, reverse=False)
    
    updater = discord.utils.get(roles, name='Updater')
#     elif str(message.channel) == "role_submissions":
#         imagext = message.content.split(".")[-1]
#         if message.attachments:
#             await hm.images(message.attachments[0].get('url'), message, client)
#         elif imagext == "png" or imagext == "jpg" or imagext == "jpeg":
#             await hm.images(message.content, message, client)
    
    if message.guild and (message.channel.permissions_for(message.author).manage_roles or updater in message.author.roles) and not message.content.startswith("e!") and not message.author.bot:
        if (message.channel.name == "leaderboard-submissions"):
            com = message.content.replace('\\n', '\n').split("\n")
            user = ""
            for x in com:
                if "#" in x:
                    user = x.strip()
                elif ',' not in x and not hm.int(x):
                    user = hm.getmember(message.guild, x)
                elif user:
                    await hm.strtolb(x, user, message.guild)
                    hm.updatetoEOTW(message.author)
        elif str(message.channel) == "role-submissions":
            time = message.created_at
            cmc = message.content.split(" ")
            
            muid = 0
            if not hm.int(cmc[0]) or len(cmc) > 2:
                firstdigs = ''
                length = ''
                pe = 0
                for x in cmc:
                    if not hm.int(x):
                        continue
                    if len(x) >= 2 and not firstdigs:
                        firstdigs = x
                    elif len(x) >= 2 and not length:
                        length = x
                    elif len(x) < 5 and not pe:
                        pe = int(x)
                    elif len(x) > 7 and not muid:
                        muid = int(x)
                if not firstdigs or not length or not pe:
                    return
                if int(length) < 30:
                    length = int(length)
                else:
                    length = 3*int(length[0]) + int(length[1])
                se = int(firstdigs + '0'*(length-len(firstdigs)))
                num = len(str(int(hm.earningsmult(se, pe))))
            else:
                for x in range(len(cmc)):
                    if len(cmc[x]) < 7:
                        try:
                            num = int(cmc[x])
                            strnum = cmc[x]
                        except:
                            try:
                                num = int(cmc[x][1:])
                                strnum = cmc[x][1:]
                            except:
                                return
                    else:
                        try:
                            muid = int(cmc[x])
                        except:
                            return
                 
                if num > 28:
                    num = 3*int(strnum[0]) + int(strnum[1]) - 2
            if not muid:
                mes = 0
                async for x in message.channel.history():
                    p = re.compile(r"https?:\/\/.+\.(?:png|jpg|jpeg)")
                    if x.attachments or p.match(x.content):
                        mes = x
                        break
                if not mes:
                    return
            else:
                try:
                    mes = await message.channel.fetch_message(muid)
                except discord.errors.NotFound:
                    try:
                        memfrid = await message.guild.fetch_member(muid)
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
            
            '''Finished processing input(ineffeciently I might add)'''
            
            auth = mes.author
            fields = await hm.updaterole(message.guild, auth, num)
            
            files = []
            if mes.attachments:
                ats = len(mes.attachments)
                for y in range(ats):
                    at = mes.attachments[y]
                    byts = requests.get(at.proxy_url).content
                    file = io.BytesIO(byts)
                    file.name = at.filename
                    files.append(discord.File(file))
            
            await mes.delete()
                
            start = str(message.author.name)
            resptime = (time - mes.created_at).total_seconds()
            mid = " has determined that the submission by " + str(auth)
            altmid = " has determined that the submission by " + str(auth.mention)
            end = "\n"+start+" took approximately " + str(resptime) + " seconds to take care of " + mes.author.name + "'s submission."
            prev = fields[1].name
            new = fields[2].name
            if num == 0:
                await message.channel.send(start + mid + " does not increase their role("+new+") due to the submission being unreadable." + end)
                await client.get_channel(455486044490694696).send(start + altmid + " does not increase their role("+new+") due to the submission being unreadable." + end, files=files)
            elif fields[0] == 0:
                await message.channel.send(start + mid + " does not increase their role("+new+") due to the submission being inadequate." + end)
                await client.get_channel(455486044490694696).send(start + altmid + " does not increase their role("+new+") due to the submission being inadequate." + end, files=files)
            elif fields[3] == "+":
                await message.channel.send(start + " has approved the submission by " + str(auth.name) + " which increased their role from " + prev + " to " + new + "." + end)
                await client.get_channel(455486044490694696).send(start + " has approved the submission by " + str(auth.mention) + " which increased their role from " + prev + " to " + new + "." + end, files=files)
            elif fields[3] == "-":
                await message.channel.send(start + mid + " decreases their role from " + prev + " to " + new +"." + end)
                await client.get_channel(455486044490694696).send(start + altmid + " decreases their role from " + prev + " to " + new +"." + end, files=files)
            await message.delete()
            hm.updatetoEOTW(message.author)
    elif not message.author.bot and not (message.channel.permissions_for(message.author).manage_roles or updater in message.author.roles):
        if str(message.channel) == "role-submissions":
            p = re.compile("https?:\\/\\/.+\\.(?:png|jpg|jpeg)")
            if not message.attachments and not p.match(message.content):
                await message.delete()
                return
        m = message.content.lower()
        if ((len(message.content) == 1 and message.content in asc) or m.endswith("no u") or "no u*" in m or "no u " in m or "triple gay" in m):
            try:
                await message.delete()
                return
            except: ""
                
    
    for x in message.content.split("\n"):
        if x.startswith("e!"):
            command=x.lower().split(" ")[0]
            for y in range(10, -1, -1):
                x = x.replace(" "*(2**y+1), " ")
            message.content=command+x[len(command):]
            await client.process_commands(message)
#         elif "egg" in m and (str(message.author) == "DiamondSphinx#0818" or str(message.author) == "⎝▂▃▅▆▇█╠RHEEEEEEEEEEEEEE╣█▇▆▅▃▂⎠#4668" or str(message.author) == "ƝØ#6436"):
#             await client.add_reaction(message, "🥚")
    


@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    chan = guild.get_channel(payload.channel_id)
    member = await guild.fetch_member(payload.user_id)
    message = await chan.fetch_message(payload.message_id)
    if str(chan) == "events":
        await member.add_roles(discord.utils.get(roles, name="Events"))


@client.event
async def on_member_join(member):
    Eggs = discord.utils.get(member.guild.roles, name="Eggs")
    await member.add_roles(Eggs)


@client.command(pass_context=True)
async def ping(ctx):
    if not str(ctx.message.author) == "Tiln#0416":
        msg = await ctx.send("Pong!")
        time = math.trunc((msg.timestamp - ctx.message.timestamp).total_seconds() * 1000)
        await msg.edit(content="Pong! `" + str(time) + " ms`")
    elif str(ctx.message.author) == "Tiln#0416":
        print(discord.ClientUser.premium)
#         prems = 0
#         for x in ctx.guild.members:
#             if x.premium:
#                 prems += 1
#         print(prems)
            
    
    
@client.command(pass_context=True)
async def help(ctx):
    com = ctx.message.content.lower().split(" ")
    base = False
    s = ""
    if len(com)>1:
        c = com[1]
        if c == "calc" or c == "Calc":
            await ctx.send(f"```e!{c} <Soul Eggs> <Prophecy Eggs> <Soul Food Research Level> <Prophecy Bonus Research Level>\nor\ne!{c} <Soul Eggs> <Prophecy Eggs>\n<> Means optional (yes that does mean everything is technically \"optional\"). Left out research is assumed maximum.```")
        elif c == "ulb":
            await ctx.send(f"```e!{c} leaderboard Member(ascii characters only) score```")
        elif c == "contract":
            await ctx.send(f"```e!{c} [egg laying rate(stats)] [internal hatchery rate(stats)] [time left in contract(contract page)] [farm population(stats)] <your current eggs produced(contract top layers)>(or 0) <internal hatchery calm upgrades>(or 20) <maximum hab capacity>(or 1134*10^7) <maximum shipping rate>(or 311462*10^6*17*10)\nWarning: Leaving out parameters may lead to inaccurate predictions\nExample: e!contract 316.804b 6440 12d11h10m35s 168m 342t 20 1.89b 5.295t```")
        elif c == "nick":
            await ctx.send(f"e!{c} nick")
        elif c == 'coop' or c == 'coopad':
            await ctx.send(f'e!{c} [co-op code] [co-op name]')
        elif c == 'completedcontracts':
            await ctx.send(f'```\ne!{c} [ID from in-game]\nExamples:\ne!{c} 117068751673085510666\ne!{c} G:11068551```')
        else: await ctx.send(f"e!{c} does not have a help if it is a command.")
    else: base = True
    if base:
        updater = discord.utils.get(roles, name='Updater')
        s += "```"
        s += "e!help Displays this command\n"
        s += "e!calc calculates earnings bonus\n"
        s += "e!contract calculates how well you are doing in your contract\n"
        s += "e!rank gives you the ranks of yourself or others among rankable things in the server.\n"
        s += "e!fullleaderboard\n"
        s += "e!nick\n"
        s += "e!wiki\n"
        s += "e!graph\n"
        s += "e!coopad\n"
        s += "e!currentcontractids; Aliases: cc\n"
        s += "e!completedcontracts ; Aliases: cc\n"
        s += "e!coop shows a co-op code's info\ne!coopad shows less of a co-op code's info\n"
        
        try:
            if ctx.channel.permissions_for(ctx.message.author).manage_roles or updater in ctx.message.author.roles:
                s += "e!ulb updates the specified leaderboard\n"
        except: ""
        s += "e!help [command] for help on that command```"
        await ctx.send(s)
   

@client.command(pass_context=True)
async def calc(ctx):
    farmers = hm.farmers_l(roles)
    cmcs = ctx.message.content.split(" ")
    if len(cmcs) == 1:
        ctx.message.content = "e!help calc"
        await client.process_commands(ctx.message)
        return
    amnt = len(cmcs) - 1
    try:
        if amnt > 0:
            SE = int(cmcs[1].replace(",", ""))
        else: SE = 1
        if amnt > 1:
            PE = int(cmcs[2].replace(",", ""))
        else: PE = 0
        threemen = False
        if ctx.message.mentions and amnt == 3:
            threemen = True
    except:
        if not ctx.guild:
            await ctx.send(traceback.format_exc().split('\n')[-2:])
        return
    sto = ""
    if PE > 5000:
        sto += "Infinifarmer"
        await ctx.send(sto + "\nEarnings bonus: Too dang high")
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
        l = math.trunc(math.log10(num) + 1 or 1)
        l = l if l else 1
        st = hm.get_pref(l)
        SEneed = math.ceil(10**(l) // (1.05 + PERL*.01)**PE // (.1 + SERL*.01))
        if not st:
            sto += "Infinifarmer"
        else: 
            if ((l - 1)%3 + 1 == 1):
                sto += st + "armer"
            elif ((l - 1)%3 + 1 == 2):
                sto += st + "armer II"
            elif ((l - 1)%3 + 1 == 3):
                sto += st + "armer III"
        role = discord.utils.get(roles, name=sto)
        sto += "\nEarnings multiplier: " + str(f"{num+1:,}") + "\nBonus per soul egg: " + str(BPE) + "\nTotal SE needed for next rank: " + str(f"{SEneed:,}")
        await ctx.send(sto)
    if amnt > 4 or threemen:
        rta = []
        rta.append(role)
        await hm.updateroles(ctx, rta, farmers, client)
        
        
@client.command(pass_context=True)
async def contract(ctx):
    #egg laying rate, internal hatchery rate, time left, current chickens, your eggs laid, internal hatchery calm
    cmc = ctx.message.content.lower().replace(",", "").replace('hr', 'h').split(" ")[1:]
    if len(cmc) == 0:
        ctx.message.content = "e!help contract"
        await client.process_commands(ctx.message)
        return
    
    prefix = "Wrong number formatting at "
    tfa = "Too few arguments."
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
    except IndexError:
        await ctx.send(tfa)  
        return
    except ValueError:
        await ctx.send(f"{prefix}egg laying rate.")   
        return
    try:
        ihr = int(cmc[1])//60
    except IndexError:
        await ctx.send(tfa)  
        return
    except ValueError:
        await ctx.send(f"{prefix}internal hatchery rate.")   
        return
    try:
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
    except IndexError:
        await ctx.send(tfa)  
        return
    except ValueError:
        await ctx.send(f"{prefix}time left.")   
        return
    try:
        if cmc[3][-1] == "k":
            pc = math.trunc(float(cmc[3][:-1])*1000)
        elif cmc[3][-1] == "m":
            pc = math.trunc(float(cmc[3][:-1])*mil)
        elif cmc[3][-1] == "b":
            pc = math.trunc(float(cmc[3][:-1])*bil)
        else: pc = int(cmc[3])
    except IndexError:
        await ctx.send(tfa)  
        return
    except ValueError:
        await ctx.send(f"{prefix}farm population.")   
        return
    try:
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
    except IndexError:
        await ctx.send(tfa)  
        return
    except ValueError:
        await ctx.send(f"{prefix}eggs laid.")   
        return
    try:
        if len(cmc) > 5:
            ihc = int(cmc[5])
        else: ihc = 20
        if ihc > 20 or ihc < 0:
            ihc = 20
    except IndexError:
        await ctx.send(tfa)  
        return
    except ValueError:
        await ctx.send(f"{prefix}internal hatchery calm.")   
        return
    try: 
        maxh = 1134*10**7
        if len(cmc) > 6:
            if cmc[6][-1] == "m":
                maxh = math.trunc(float(cmc[6][:-1])*mil)
            elif cmc[6][-1] == "b":
                maxh = math.trunc(float(cmc[6][:-1])*bil)
            else: maxh = int(cmc[6])
    except IndexError:
        await ctx.send(tfa)  
        return
    except ValueError:
        await ctx.send(f"{prefix}maximum hab capacity.")   
        return
    try:  
        maxsr = 311462*10**6*17*10
        if len(cmc) > 7:
            if cmc[7][-1] == "m":
                maxsr = math.trunc(float(cmc[7][:-1])*mil)
            elif cmc[7][-1] == "b":
                maxsr = math.trunc(float(cmc[7][:-1])*bil)
            elif cmc[7][-1] == "t":
                maxsr = math.trunc(float(cmc[7][:-1])*tril)
            else: maxsr = math.trunc(float(cmc[7]))
        maxsr = maxsr//60
    except IndexError:
        await ctx.send(tfa)  
        return
    except ValueError:
        await ctx.send(f"{prefix}shipping rate.")   
        return
    
    mh = None
    ms = None
    elrpc = elr / pc
    if tl > 2*30*24*3600:
        return
    for x in range(tl):
        if pc > maxh:
            pc = maxh
            if not mh:
                mh = x
        if pc*elrpc > maxsr:
            el += maxsr
            if not ms:
                ms = x
        else: el += pc*elrpc
        pc += ihr*4*(ihc/10+1)
    
    toofull = ''
    if mh:
        toofull += f' Habs were maxed at {hm.humantime(mh)}.'
    if ms:
        toofull += f' Shipping was maxed at {hm.humantime(ms)}.'
    
    fel = hm.humanize(el)
    
    await ctx.send(f'You will have produced approximately {fel} eggs by the time the given time period ends.{toofull}')
    
@client.command(pass_context=True)
async def rank(ctx):
    cmc = ctx.message.content.split(" ")[1:]
    eggguild = discord.utils.get(client.guilds, id=455380663013736479)
    members = []
    for x in cmc:
        mem = await hm.getmember(eggguild, x)
        if mem:
            members.append(mem)
    if not members:
        members.append(ctx.author)
    
    s = '```'
    lbnames = ['drones', 'oom', 'prestiges', 'souleggs']
    lbs = []
    for x in lbnames:
        file = open(f'{x}.json', "r")
        scores = json.load(file)
        lbs.append(scores)
        file.close()
    
    farmerlist = hm.farmers_l(eggguild.roles)
    flranks = {}
    acf = []
    num = 1
    for f in reversed(farmerlist):
        flranks.update({f: num})
        for m in f.members:
            if m.id not in acf:
                num += 1
                acf.append(m.id)
    
    for x in members:
        if not ctx.guild:
            x = discord.utils.get(eggguild.members, id=x.id)
        s += f'\n{hm.cap(str(x))}:\n'
        for y in reversed(x.roles):
            if y in farmerlist:
                s += f'    Farmer-role: {y}({flranks.get(y)}{hm.rankednum(flranks.get(y))})\n'
                break
        for y in range(len(lbs)):
            if not lbs[y].get(hm.cap(str(x))):
                continue
            rank = 1
            for k, v in sorted(lbs[y].items(), key=lambda x: int(x[1].replace(',', '')), reverse=True):
                if hm.cap(str(x)) == k:
                    break
                rank += 1
            if lbnames[y] == 'oom':
                theirscore = lbs[y].get(hm.cap(str(x)))
            else:
                theirscore = f'{int(lbs[y].get(hm.cap(str(x))).replace(",", "")):,}'
            if theirscore:
                s += f'    {lbnames[y]}:{" "*(12-len(lbnames[y]))}{theirscore}({rank}{hm.rankednum(rank)})\n'
    if s != '```':
        await ctx.send(s + '```')
        

@client.command()
async def fullleaderboard(ctx):
    cmc = ctx.message.content.split(" ")[1:]
    try:
        file = open(f'{cmc[0]}.json', "r")
    except:
        await ctx.send('Invalid leaderboard, oom/drones/prestiges/souleggs.')
        return
    scores = json.load(file)
    file.close()
    
    try:
        start = (int(cmc[1]) - 1) * 10
    except:
        await ctx.send('Invalid integer for a page.')
        return
    s = f'There are {len(scores)/10} pages.\n'
    n = 0
    uptoten = 0
    for k, v in sorted(scores.items(), key=lambda x: int(x[1].replace(',', '')), reverse=True):
        n += 1
        if n <= start:
            continue
        uptoten += 1
        s += f'{str(n)} {k}\n{" "*(2+2*len(str(n)))}{v}\n'
        if uptoten >= 10:
            break
    await ctx.send(s)

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
        else: await ctx.send("Please format it as " + com[0] + " category member score")
    else: await ctx.send("You don't have permission to use that command :sweat_smile: ")


@client.command(pass_context = True)
async def nick(ctx):
    s = ctx.message.content.split(" ", 1)[1]
    for x in s:
        if x not in asc:
            s = s.replace(x, '')
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
    await ctx.send(farmers[len(eb)-1])
    

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
    await ctx.send(s)

@client.command(pass_context = True)
async def getupdaterlb(ctx):
    file = open('updaters.json', 'r+')
    updaters = json.load(file)
    
    WTG = 0
    total = 0
    for x in updaters.values(): 
        total += x
    updaters.update({'Tiln': int(total*WTG + updaters.get('Tiln')*(1 - WTG))})
    s = f"```"
    for k, v in sorted(updaters.items(), key = itemgetter(1), reverse = True):
        if k == 'Tiln':
            s += '\n' + k + ": " + str(int(v))
        else:
            s += '\n' + k + ": " + str(int(v*(1 - WTG)))
    s += f'\nTotal updates since lb inception: {total}'
    await ctx.send(s + "```")
    
@client.command(pass_context = True)
async def graph(ctx):
#     updater = discord.utils.get(roles, name='Updater')
#     if not (ctx.message.channel.permissions_for(ctx.message.author).manage_roles or updater in ctx.message.author.roles):
#         await ctx.send('I\'ve recently decided that you don\'t have permission to use that command.')
#         return
    todel = await ctx.send("May not be working atm.")
    farmroles = []
    eb = []
    
    farmers = []
    farmers.append(discord.utils.get(roles, name="Eggs"))
    for x in hm.farmers_l(roles):
        farmers.append(x)
    larnum = 0
    total = 0
    acf = []
    torev = []
    orderednums = []
    farmernum = 28
    for f in reversed(farmers):
        num = 0
        for m in f.members:
            if m.id not in acf:
                num += 1
                acf.append(m.id)
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
    corrected = reversed(torev)
    farmdict = {}
    counter = 0
    for x in corrected:
        s += x + "\n"
        
        num = x.split(" ")[-1]
        rank = ' '.join(x.split(" ")[:2])
        farmdict.update({counter: f'{num},{rank}'})
        counter += 1
    
    bettertotal = total-int(farmdict[0].split(',')[0])
    temptotal = 0
    halftotal = bettertotal//2
    temphalftotal = 0
    medianrank = ""
    for k, v in farmdict.items():
        if "Eggs" in v:
            continue
        numrank = v.split(',')
        num = int(numrank[0])
        temptotal += k * num
        temphalftotal += num
        if temphalftotal > halftotal and not medianrank:
            medianrank = numrank[1]
        
    avgrank = farmdict.get(temptotal//bettertotal).split(',')[1]
    s += f'Average: {avgrank}\n'
    s += f'Median: {medianrank}\n'
    
    s += "Total: " + str(total) + "```"
    "Finished making the string part of the return"
    orderednums = list(reversed(orderednums))
    eb = list(reversed(eb))
    if eb[0] > larnum: eb[0] = larnum
    farmroles = list(reversed(farmroles))
    
    #plt.subplots()
    #ax.yaxis.set_major_formatter(formatter)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    bars = plt.bar(orderednums, eb)
    prop = fm.FontProperties(fname='portlligatslab-regular.ttf')
    plt.xticks(orderednums, farmroles, rotation=45, va='baseline', ha='right', fontsize=9, fontproperties=prop)
    plt.yticks(np.arange(-1, larnum+larnum//25, step=larnum//25), fontsize=9, fontproperties=prop)
    colors = [str(x.colour) for x in farmers]
    for x in range(len(eb)):
        bars[x].set_color(colors[x])       
    ax.set_facecolor('#404040')
    tim = int(time.time())
    fig.savefig(f"graphs/graph{tim}.png", facecolor='#cccccc')
    plt.close(fig)
    await ctx.send(file=discord.File(f"graphs/graph{tim}.png"), content=s)
    await todel.delete()
    "Finished making graph and sending everything"
    
    
@client.command()
async def allfarmerchannels(ctx):
    remove = False
    if ' ' in ctx.message.content:
        remove = True
    farmers = hm.farmers_l(roles)
    for x in reversed(farmers):
        if x in ctx.author.roles:
            farmers.remove(x)
            break
        else:
            farmers.remove(x)
    for x in reversed(farmers):
        if 'III' not in x.name:
            farmers.remove(x)
    if remove:
        await ctx.author.remove_roles(*farmers, reason='User initiated revocation of lower farmer roles')
        await ctx.send("Successfully removed your lower farmer channel access")
    else:
        await ctx.author.add_roles(*farmers, reason='User initiated addition of lower farmer roles')
        await ctx.send("Successfully gave you your lower farmer channel access")


@client.command()
async def coop(ctx):
    try:
        name = ctx.channel.name
        ID = ctx.channel.id
    except:
        name = 'bot-commands'
        ID = 455512567004004353
    if name in adchannels or ID in adchannels:
        await coopad2(ctx)
        return
    if name not in coopchannels and ID not in coopchannels:
        return
    cmc = ctx.message.content.split(" ")[1:]
    if len(cmc) < 2 :
        if ctx.channel.id == 455512567004004353 or type(ctx.channel) == discord.DMChannel:
            await ctx.send("Please specify a co-op name and a contract id.")
            return
        else:
            await ctx.send("Please specify a co-op name and a contract id. Please go to <#455512567004004353> or DMs to try again.")
            return
    #coopids = pb.contractids()
    
    coopid = ''
    coopname = ''
    for x in cmc:
        if x == x.lower() and not coopid:
            coopid = x
        else:
            coopname = x 
    if not coopid:
        if ctx.channel.id == 455512567004004353 or type(ctx.channel) == discord.DMChannel:
            await ctx.send("No valid co-op specified. Co-ops ids can be found with e!currentcontractids.")
            return
        else:
            await ctx.send("No valid co-op specified. Co-ops ids can be found with e!currentcontractids. Please go to <#455512567004004353> or DMs to try again.")
            return
    eggemojis = [discord.utils.get(client.emojis, id=455471603384582165), discord.utils.get(client.emojis, id=455467571613925418), discord.utils.get(client.emojis, id=455468082635210752), discord.utils.get(client.emojis, id=455468241582817299), discord.utils.get(client.emojis, id=455468270661795850), discord.utils.get(client.emojis, id=455468299480989696), discord.utils.get(client.emojis, id=455468299480989696), discord.utils.get(client.emojis, id=455468361099247617), discord.utils.get(client.emojis, id=455468394892886016), discord.utils.get(client.emojis, id=455468421048696843), discord.utils.get(client.emojis, id=455468444070969369), discord.utils.get(client.emojis, id=455468464639967242), discord.utils.get(client.emojis, id=455468487641661461), discord.utils.get(client.emojis, id=455468509099458561), discord.utils.get(client.emojis, id=455468542171807744), discord.utils.get(client.emojis, id=455468555421483010), discord.utils.get(client.emojis, id=455468564590100490), discord.utils.get(client.emojis, id=455468583426981908), discord.utils.get(client.emojis, id=455470627663380480), discord.utils.get(client.emojis, id=455470644646379520), discord.utils.get(client.emojis, id=460976773430116362), discord.utils.get(client.emojis, id=460976588893454337), discord.utils.get(client.emojis, id=503686019896573962)]
    try:
        eggemoji = eggemojis[pb.getcontractegg(coopid)]
    except:
        eggemoji = ""
    m = pb.coop(coopid, coopname)
    if type(m) == str: return
    cdeets = pb.contract2(coopid)
    cname = '' if 'GetContractsResponse' in str(type(cdeets)) else f'{cdeets.name}: '
    result = ""
    result += f"{m.coop} ({cname}{m.contract})\n"
    
    result += f"Eggs: {pb.humanize(m.eggs)} {eggemoji}\n"
    total_rate = sum([member.rate for member in m.members]) or 1
    result += f"Rate: {pb.humanize(total_rate)}/s ({pb.humanize(round(3600 * total_rate, 3))}/hr)\n"
    result += f"Time Remaining: {hm.humantime(m.timeleft)}\n"
    if 'GetContractsResponse' not in str(type(cdeets)):
        result += f"Minimum Projected Eggs: {pb.humanize(m.eggs + total_rate * m.timeleft)}/{hm.humanize(cdeets.rewards[-1].eggs)}\n"
        result += f'Maximum Time to Completion: {hm.humantime((cdeets.rewards[-1].eggs-m.eggs)/total_rate)}\n'
    result += '\n'
    
    maxmem = "?"
    try:
        maxmem = pb.getcontractmax(coopid)
    except: ""
    result += f"{len(m.members)}/{maxmem} Members:\n```ini\n"
    
    longest = 0
    for member in m.members:
        l = len(member.name)
        if member.x04 == 0:
            l += 2
        l -= 5-len(hm.humanize(member.eggs))
        if l > longest:
            longest = l
    
    plyrcnt = 1
    for member in m.members:
        zzz = ""
        if member.x04 == 0:
            zzz = 'zZ '#discord.utils.get(client.emojis, id=528887297517551617)
        start = f"{'0' if len(str(plyrcnt)) == 1 else ''}{plyrcnt} {member.name}"
        startlen = len(start)
        if zzz: startlen += 3
        try:
            timetook = member.eggs/member.rate
            displaytt = f'|{hm.humantime(timetook)}' if timetook >= (cdeets.duration - m.timeleft) else ''
        except: displaytt = ''
        eggs = hm.humanize(member.eggs)
        eggslen = len(eggs)
        memrate = hm.humanize(member.rate) + '/s ' if '.' not in hm.humanize(member.rate) else hm.humanize(member.rate) + '/s'
            
        result += f"{start}{' '*((longest+5)-startlen)}{zzz}{' '*(5-eggslen)}{eggs}|{memrate}{displaytt}\n"
        plyrcnt += 1
    result = result[:-1]
    
    pgs = math.ceil(len(result)/1995)
    splitres = result.split('\n')
    tempres = ""
    pgcnt = 1
    for x in range(len(splitres)):
        if not tempres and x != 0:
            tempres = f'{m.coop} {pgcnt}/{pgs}\n```ini\n'
        tempres += splitres[x] + '\n'
        if x+1 == len(splitres) or len(tempres + splitres[x+1]) > 1997:
            await ctx.send(tempres[:-1] + '```')
            tempres = ""
            pgcnt += 1
    
async def coopad2(ctx):
    
    cmc = ctx.message.content.split(" ")[1:]
    if len(cmc) < 2 :
        if ctx.channel.id == 455512567004004353 or type(ctx.channel) == discord.DMChannel:
            await ctx.send("Please specify a co-op name and a contract id.")
            return
        else:
            await ctx.send("Please specify a co-op name and a contract id. Please go to <#455512567004004353> or DMs to try again.")
            return
    
    coopid = ''
    coopname = ''
    for x in cmc:
        if x == x.lower() and not coopid:
            coopid = x
        else:
            coopname = x 
    if not coopid:
        if ctx.channel.id == 455512567004004353 or type(ctx.channel) == discord.DMChannel:
            await ctx.send("No valid co-op specified. Co-ops ids can be found with e!currentcontractids.")
            return
        else:
            await ctx.send("No valid co-op specified. Co-ops ids can be found with e!currentcontractids. Please go to <#455512567004004353> or DMs to try again.")
            return
    m = pb.coop(coopid, coopname)
    if type(m) == str: return
    if len(m.members) >= pb.getcontractmax(coopid) and not ctx.channel.id == 455512567004004353 and not type(ctx.channel) == discord.DMChannel:
        await ctx.send("This co-op is full. Please go to <#455512567004004353> or DMs to try again.")
        return
    
    
    eggemojis = [discord.utils.get(client.emojis, id=455471603384582165), discord.utils.get(client.emojis, id=455467571613925418), discord.utils.get(client.emojis, id=455468082635210752), discord.utils.get(client.emojis, id=455468241582817299), discord.utils.get(client.emojis, id=455468270661795850), discord.utils.get(client.emojis, id=455468299480989696), discord.utils.get(client.emojis, id=455468299480989696), discord.utils.get(client.emojis, id=455468361099247617), discord.utils.get(client.emojis, id=455468394892886016), discord.utils.get(client.emojis, id=455468421048696843), discord.utils.get(client.emojis, id=455468444070969369), discord.utils.get(client.emojis, id=455468464639967242), discord.utils.get(client.emojis, id=455468487641661461), discord.utils.get(client.emojis, id=455468509099458561), discord.utils.get(client.emojis, id=455468542171807744), discord.utils.get(client.emojis, id=455468555421483010), discord.utils.get(client.emojis, id=455468564590100490), discord.utils.get(client.emojis, id=455468583426981908), discord.utils.get(client.emojis, id=455470627663380480), discord.utils.get(client.emojis, id=455470644646379520), discord.utils.get(client.emojis, id=460976773430116362), discord.utils.get(client.emojis, id=460976588893454337), discord.utils.get(client.emojis, id=503686019896573962)]
    try:
        eggemoji = eggemojis[pb.getcontractegg(coopid)]
    except:
        eggemoji = ""
    
    cdeets = pb.contract2(coopid)
    cname = '' if 'GetContractsResponse' in str(type(cdeets)) else f'{cdeets.name}: '
    result = ""
    result += f"{m.coop} ({cname}{m.contract})\n"
    
    result += f"Eggs: {pb.humanize(m.eggs)} {eggemoji}\n"
    total_rate = sum([member.rate for member in m.members]) or 1
    result += f"Rate: {pb.humanize(total_rate)}/s ({pb.humanize(round(3600 * total_rate, 3))}/hr)\n"
    result += f"Time Remaining: {hm.humantime(m.timeleft)}\n"
    if 'GetContractsResponse' not in str(type(cdeets)):
        result += f"Minimum Projected Eggs: {pb.humanize(m.eggs + total_rate * m.timeleft)}/{hm.humanize(cdeets.rewards[-1].eggs)}\n"
        result += f'Maximum Time to Completion: {hm.humantime((cdeets.rewards[-1].eggs-m.eggs)/total_rate)}\n'
    result += f"{len(m.members)}/{pb.getcontractmax(coopid)} Members\n"
    result = result[:-1]
    await ctx.send(result[:2000])
        
@client.command()
async def coopad(ctx):
    try:
        name = ctx.channel.name
        ID = ctx.channel.id
    except:
        name = 'bot-commands'
        ID = '455512567004004353'
    if name in adchannels or name in coopchannels or ID in adchannels or ID in coopchannels:
        await coopad2(ctx)


async def cci2(ctx):
    s = '```'
    for x in pb.contractids():
        s += "\n" + x 
    s += '```'
    await ctx.send(s)
    
@client.command()
async def cci(ctx):
    await cci2(ctx)
    
@client.command()
async def currentcontractids(ctx):
    await cci2(ctx)
    

async def cc2(ctx):
    cmc = ctx.message.content.split(" ")[1:]
    if len(cmc) == 0:
        ctx.message.content = "e!help completedcontracts"
        await client.process_commands(ctx.message)
        return
    data = pb.backup(cmc[0])
    if not str(data).strip(): return
    totalpe = 0
    s = ''
    for contract in data.contracts.complete:
        actuallycompleted = True
        for reward in contract.contract.rewards:
            if reward.eggs > contract.reward_count:
                actuallycompleted = False
            if reward.type == 4 and actuallycompleted:
                totalpe += reward.quantity
        if not actuallycompleted:
            s += '*'
        s += f'{contract.contract.name}({contract.contract.identifier})\n'
    await ctx.send(f'Total PE from these contracts: {int(totalpe)}\nAttempted contracts:\n```\n *==Incomplete Contract\n{s}'[:1997] + '```')
    
@client.command()
async def cc(ctx):
    await cc2(ctx)

@client.command()
async def completedcontracts(ctx):
    await cc2(ctx)
    
@client.command()
async def alleggslaid(ctx):
    cmc = ctx.message.content.split(" ")[1:]
    data = pb.backup(cmc[0])
    if not str(data).strip(): return
    eggs = ['Edible', 'Superfood', 'Medical', 'Rocket Fuel', 'Super Material', 'Fusion', 'Quantum', 'Immortality', 'Tachyon', 'Graviton', 'Dilithium', 'Prodigy', 'Terraform', 'Antimatter', 'Dark Matter', 'A.I.', 'Nebula']
    s = '```'
    for x, y in zip(eggs, data.stats.x08):
        s += f'\n{x}: {hm.humanize(y)}'
    await ctx.send(s + '```')

@client.command()
async def submitid(ctx):
    file = open('nosubmit.json', 'r+')
    nosubmitters = json.load(file)
    if str(ctx.author.id) in nosubmitters:
        return
    
    file = open('ids.json', 'r+')
    identifiers = json.load(file)
    
    cmc1 = ctx.message.content.split(" ")[1]
    if cmc1 in identifiers.keys():
        await ctx.send('That indentifier has already been assigned to someone!')
        return
    if not str(pb.backup(cmc1)).strip():
        await ctx.send('Invalid identifier')
        return
    
    identifiers.update({cmc1:str(ctx.author.id)})
    
    file = open('ids.json', 'w+')
    file.write(json.dumps(identifiers))
    
    await ctx.message.delete()
    await ctx.send("Success!")
    
@client.command()
async def getids(ctx):
    updater = discord.utils.get(roles, name='Updater')
    if not ctx.channel.permissions_for(ctx.author).manage_roles and not updater in ctx.author.roles:
        return
    file = open('ids.json', 'r+')
    identifiers = json.load(file)
    
    s = ""
    for k, v in identifiers.items():
        mem = await ctx.guild.fetch_member(int(v))
        s += f"{mem}: {k}, "
    await ctx.send(s[:-2][:2000])

@client.command()
async def forceupdate(ctx):
    updater = discord.utils.get(roles, name='Updater')
    if not ctx.channel.permissions_for(ctx.author).manage_roles and not updater in ctx.author.roles:
        return
    cmc = ctx.message.content.split(" ")[1:]
    if not cmc:
        await hm.loopableIDtasks(ctx.guild)
        return
    
    file = open('ids.json', 'r+')
    identifiers = json.load(file)
    
    for k, v in identifiers.items():
        #cont = False
        for x in cmc:
            user = hm.getmember(ctx.guild, x)
            if v == str(user.id):
                hm.IDtasks(ctx.guild, user, k)
                #cont = True
                break
        #if cont: continue
        
@client.command()
async def removeids(ctx):
    updater = discord.utils.get(roles, name='Updater')
    if not ctx.channel.permissions_for(ctx.author).manage_roles and not updater in ctx.author.roles:
        return
    cmc = ctx.message.content.split(" ")[1:]
    if not cmc:
        await hm.loopableIDtasks(ctx.guild)
        return
    
    file = open('ids.json', 'r+')
    identifiers = json.load(file)
    
    for k, v in identifiers.items():
        for x in cmc:
            user = await hm.getmember(ctx.guild, x)
            if v == str(user.id):
                del identifiers[k]
                break
    file = open('ids.json', 'w')
    file.write(json.dumps(identifiers))


@client.command()
async def nosubmit(ctx):
    updater = discord.utils.get(roles, name='Updater')
    if not ctx.channel.permissions_for(ctx.author).manage_roles and not updater in ctx.author.roles:
        return
    cmc = ctx.message.content.split(" ")[1:]
    
    file = open('nosubmit.json', 'r')
    nosubmitters = json.load(file)
    
    s = "```"
    for x in cmc:
        user = await hm.getmember(ctx.guild, x)
        if user:
            if str(user.id) not in nosubmitters:
                nosubmitters.append(str(user.id))
                s += f'\nAdded{str(user)}'
            if str(user.id) in nosubmitters:
                nosubmitters.remove(str(user.id))
                s += f'\nRemoved{str(user)}'
                
    file = open('nosubmit.json', 'w')
    file.write(json.dumps(nosubmitters))
    await ctx.send(f'{s}```')

@client.command()
async def geteb(ctx):
    cmc = ctx.message.content.split(" ")[1:]
    if not cmc:
        return
    
    file = open('ids.json', 'r+')
    identifiers = json.load(file)
    
    s = '```'
    for k, v in identifiers.items():
        for x in cmc:
            user = await hm.getmember(ctx.guild, x)
            if v == str(user.id):
                s += f'\n{user}: {int(pb.eb(k)):,}'
    if s == '```':
        await ctx.send("Invalid input.")
    else:
        await ctx.send(f'{s}```')


try:
    file = open(os.path.dirname(__file__) + "/../eitok.txt")
    client.run(file.readline())
    file.close
except:
    client.run(sys.argv[1])



