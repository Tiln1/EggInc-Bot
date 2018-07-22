'''
Created on May 12, 2018

@author: Tiln
'''
import math
import os.path
import datetime

import discord
class HelpMethods(object):
    
    
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


    async def updateroles(self, ctx, rolestoadd, rolestoremove, client):
        updater = discord.utils.get(ctx.message.server.roles, name='Updater')
        user = ""
        cmcs = ctx.message.content.split(" ")[1]
        if cmcs.isdigit():
            user = ctx.message.server.get_member(cmcs)
        else: user = ctx.message.mentions[0]
        if ctx.message.channel.permissions_for(ctx.message.author).manage_roles or updater in ctx.message.author.roles:
            if (ctx.message.mentions or cmcs.isdigit()) and len(ctx.message.content.split(" ")) > 2:
                sucr = ""
                exist = ""
                rtrnothave = ""
                for role in rolestoremove:
                    if role in ctx.message.server.roles:
                        if role in user.roles:
                            sucr += "\n" + str(role)
                            await client.remove_roles(user, role)
                        else: rtrnothave += "\n" + str(role)
                    else: exist += "\n" + str(role)
                rtahave = ""
                suca = ""
                for role in rolestoadd:
                    if role in ctx.message.server.roles:
                        if role not in user.roles:
                            suca += "\n" + str(role)
                            await client.add_roles(user, role)
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
                await client.say("Successfully updated role(s)\n```" + string + " ```")
            else: await client.say("Please format it as " + ctx.message.content.split(" ")[0] + " @username role")
        else: await client.say("You don't have permission to use that part of that command :sweat_smile: ")
    

    async def updatelb(self, filename, username, score, message_id, client):
        file = open(filename, "r")
        content = file.read()
        file.close()
        contents = content.split("\n")
        if (len(contents)) < 2:
            await client.send_message(client.get_channel("455512668606955541"), ("Why is the leaderboard " + filename.replace(".txt", "") + " gone on our end?"))
            return
        newcontent = contents[0] + "\n" + contents[1]
        username = username.replace("_", " ")
        username = self.cap(username)
        nu = True
        namu = False
        numscore = int(score.replace(",", ""))
        for x in range(3, len(contents), 2):
            num = math.trunc((x-3)/2+1)
            sol = contents[x].replace(",", "").replace(".", "").replace(" ", "")
            nam = contents[x-1][3:]
            if namu:
                num -= 1
            if numscore > int(sol) and nu:
                nu = False
                newcontent += "\n"
                if len(str(num)) == 1: newcontent += "0"
                newcontent += str(num) + " " + username + "\n" + "   " + str(score)
            if not nam == username and not nu:
                plusone = contents[x-1][2:]
                newcontent += "\n"
                if len(str(num+1)) == 1: newcontent += "0"
                newcontent += str(num+1) + plusone + "\n" + contents[x]
            elif nu and not nam == username:
                plusone = contents[x-1][2:]
                newcontent += "\n"
                if len(str(num)) == 1: newcontent += "0"
                newcontent += str(num) + plusone + "\n" + contents[x]
            elif nam == username:
                namu = True
            
        while(len(newcontent) > 1996):
            newcontent = newcontent.rsplit("\n", 2)[0]
        newcontent += "\n```"
    
        file = open(filename, "w")
        file.write(newcontent)
        file.close()
    
        await client.http.edit_message(message_id, "455385893537185806", newcontent)
        
        split = client.get_channel("455512668606955541").topic.split("\n")
        newstr = ""
        s = contents[-2].strip()
        if filename == "prestiges.txt": 
            for x in range(len(split)):
                if x == 1:
                    newstr += "Prestiges: " + s + "\n"
                else: newstr += split[x] + "\n"
        elif filename == "oom.txt":
            for x in range(len(split)):
                if x == 2:
                    newstr += "OoM: " + s + "\n"
                else: newstr += split[x] + "\n"
        elif filename == "souleggs.txt":
            for x in range(len(split)):
                if x == 3:
                    newstr += "Soul Eggs: " + s + "\n"
                else: newstr += split[x] + "\n"
        elif filename == "drones.txt":
            for x in range(len(split)):
                if x == 4:
                    newstr += "Drones: " + s
                else: newstr += split[x] + "\n"
                
        await client.edit_channel(client.get_channel("455512668606955541"), topic=newstr)
        await self.getleaderboards(client, client.get_channel("455385893537185806"), getlb=False, lb=filename.replace(".txt", ""))
    
    
    async def getleaderboards(self, client, channel, getlb=True, lb=None):
        async for x in client.logs_from(channel):
            date = str(datetime.datetime.utcnow()).replace(" ", "-").replace(":", "")
            if "Prestige Count" in x.content and (lb == None or lb == "prestiges"):
                file = open("prestiges.txt")
                filebackup = open(os.path.dirname(__file__) + "/../pc/"+ date +".txt", "w+")
            elif "Soul Eggs" in x.content and (lb == None or lb == "souleggs"):
                file = open("souleggs.txt")
                filebackup = open(os.path.dirname(__file__) + "/../se/"+ date +".txt", "w+")
            elif "Drone Takedowns" in x.content and (lb == None or lb == "drones"):
                file = open("drones.txt")
                filebackup = open(os.path.dirname(__file__) + "/../dt/"+ date +".txt", "w+")
            elif "OoM" in x.content and (lb == None or lb == "oom"):
                file = open("oom.txt")
                filebackup = open(os.path.dirname(__file__) + "/../oom/"+ date +".txt", "w+")
            try:
                filebackup.write(file.read())
                if getlb:
                    file.write(x.content)  
                file.close
                filebackup.close
            except: print(x.content)

        
    def cap(self, toCap):
        if ord(toCap[0]) > 96 and ord(toCap[0]) < 123:
            toCap = chr(ord(toCap[0]) - 32) + toCap[1:]
        return toCap
    
    
    def get_farmer_role(self, roles, message):
        farmers = reversed(self.farmers_l(roles))
        for x in farmers:
            if x in message.author.roles:
                return x
    
    
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
        