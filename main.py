import discord, config, asyncio
import bot_tools as tools
from discord.ext import commands
# from aiohttp import connector

intents = discord.Intents.default()
intents.message_content = True # required for on_message event
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

def is_me(m):
    return m.author == bot.user

@bot.command() 
async def delete(ctx): # delete previous message
    await ctx.channel.purge(limit=50, check=is_me)

@bot.command()
async def help(ctx): # how to use bot
     await ctx.send("Use your links as normal. This bot works with links from\n "+\
                    "1. tiktok.com\n" + \
                    "2. instagram.com\n" + \
                    "3. x.com\n" + \
                    "4. twitter.com\n" + \
                    "5. pixiv.com\n" + \
                    "They can be embedded among text in the message or be its own message." + \
                    "\n**If you need to delete a message from the bot, type !delete to get rid of the last message "+ \
                    "from the bot. Right now the bot doesn't recognize a hidden link using <> as one that you "+ \
                    "don't want it to repost, so use !delete instead.**")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    # ignore bot's messages
    if message.author == bot.user:
        return
    
    if 'https://twitter.com' in message.content:
        await message.edit(suppress=True)
        await asyncio.sleep(2)
        await message.edit(suppress=True)
        ind = tools.find_url_index('https://twitter.com', message.content)
        urls = tools.get_urls(message.content, ind)
        urls = tools.change_to_vx('https://twitter.com', urls, 'twt')
        if len(urls) != 0: await message.channel.send(tools.join_urls(urls))

    if 'https://x.com' in message.content:
        await message.edit(suppress=True)
        await asyncio.sleep(2)
        await message.edit(suppress=True)
        ind = tools.find_url_index('https://x.com', message.content)
        urls = tools.get_urls(message.content, ind)
        urls = tools.change_to_vx('https://x.com', urls, 'twt')
        if len(urls) != 0: await message.channel.send(tools.join_urls(urls))

    if 'https://www.tiktok.com' in message.content:
        await message.edit(suppress=True)
        await asyncio.sleep(2)
        await message.edit(suppress=True)
        ind = tools.find_url_index('https://www.tiktok.com', message.content)
        urls = tools.get_urls(message.content, ind)
        urls = tools.change_to_vx('https://www.tiktok.com', urls, 'tt')
        if len(urls) != 0: await message.channel.send(tools.join_urls(urls))

    # if 'https://www.instagram.com' in message.content:
    #     await message.edit(suppress=True)
    #     ind = tools.find_url_index('https://www.instagram.com', message.content)
    #     urls = tools.get_urls(message.content, ind)
    #     urls = tools.change_to_vx('https://www.instagram.com', urls, 'ig')
    #     if len(urls) != 0: await message.channel.send(tools.join_urls(urls))

    if 'https://www.pixiv.net' in message.content:
        await message.edit(suppress=True)
        await asyncio.sleep(2)
        await message.edit(suppress=True)
        ind = tools.find_url_index('https://www.pixiv.net', message.content)
        urls = tools.get_urls(message.content, ind)
        urls = tools.change_to_vx('https://www.pixiv.net', urls, 'px')
        if len(urls) != 0: await message.channel.send(tools.join_urls(urls))
        
    await bot.process_commands(message)

# try:
#     client.run(config.dsc_token)
# except connector.ClientConnectorError:
#     pass

bot.run(config.dsc_token)


