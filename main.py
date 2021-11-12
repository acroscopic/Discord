import discord
import asyncio
import requests
import random
import sys
import time
import os
import string
import json
from discord.ext import commands
from datetime import datetime
import pandas as pd

token = open("token.txt", "r").read().strip().replace("\n", "") # reads the discord bot token through a file named token.txt
client = discord.Client()

#wallcat ready
@client.event
async def on_ready():
	game = discord.Game("in the wall")
	await client.change_presence(status=discord.Status.dnd, activity=game)
	print('logged in as wallcat')
	print('--------------------')

#chat commands
@client.event
async def on_message(message):

	if message.author == client.user: #bot ignores its own messages
		return

	def get_crypto_price(symbol):
	    api_key = open("api_key.txt", "r").read().strip().replace("\n", "") # Read the api key from api_key.txt
	    api_url = f'https://cloud.iexapis.com/stable/crypto/{symbol}/price?token={api_key}'
	    raw = requests.get(api_url).json()
	    price = raw['price']
	    return float(price)

	btc  = get_crypto_price('btcusd')
	eth  = get_crypto_price('ethusd')
	doge = get_crypto_price('dogeusdt')
	shib = get_crypto_price('shibusdt')
	ada  = get_crypto_price('adausdt')
	sol  = get_crypto_price('solusdt')
	xrp  = get_crypto_price('xrpusdt')
	dot  = get_crypto_price('dotusdt')
	algo = get_crypto_price('algousdt')
	link = get_crypto_price('linkusdt')


	if str.lower(message.content) == ('>btc'):
		msg = ('Current price of 1 Bitcoin: {} USD'.format(btc))
		await message.channel.send(msg)

	if str.lower(message.content) == ('>eth'):
		msg = ('Current price of 1 Ethereum: {} USD'.format(eth))
		await message.channel.send(msg)

	if str.lower(message.content) == ('>doge'):
		msg = ('Current price of 1 Dogecoin: {} USD'.format(doge))
		await message.channel.send(msg)

	if str.lower(message.content) == ('>shib'):
		msg = ('Current price of 1 Shib: {} USD'.format(shib))
		await message.channel.send(msg)

	if str.lower(message.content) == ('>ada'):
		msg = ('Current price of 1 Ada: {} USD'.format(ada))
		await message.channel.send(msg)

	if str.lower(message.content) == ('>sol'):
		msg = ('Current price of 1 Sol: {} USD'.format(sol))
		await message.channel.send(msg)

	if str.lower(message.content) == ('>xrp'):
		msg = ('Current price of 1 XRP: {} USD'.format(xrp))
		await message.channel.send(msg)

	if str.lower(message.content) == ('>dot'):
		msg = ('Current price of 1 Polkadot: {} USD'.format(dot))
		await message.channel.send(msg)

	if str.lower(message.content) == ('>algo'):
		msg = ('Current price of 1 Algorand: {} USD'.format(algo))
		await message.channel.send(msg)

	if str.lower(message.content) == ('>link'):
		msg = ('Current price of 1 Chainlink: {} USD'.format(link))
		await message.channel.send(msg)


	aa = ('>help')
	lower = str.lower(message.content)
	if lower == (aa):
		url = ('https://i.imgur.com/6dIcxvW.jpg') # picture of walldog
		color = random.randint(0, 0xFFFFFF)

		msg = (
			"""**>help:** brings up the help menu 
		\n **>btc**:  Outputs current Bitcoin price
		\n **>eth**:  Outputs current Ethereum price
		\n **>doge**: Outputs current Dogecoin price
		\n **>shib**: Outputs current Shiba Inu price
		\n **>ada**:  Outputs current Cardano price 
		\n **>sol**:  Outputs current Solana price 
		\n **>xrp**:  Outputs current Ripple price
		\n **>dot**:  Outputs current Polkadot price
		\n **>algo**: Outputs current Algorand price
		\n **>link**: Outputs current Chainlink price"""
		)

		emb = (discord.Embed(description=(msg),color=(color)))
		emb.set_author(name="help menu!", icon_url=(url))
		await message.channel.send(embed=emb)


	if 'discord.gg/' in message.content: # deletes invite links
		await message.delete()

client.run(token, bot=True)