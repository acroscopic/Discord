import discord
import asyncio
import requests
import time
import json
import random
import string
import re
from datetime import datetime
from time import strftime
from time import gmtime

token = open("token.txt", "r").read().strip().replace("\n", "")
client = discord.Client()

@client.event
async def on_ready():
	print("Username : {0.name}".format(client.user))
	print("User ID : {0.id}" "\n".format(client.user))

async def bfr():
	await client.wait_until_ready()
	while client.is_closed:
		seconds = (random.randint(36000,86400))
		print(time.strftime("Current time : " + "%Y-%m-%d %I:%M %p", time.localtime()))
		print(strftime("Time left : %H hours, %M minutes, and %S seconds", gmtime(seconds)))
		await asyncio.sleep(seconds)
		await client.get_user(117666744021024771).send("ily")
		print("message sent" "\n")

@client.event
async def on_message(message):
	if message.author != client.user:
		return

	if message.content.startswith('.d'):
		if re.search(r'\d+$', message.content) is not None:
			t = int(message.content[len('.d'):].strip())
		else:
			t = 15
		async for m in message.channel.history(limit=t):
			try:
				if m.author == client.user:
					await m.delete()
			except: pass

	if message.content.startswith('.t'):
		msg = random.choice(json.loads(open('messages.json').read()))
		censored = "2"
		mymessage = censored in msg
		while mymessage == False:
			print(msg)
			await message.channel.send(str(msg))
		elif mymessage == True:
			break
	
client.loop.create_task(bfr())
client.run(token, bot=False)
