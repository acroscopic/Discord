import discord
import asyncio
import requests
import sys
import time
import random
import json
import os
import string
from discord.ext import commands
from datetime import datetime

token = open("token.txt", "r").read().strip().replace("\n", "")
client = discord.Client()

#walldog ready
@client.event
async def on_ready():
	game = discord.Game("in the wall")
	await client.change_presence(status=discord.Status.dnd, activity=game)
	print('logged in as walldog')
	print('--------------------')

#user joins
@client.event
async def on_member_join(member):
	channel = client.get_channel(574399381621571596)
	msg = "welcome to the walldog fan server :sunglasses: {0.mention} ".format(member)
	await channel.send(msg)

#user leaves
@client.event
async def on_member_remove(member):
	channel = client.get_channel(574399381621571596)
	msg = "bye friend come back soon :frowning: {0.mention}".format(member)
	await channel.send(msg)

#chat commands
@client.event
async def on_message(message):

	if message.author == client.user:
		return

#walldog talks woa

	a = ('walldog', '<@589505610937008239>')
	lower = str.lower(message.content)
	if lower.startswith(a):
		msg = ("im in the wall {0.author.mention}".format(message))
		await message.channel.send(msg)

	b = ('good bot', 'good job walldog', 'gj walldog', 'good job <@589505610937008239>')
	lower = str.lower(message.content)
	if lower.startswith(b):
		await message.channel.send('ty')

	c = ('i hate walldog', 'bad bot')
	lower = str.lower(message.content)
	if lower.startswith(c):
		await message.channel.send(':frowning:')

	d = ('i love <@589505610937008239>', 'i love walldog')
	lower = str.lower(message.content)
	if lower.startswith(d):
		msg = ('ily2 {0.author.mention}'.format(message))
		await message.channel.send(msg)


#commands

	aa = ('>help')
	lower = str.lower(message.content)
	if lower == (aa):
		url = ('https://cdn.discordapp.com/attachments/585894630009077765/590169729029636096/walldog.png')
		color = random.randint(0, 0xFFFFFF)
		msg = ('**>help:** brings up the help menu \n \n **>ping:** checks the latency to the bot in milliseconds \n \n **>bitcoin:** fetches the most recent bitcoin price from coinmarketcap \n \n **>ethereum:** fetches the most recent ethereum price from coinmarketcap \n \n **>dogecoin:** feteches the most recent dogecoin price from coinmarketcap \n \n  **>8ball:** ask walldog epic questions')
		emb = (discord.Embed(description=(msg),color=(color)))
		emb.set_author(name="help menu!", icon_url=(url))
		await message.channel.send(embed=emb)

	bb = ('>bitcoin')
	lower = str.lower(message.content)
	if lower == (bb):
		def get_latest_bitcoin_price():
			BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
			response = requests.get(BITCOIN_API_URL)
			response_json = response.json()
			s = str(response_json[0]['price_usd'])
			return str(s[0:7])
		msg = ("$" + get_latest_bitcoin_price() + " is the current bitcoin price")
		await message.channel.send(msg)

	cc = ('>8ball')
	lower = str.lower(message.content)
	if lower.startswith(cc):
		balls = json.loads(open('balls.json').read())
		msg = (random.choice(balls))
		await message.channel.send(msg)

	#turn on when vps set up

	dd = ('>ping')
	lower = str.lower(message.content)
	if lower == (dd):
		def pingtime():
			latency = ('{0}'.format(client.latency))
			return str(latency[2:5])
		msg = ('pong! latency is ' + '**' + pingtime() + 'ms**')
		await message.channel.send(msg)

	ee = ('>ethereum')
	lower = str.lower(message.content)
	if lower == (ee):
		def get_latest_ethereum_price():
			ETHEREUM_API_URL = 'https://api.coinmarketcap.com/v1/ticker/Ethereum/'
			response = requests.get(ETHEREUM_API_URL)
			response_json = response.json()
			s = str(response_json[0]['price_usd'])
			return str(s[0:7])
		msg = ("$" + get_latest_ethereum_price() + " is the current ethereum price")
		await message.channel.send(msg)

	ff = ('>dogecoin')
	lower = str.lower(message.content)
	if lower == (ff):
		def get_latest_dogecoin_price():
			DOGECOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/dogecoin/'
			response = requests.get(DOGECOIN_API_URL)
			response_json = response.json()
			s = str(response_json[0]['price_usd'])
			return str(s[0:7])
		msg = ("$" + get_latest_dogecoin_price() + " is the current dogecoin price")
		await message.channel.send(msg)

	gg = 'discord.gg/'
	if gg in message.content:
		await message.delete()

client.run(token, bot=True)
