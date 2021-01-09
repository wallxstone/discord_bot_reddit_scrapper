import discord
import os
import requests
import random
from keep_alive import keep_alive
from scrapper import top_post, newPost, hotpost

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    # returns a random top 10 post from given subreddit
    if msg.startswith('$t'):
        req = msg.split('$t ', 1)[1]
        post = top_post(req)
        await message.channel.send(post)

    # returns a random new post from  10 new posts from the given subreddit
    if msg.startswith('$n'):
        req = msg.split('$n', 1)[1]
        post = newPost(req)
        await message.channel.send(post)

    # returns a random hot post from 10 hot posts from the given subreddit
    if msg.startswith('$h'):
        req = msg.split('$h ', 1)[1]
        post = hotpost(req)
        await message.channel.send(post)

keep_alive()
client.run(os.getenv(''))
