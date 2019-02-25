import discord
import sys
import time
import os, signal


with open("mep.txt") as f:
    TOKEN = f.readline().strip()

logfilename = (str(time.time()) + ".txt")
f = open(logfilename, "w+")
print ("logs stored in " + logfilename)
f.close()


client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        msg = 'REEEE {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        print(msg)

   
    content = str(message.content).lower()
    content = str(message.author) + ": " + content
    print(content)

    cmd = ('echo ' + '\'' + content + '\'' + ' >> ' + logfilename) #add channel
    os.system(cmd)

    if (message.author.id == '282031512713560064') or (message.author.id == '280925106685870082'):
    	if str(message.content).lower() == 'ok':
    		msg = ("REEEE WE GET IT {0.author.mention}, YOU'RE OK GEEEEZ").format(message)
    		await client.send_message(message.channel, msg)
    		print(msg)

#    if message.author.id == '280925106685870082' and str(message.content).lower() == '-terminate':
#    	print("ENDING")
#   	os.kill(p.pid, signal.SIGINT)

#SP[ECIAL CHAREFCTERS AND SHRUSDHGSS]
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)