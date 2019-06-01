'''
Created on May 12, 2018

@author: Tiln
'''
import math
import os.path
import json
import asyncio
from datetime import datetime
from decimal import Decimal, getcontext


import egginc as pb

import discord
class HelpMethods(object):
    conts = None
    async def getmember(self, guild, possmember):
        member = None
        if '#' in possmember:
            member = discord.utils.get(guild.members, name=possmember.split('#')[0], discriminator=possmember.split('#')[1])
        elif possmember.isdigit():
            n = int(possmember)
            if n > 10000000000000000:
                member = discord.utils.get(guild.members, id=n)
        elif possmember[3:-1].isdigit():
            n = int(possmember[3:-1])
            if n > 10000000000000000:
                member = discord.utils.get(guild.members, id=n)
        else:
            member = discord.utils.get(guild.members, mention=possmember)
        return member
    
    def getchannel(self, guild, posschannel):
        channel = None
        if posschannel.isdigit():
            n = int(posschannel)
            if n > 10000000000000000:
                channel = discord.utils.get(guild.channels, id=n)
        else:
            channel = discord.utils.get(guild.channels, mention=posschannel) or discord.utils.get(guild.channels, name=posschannel)
        return channel
    
    def get_pref(self, l):
        pref = ["F", "Kilof", "Megaf", "Gigaf", "Teraf", "Petaf", "Exaf", "Zettaf", "Yottaf"]
        if l < 28:
            return pref[(l+2)//3-1]
        else: return False


    def farmers_l(self, roles):
        farmers = []
        for x in range(1, 28):
            string = self.get_pref(x)
            suff = (x - 1)%3 + 1
            if suff == 1:
                string += "armer"
            else:
                string += "armer " + ("I" * suff)
            farmers.append(discord.utils.get(roles, name=string))
        farmers.append(discord.utils.get(roles, name="Infinifarmer"))
        return farmers
    
    def earningsmult(self, se, pe):
        return se * 1.5 * 1.1**pe + 1
    
    def int(self, num):
        try: int(num)
        except: return False
        return True


    async def updateroles(self, ctx, rolestoadd, rolestoremove, client):
        updater = discord.utils.get(ctx.message.server.roles, name='Updater')
        user = ""
        cmcs = ctx.message.content.split(" ")[1]
        if cmcs.isdigit():
            user = await ctx.message.server.fetch_member(cmcs)
        else: user = ctx.message.mentions[0]
        if not ctx.message.channel.permissions_for(ctx.message.author).manage_roles or updater in ctx.message.author.roles:
            await ctx.message.channel.send("You don't have permission to use that part of that command :sweat_smile: ")
            return
        if not (ctx.message.mentions or cmcs.isdigit()) and len(ctx.message.content.split(" ")) > 2:
            await ctx.message.channel.send("Please format it as " + ctx.message.content.split(" ")[0] + " @username role")
            return
        sucr = ""
        exist = ""
        rtrnothave = ""
        for role in rolestoremove:
            if role in ctx.message.server.roles:
                if role in user.roles:
                    sucr += "\n" + str(role)
                    await user.remove_roles(role)
                else: rtrnothave += "\n" + str(role)
            else: exist += "\n" + str(role)
        rtahave = ""
        suca = ""
        for role in rolestoadd:
            if role in ctx.message.server.roles:
                if role not in user.roles:
                    suca += "\n" + str(role)
                    await user.add_roles(role)
                else: rtahave += "\n" + str(role)
            else: exist += "\n" + str(role)
        string = ""
        amnt = len(exist.split("\n")) - 1 
        if sucr: string += "These roles were successfully removed: " + sucr + "\n"
        if suca: string += "These roles were successfully added: " + suca + "\n"
        if exist: string += "I attempted to add/remove " + str(amnt) + " roles that were not added/removed because they do not exist. Some other roles still may've succeeded\n"
        if rtahave: string += "These roles were already on the user:" + rtahave + "\n"
        string = string[:-1]
        #if rtrnothave: print(rtrnothave)
        await ctx.message.channel.send("Successfully updated role(s)\n```" + string + " ```")
        
    def rankednum(self, num):
        num = str(num)
        if len(num) > 1 and num[-2] == '1':
            return 'th'
        ranks = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']
        return ranks[ord(num[-1])-48]
    

    async def updatelb(self, filename, username, score, message):
        file = open(filename, "r")
        scores = json.load(file)
        file.close()
        intscore = int(score.replace(',', ''))
        if intscore == 0 or filename != 'oom.json': lowerable = True
        else: lowerable = False
        username = self.cap(username.replace("_", " "))
        try:
            oldscore = int(scores.get(username).replace(',', ''))
        except:
            oldscore = 0
        if intscore <= oldscore and not lowerable:
            return
        
        scores.update({username: score})
        file = open(filename, "w")
        file.write(json.dumps(scores))
        file.close()
        
        s = message.content.split('\n', 1)[0] + '\n'
        n = 0
        for k, v in sorted(scores.items(), key=lambda x: int(x[1].replace(',', '')), reverse=True):
            n += 1
            s += str(n) if n > 9 else f'0{str(n)}'
            s += f' {k}\n{" "*6}{v}\n'
        s = s[:-1]
        while(len(s) > 1999):
            s = s.rsplit("\n", 2)[0]
        s += "\n"
        await message.edit(content=s)
        
    
    async def strtolb(self, string, user, guild):
        if string[-3] == ',':
            await self.updatelb("oom.json", user, string, await guild.get_channel(455385893537185806).fetch_message(457715280152363018))
        elif len(string) < 10 and ',' in string:
            await self.updatelb("drones.json", user, string, await guild.get_channel(455385893537185806).fetch_message(457715344367288331))
        elif len(string) >= 10 and ',' in string:
            await self.updatelb("souleggs.json", user, string, await guild.get_channel(455385893537185806).fetch_message(457715345546018828))
        else:
            await self.updatelb("prestiges.json", user, string, await guild.get_channel(455385893537185806).fetch_message(457715346615566338))
            
    
    async def updaterole(self, guild, auth, num):
        roles = sorted(guild.roles, key=lambda x: x.position, reverse=False)
        eggs = discord.utils.get(guild.roles, name="Eggs")
        offset = eggs.position-1 
        prev = eggs
        for x in range(offset, offset+30):
            if roles[x] in auth.roles:
                prev = roles[x]
        if num != 0:
            new = discord.utils.get(roles, position=(num+offset+1))
        else: new = prev
        
        pref = '+'
        if new != prev:
            authroles = auth.roles
            authroles.remove(prev)
            authroles.append(new)
            try: await auth.edit(roles=authroles)
            except: return
            if new.position > prev.position:
                pref = '+'
            else:
                pref = '-'
        else: num = 0
        return [num, prev, new, pref]

    
    async def getleaderboards(self, client, channel, getlb=True, lb=None):
        async for x in channel.history():
            date = str(datetime.datetime.utcnow()).replace(" ", "-").replace(":", "")
            if "Prestige Count" in x.content and (lb == None or lb == "prestiges"):
                filer = open("prestiges.txt", "r")
                if lb == None: lebo = "prestiges" 
                filebackup = open(os.path.dirname(__file__) + "/../pc/"+ date +".txt", "w+")
            elif "Soul Eggs" in x.content and (lb == None or lb == "souleggs"):
                filer = open("souleggs.txt","r")
                if lb == None: lebo = "souleggs" 
                filebackup = open(os.path.dirname(__file__) + "/../se/"+ date +".txt", "w+")
            elif "Drone Takedowns" in x.content and (lb == None or lb == "drones"):
                filer = open("drones.txt", "r")
                if lb == None: lebo = "drones" 
                filebackup = open(os.path.dirname(__file__) + "/../dt/"+ date +".txt", "w+")
            elif "OoM" in x.content and (lb == None or lb == "oom"):
                filer = open("oom.txt", "r")
                if lb == None: lebo = "oom" 
                filebackup = open(os.path.dirname(__file__) + "/../oom/"+ date +".txt", "w+")
            try:
                filebackup.write(filer.read())
                if getlb:
                    filew = open(lb or lebo + ".txt", "w")
                    filew.write('\n' + x.content)  
                    filew.close
                filebackup.close
            except: print(x.content)

        
    def cap(self, toCap):
        if ord(toCap[0]) > 96 and ord(toCap[0]) < 123:
            toCap = chr(ord(toCap[0]) - 32) + toCap[1:]
        return toCap
    
    def humanize(self, num):
        suffixes = ["","k","M","B","T","q","Q","s","S","o","N","d","U","D","Td","qd","Qd","sd","Sd","od","Nd","V","uV","dV",'tV','qV','QV','sV','SV','oV','NV','T']
        p = (len(str(int(num)))-1)//3
        getcontext().prec = 3
        x = Decimal(Decimal(num) / (10 ** (Decimal(p) * 3)))
#         sp = ''
#         if '.' not in str(x):
#             sp = ' '
        return f"{x}{suffixes[p]}"
    
    def humantime(self, seconds):
        human = ''
        terms = 0
        if terms < 3 and seconds >= 31104000 and int(seconds//31104000) != 0:
            human += f'{int(seconds//31104000)}y'
            terms += 1
        if terms < 3 and seconds >= 2592000 and int(seconds//2592000%12) != 0:
            human += f'{int(seconds//2592000%12)}m'
            terms += 1
        if terms < 3 and seconds >= 86400 and int(seconds//86400%30) != 0:
            human += f'{int(seconds//86400%30)}d'
            terms += 1
        if terms < 3 and seconds >= 3600 and int(seconds//3600%24) != 0:
            human += f'{int(seconds//3600%24)}h'
            terms += 1
        if terms < 3 and seconds >= 60 and int(seconds//60%60) != 0:
            human += f'{int(seconds//60%60)}m'
            terms += 1
        if terms < 3 and seconds >= 1 and int(seconds%60) != 0:
            human += f'{int(seconds%60)}s'
            terms += 1
        if terms < 3 and seconds >= 0.001 and int(seconds*1000%1000) != 0:
            human += f'{int(seconds*1000%1000)}ms'
            terms += 1
        return human
    
    
    def get_farmer_role(self, roles, message):
        farmers = reversed(self.farmers_l(roles))
        for x in farmers:
            if x in message.author.roles:
                return x
    
    
    def updatetoEOTW(self, member):
        file = open('updaters.json', 'r+')
        updaters = json.load(file)
        file.close()
        amnt = updaters.get(member.name) or 0
        updaters.update({member.name:amnt+1})
        file = open('updaters.json', 'w+')
        file.write(json.dumps(updaters))
        file.close()
        
    
    async def loopIDtasks(self, guild):
        while(True):
            await asyncio.sleep(55)
            d = datetime.utcnow()
            if d.hour == 17 and d.minute == 0:
                await self.loopableIDtasks(guild)
                await asyncio.sleep(120)
#             conts = pb.contracts()
#             if self.conts and self.conts != conts and len(self.conts) < len(conts):
#                 await discord.utils.get(guild.channels, id=455393480957624330).send(f"New Contract(s)!\n{conts[:1980]}")
#             self.conts = conts
    
        
    async def loopableIDtasks(self, guild):
        file = open('ids.json', 'r+')
        identifiers = json.load(file)
        todel = []
        
        for k, v in identifiers.items():
            backup = pb.backup(k)
            if not str(backup).strip():
                todel.append(k)
                continue
            user = await guild.fetch_member(int(v))
            await self.IDtasks(guild, user, backup=backup)
            await asyncio.sleep(0.01)
        for x in todel:
            del identifiers[x]
        if todel:
            file = open('ids.json', 'w')
            file.write(json.dumps(identifiers))
        
    
    async def IDtasks(self, guild, user, backup=None, identifier=None):
        if not identifier and not backup:
            return
        if not backup:
            backup = pb.backup(identifier)
        await self.updatelb("drones.json", str(user), f'{backup.stats.drone_takedowns:,}', await guild.get_channel(455385893537185806).fetch_message(457715344367288331))
        await self.updatelb("souleggs.json", str(user), f'{backup.data.soul_eggs:,}', await guild.get_channel(455385893537185806).fetch_message(457715345546018828))
        await self.updatelb("prestiges.json", str(user), f'{backup.stats.prestige_count}', await guild.get_channel(455385893537185806).fetch_message(457715346615566338))
        
        await self.updaterole(guild, user, len(str(int(pb.eb(backup=backup)))))
    
#     async def settopictwohours(self, guild):
#         datetime.now()
    
    
#   async def images(self, imageUrl, message, client):
#         sep = "  "
#         imglist = open("images.txt", "r").read().split("\n")
#         imageName = imageUrl.split("/")[-1].split(".")[0]
#         good = True
#         inpimg = await self.image(imageUrl)
#         for image in imglist:
#             dbimg = await self.image(image.split(sep)[0])
#             if imageUrl == image:
#                 good = False
#                 await client.send_message(client.get_channel("426315610897645589"), "Notification: ```" + image + " from the database and " + imageUrl + "``` from " + message.author.mention + " are completely identical")

#             elif dbimg and inpimg:
#                 h1 = dbimg.histogram()
#                 h2 = inpimg.histogram()
#                 rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
#                 if rms < 100:
#                     good = False
#                     await client.send_message(client.get_channel("426315610897645589"), "Notification: ```" + image + " from the database and " + imageUrl + "``` from " + message.author.mention + " are probably identical images")
   
#             if imageName == image.split(sep)[0].split("/")[-1].rsplit(".", 1)[0] and not imageName == "image" and not imageName == "unknown" and good == True:
#                 good = False
#                 await client.send_message(client.get_channel("426315610897645589"), "Notification: ```" + image + " from the database and " + imageUrl + "``` from " + message.author.mention + " have identical names.")
            
            #newcontent = newcontent.rsplit("\n", 2)[0]
#             elif not dbimg:
#                 print(image)
#                 place = imglist.index(image)
#                 f = open("images.txt", "r")
#                 images = f.read().split("\n")
#                 f.close()
#                 del images[place]
#                 s = ""
#                 f = open("images.txt", "w")
#                 for x in images:
#                     s += x + "\n"
#                 f.write(s)
#                 f.close()
#         if good:
#             f = open("images.txt", "a")
#             f.write("\n" + imageUrl + sep + str(message.author))
#             f.close()
             
#     async def image(self, url):
#         try:
#             response = requests.get(url)
#             img = Image.open(BytesIO(response.content))
#             return img
#         except:
#             return False
        