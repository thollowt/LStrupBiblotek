from doctest import debug_script
from telnetlib import DM
from turtle import title
from unittest import result
from urllib import response
from pygelbooru import Gelbooru
from unicodedata import name
import hmtai
from cv2 import sort
from dis import disco
from AnilistPython import Anilist
import sys
from discord.ext import commands
import string
import discord
from cryptography.fernet import Fernet
from matplotlib.pyplot import get
from googletrans import Translator
import requests
import shodan
import os
import math
from bs4 import BeautifulSoup
import random
import asyncio
import pprint
import ffmpeg
import youtube_dl


anilist = Anilist()
key = b'PuyMXLRTgTzJZ3Zrx-Z9eKT2LJE2XLSoIJhd47R2Gqs='

intent = discord.Intents.default()
intent.members = True

intent.messages = True

token = 'OTcwNTc4MDk3OTQwMzY1MzEy.Ym9_Sw.t09Oj4snNOJi0ulzUQexTLhXxOI'

bot = commands.Bot(command_prefix='-', intents=intent)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    

#Mention user in dm on join
@bot.event
async def on_member_join(member):
    #Mention user
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.mention}, welcome to the server!')

#Search urbandictionary
@bot.command()
async def ud(ctx, *, search):
    url = 'http://api.urbandictionary.com/v0/define?term=' + search
    response = requests.get(url).json()
    embed = discord.Embed(title="Urban Dictonary", description="", color=0x00ff00)
    embed.add_field(name="Word", value=response['list'][0]['word'], inline=True)
    embed.add_field(name="Definition", value=response['list'][0]['definition'], inline=True)
    embed.add_field(name="Example", value=response['list'][0]['example'], inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def anime(ctx, *, search):
    """
    {'name_romaji': 'Owari no Seraph', 'name_english': 'Seraph of the End: Vampire Reign', 'starting_time': '4/4/2015', 'ending_time': '6/20/2015', 'cover_image': 'https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx20829-tFFjDs6qqPfL.png', 'banner_image': 'https://s4.anilist.co/file/anilistcdn/media/anime/banner/20829-1BRrVJAxlEKT.jpg', 'airing_format': 'TV', 'airing_status': 'FINISHED', 'airing_episodes': 12, 'season': 'SPRING', 'desc': 'The story takes place in a world where an unknown virus has killed the entire human population except for children under 13. Those children were then enslaved by vampires. The manga centers on Yuichiro Hyakuya, a human who dreams of becoming strong enough to kill all vampires.<br>\n<br>\n(Source: Anime News Network)', 'average_score': 73, 'genres': ['Action', 'Drama', 'Fantasy', 'Mystery', 'Supernatural'], 'next_airing_ep': None}
    """
    #If anime dosent exist respond with error
    try:
        anime = anilist.get_anime(search)
        #Make modified search string with - instead of spaces
        searchPir = search.replace(' ', '-')
        animeID = anilist.get_anime_id(search)
        embed = discord.Embed(title="Anime Information", description="", color=0x00ff00)
        embed.add_field(name="Romanji Title:", value=anime['name_romaji'], inline=True)
        embed.add_field(name="English Title:", value=anime['name_english'], inline=True)
        embed.add_field(name="Starting Date:", value=anime['starting_time'], inline=True)
        embed.add_field(name="Airing:", value=anime['airing_status'], inline=True)
        embed.add_field(name="Episodes:", value=anime['airing_episodes'], inline=True)
        #Format genre list
        genre_list = ""
        for genre in anime['genres']:
            genre_list += genre + ", "
        embed.add_field(name="Genres:", value=genre_list, inline=True)

        embed.add_field(name="Average Score:", value=anime['average_score'], inline=True)
        description = anime['desc']
        description = description.replace('<br>', '\n')
        description = description.replace('<i>', '*')
        description = description.replace('</i>', '*')
        description = description.replace('<b>', '**')
        description = description.replace('</b>', '**')
        description = description.replace('<br/>', '\n')
        embed.set_footer(text=description)
        embed.add_field(name="Link:", value="https://anilist.co/anime/" + str(animeID), inline=True)
        embed.add_field(name="(WIP)Watch here:", value="https://gogoanime.sk/category/" + str(searchPir), inline=True)
        embed.set_thumbnail(url=anime['cover_image'])
        embed.set_image(url=anime['banner_image'])
        await ctx.send(embed=embed)
    except:
        await ctx.send("Anime not found")





@bot.command()
async def startTerm(ctx):
    while True:
        x = input("Enter a message: ")
        if x == "ip":
            ip = input("Enter the IP address of the server: ")
            response = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=a6ee9b65681b4b72b951011c53cb41fd&ip={}'.format(ip))
            dataGoBrr = response.json()
            #make embed for ip
            embed = discord.Embed(title="IP Information", description="", color=0x00ff00)
            embed.add_field(name="IP", value=dataGoBrr['ip'], inline=True)
            embed.add_field(name="Country", value=dataGoBrr['country_name'], inline=True)
            embed.add_field(name="City", value=dataGoBrr['city'], inline=True)
            embed.add_field(name="Latitude", value=dataGoBrr['latitude'], inline=True)
            embed.add_field(name="Longitude", value=dataGoBrr['longitude'], inline=True)
            embed.add_field(name="Zipcode", value=dataGoBrr['zipcode'], inline=True)
            #timezone has subfields
            embed.add_field(name="Timezone", value=dataGoBrr['time_zone']['name'], inline=True)
            embed.add_field(name="ISP", value=dataGoBrr['isp'], inline=True)
            embed.add_field(name="Organization", value=dataGoBrr['organization'], inline=True)
            embed.add_field(name="Current Time", value=dataGoBrr['time_zone']['current_time'], inline=True)
            await ctx.send(embed=embed)
        elif x == "exit":
            break
        elif x == "purge":
            await ctx.channel.purge(limit=100)
        else:
            await ctx.send(x)

@bot.command()
async def test(ctx):
    await ctx.send('test')

@bot.command()
async def encrypt(ctx, message):
    encrypt = Fernet(key)
    encrypted = encrypt.encrypt(message.encode())
    await ctx.send(encrypted)


@bot.command()
async def decrypt(ctx, encrypted):
    decrypt = Fernet(key)
    decrypted = decrypt.decrypt(encrypted.encode())
    await ctx.send(decrypted)


#Purge chat
@bot.command()
@commands.has_role('Cooolio')
async def purge(ctx, amount):
    await ctx.channel.purge(limit=int(amount))



#Make a random message using binary numbers
@bot.command()
async def binary(ctx, amount):
    binary = ""
    for x in range(int(amount)):
        binary += str(random.randint(0, 1))
    await ctx.send(binary)



#Send a hug using https://some-random-api.ml/animu/hug
@bot.command()
async def hug(ctx, user):
    response = requests.get('https://some-random-api.ml/animu/hug')
    data = response.json()
    embed = discord.Embed(title="Hug", description="", color=0x00ff00)
    #add embed with mention
    embed.add_field(name="Hugged:", value=user, inline=True)
    embed.set_image(url=data['link'])
    await ctx.send(embed=embed)


#Pat a user using https://some-random-api.ml/animu/pat
@bot.command()
async def pat(ctx, user):
    response = requests.get('https://some-random-api.ml/animu/pat')
    data = response.json()
    embed = discord.Embed(title="Pat", description="", color=0x00ff00)
    #add embed with mention
    embed.add_field(name="Pat:", value=user, inline=True)
    embed.set_image(url=data['link'])
    await ctx.send(embed=embed)

@bot.command()
async def lyrics(ctx, song):
    response = requests.get('https://some-random-api.ml/lyrics?title=' + song)
    data = response.json()
    embed = discord.Embed(title="Lyrics", description="", color=0x00ff00)
    #Strip to 1024
    lyrics = data['lyrics'][:1024]
    embed.add_field(name="Lyrics:", value=lyrics, inline=True)
    await ctx.send(embed=embed)

#Fighting game between two users
@bot.command()
async def fight(ctx, user1, user2):
    #get users
    user1 = ctx.guild.get_member(int(user1.replace("<@", "").replace(">", "")))
    user2 = ctx.guild.get_member(int(user2.replace("<@", "").replace(">", "")))
    #get hp
    hp1 = random.randint(1, 100)
    hp2 = random.randint(1, 100)
    #get damage
    d1 = random.randint(1, 100)
    d2 = random.randint(1, 100)
    #get speed
    s1 = random.randint(1, 100)
    s2 = random.randint(1, 100)
    #get attack type
    at1 = random.randint(1, 2)
    at2 = random.randint(1, 2)
    #get attack name
    if at1 == 1:
        at1 = "Slap"
    else:
        at1 = "Punch"
    if at2 == 1:
        at2 = "Slap"
    else:
        at2 = "Punch"
    #make embed
    embed = discord.Embed(title="Fight", description="", color=0x00ff00)
    embed.add_field(name="Player 1", value="HP: " + str(hp1) + "\nDamage: " + str(d1) + "\nSpeed: " + str(s1) + "\nAttack: " + at1, inline=True)
    embed.add_field(name="Player 2", value="HP: " + str(hp2) + "\nDamage: " + str(d2) + "\nSpeed: " + str(s2) + "\nAttack: " + at2, inline=True)
    await ctx.send(embed=embed)
    #while both hp are above 0
    while hp1 > 0 and hp2 > 0:
        if s1 > s2:
            hp2 -= d1
            s2 += random.randint(1, 100)
        elif s2 > s1:
            hp1 -= d2
            s1 += random.randint(1, 100)
        else:
            hp1 -= d2
            hp2 -= d1
            s1 += random.randint(1, 100)
            s2 += random.randint(1, 100)
        embed = discord.Embed(title="Fight", description="", color=0x00ff00)
        embed.add_field(name="Player 1", value="HP: " + str(hp1) + "\nDamage: " + str(d1) + "\nSpeed: " + str(s1) + "\nAttack: " + at1, inline=True)
        embed.add_field(name="Player 2", value="HP: " + str(hp2) + "\nDamage: " + str(d2) + "\nSpeed: " + str(s2) + "\nAttack: " + at2, inline=True)
        await ctx.send(embed=embed)
    #if player 1 wins
    if hp1 <= 0:
        await ctx.send(user2.mention + " wins!")
        await ctx.send(user1.mention + " lost!")
    #if player 2 wins
    elif hp2 <= 0:
        await ctx.send(user1.mention + " wins!")
        await ctx.send(user2.mention + " lost!")
    #if tie
    else:
        await ctx.send("It's a tie!")


#Send a user avatar
@bot.command()
async def avatar(ctx, user):
    user = ctx.guild.get_member(int(user.replace("<@", "").replace(">", "")))
    await ctx.send(user.avatar_url)


#Rainbow overlay on user
@bot.command()
async def gayify(ctx, user):
    #Fetch user and get avatar
    user = ctx.guild.get_member(int(user.replace("<@", "").replace(">", "")))
    pfpUrl = str(user.avatar_url)
    #Strip .wepb extension
    avatarF = pfpUrl.replace(".webp", ".png")
    resp = requests.get('https://some-random-api.ml/canvas/gay?avatar='+avatarF)
    if resp.status_code == 200:
        open('gayify.png', 'wb').write(resp.content)
        await ctx.send(file=discord.File('gayify.png'))
    elif resp.status_code != 200:
        await ctx.send("Error: " + str(resp.status_code))


@bot.command()
async def com(ctx, user):
    #https://some-random-api.ml/canvas/comrade?avatar=
    #Fetch user and get avatar
    user = ctx.guild.get_member(int(user.replace("<@", "").replace(">", "")))
    pfpUrl = str(user.avatar_url)
    #Strip .wepb extension
    avatarF = pfpUrl.replace(".webp", ".png")
    resp = requests.get('https://some-random-api.ml/canvas/comrade?avatar='+avatarF)
    if resp.status_code == 200:
        open('comm.png', 'wb').write(resp.content)
        await ctx.send(file=discord.File('comm.png'))
    elif resp.status_code != 200:
        await ctx.send("Error: " + str(resp.status_code))


#https://some-random-api.ml/canvas/triggered?avatar=
@bot.command()
async def mad(ctx, user):
    #Fetch user and get avatar
    user = ctx.guild.get_member(int(user.replace("<@", "").replace(">", "")))
    pfpUrl = str(user.avatar_url)
    #Strip .wepb extension
    avatarF = pfpUrl.replace(".webp", ".png")
    resp = requests.get('https://some-random-api.ml/canvas/triggered?avatar='+avatarF)
    if resp.status_code == 200:
        open('trig.gif', 'wb').write(resp.content)
        await ctx.send(file=discord.File('trig.gif'))
    elif resp.status_code != 200:
        await ctx.send("Error: " + str(resp.status_code))

#Use this https://some-random-api.ml/img/pikachu to send a pic
@bot.command()
async def suprise(ctx):
    resp = requests.get('https://some-random-api.ml/img/pikachu')
    data = resp.json()
    #make embed
    embed = discord.Embed(title="Suprise", description="", color=0x00ff00)
    embed.set_image(url=data['link'])
    await ctx.send(embed=embed)




#Make a jail overlay using 'https://some-random-api.ml/canvas/jail?avatar=
@bot.command()
async def jail(ctx, user):
    #Fetch user and get avatar
    user = ctx.guild.get_member(int(user.replace("<@", "").replace(">", "")))
    pfpUrl = str(user.avatar_url)
    #Strip .wepb extension
    avatarF = pfpUrl.replace(".webp", ".png")
    resp = requests.get('https://some-random-api.ml/canvas/jail?avatar='+avatarF)
    if resp.status_code == 200:
        open('jail.png', 'wb').write(resp.content)
        await ctx.send(file=discord.File('jail.png'))
    elif resp.status_code != 200:
        await ctx.send("Error: " + str(resp.status_code))


@bot.command()
async def news(ctx, country):
    #If country not exist
    country_codes = ['se','ar','au', 'at', 'hk', 'jp', 'no', 'de', 'nl', 'us', 'uk', 'ua', 'ru']
    if country not in country_codes:
        await ctx.send("Country not found") 
    apiKey = '738b9667b32f43f58b107a63e53e4dc8'
    #If country is not specified, default to US
    if country == "":
        country = "us"
    
    #Use this api for the war https://newsapi.org/v2/top-headlines?country=ua&apiKey=
    resp = requests.get('https://newsapi.org/v2/top-headlines?country='+country+'&apiKey='+apiKey)
    data = resp.json()
    #make embed
    ran = random.randint(0, len(data['articles'])-1)
    embed = discord.Embed(title="War", description="", color=0x00ff00)
    embed.add_field(name="News", value=data['articles'][ran]['url'], inline=False)
    embed.add_field(name="News", value=data['articles'][ran]['title'], inline=False)
    embed.set_image(url=data['articles'][ran]['urlToImage'])
    await ctx.send(embed=embed)





#Make a magic 8ball
@bot.command()
async def eightball(ctx, *, question):
    responses = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes, definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don\'t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful'
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')




#Lewd stuff ig
@bot.command()
async def lewd(ctx):
    channel = discord.utils.get(bot.get_all_channels(), name='nsfw')

    listOfImgs = ['ass', 'bdsm', 'blowjob', 'cuckold', 'cum', 'ero', 'femdom', 'foot', 'gangbang', 'glasses', 'hentai', 'hnt_gifs', 'jahy', 'manga', 'masturbation', 'mW', 'nsfwMW', 'nsfwNeko', 'orgy', 'panties', 'pussy', 'sfwNeko', 'tentacles', 'thighs', 'uniform', 'wallpaper', 'yuri', 'zerRyo']
    randomImg = random.choice(listOfImgs)
    genImg = hmtai.useHM('2', randomImg)
    await ctx.send("You dirty bastard")
    await channel.send(genImg)



#Make a restart command for the bot
@bot.command()
async def restart(ctx):
    await ctx.send("Restarting...")
    os.execl(sys.executable, sys.executable, *sys.argv)









#Use a cool api to get a random image
@bot.command()
async def cat(ctx):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    embed = discord.Embed(title="Random Image", description="", color=0x00ff00)
    embed.set_image(url=data[0]['url'])
    await ctx.send(embed=embed)


#mute user from text channel
@bot.command()
@commands.has_role('Cooolio')
async def mute(ctx, member: discord.Member, *, reason=None):
    await member.add_roles(ctx.message.guild.get_role(970617916284362754), reason=reason)
    await ctx.send(f"{member} has been muted for {reason}")

#unmute user from text channel
@bot.command()
@commands.has_role('Cooolio')
async def unmute(ctx, member: discord.Member, *, reason=None):
    await member.remove_roles(ctx.message.guild.get_role(970617916284362754), reason=reason)
    await ctx.send(f"{member} has been unmuted for {reason}")


@bot.command()
@commands.has_role('Cooolio')
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(title="User Information", description="", color=0x00ff00)
    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    #Account creation date
    embed.add_field(name="Account Created", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
    embed.add_field(name="Nickname", value=member.nick, inline=True)
    embed.add_field(name="Status", value=member.status, inline=True)
    embed.add_field(name="Joined", value=member.joined_at, inline=True)
    embed.add_field(name="Roles", value=member.roles, inline=True)
    await ctx.send(embed=embed)


#Make a channel that logs all edited and deleted messages
@bot.command()
@commands.has_role('Cooolio')
async def makelogs(ctx):
    #Creat channel if it doesn't exist
    
    if not discord.utils.get(bot.get_all_channels(),name='logs'):
        await ctx.guild.create_text_channel('logs')
        await ctx.send('Succesfully made log channel!')

    else:
        await ctx.send('Channel already exists')
    
    #Add the role to the channel
    #make read only
    channel = discord.utils.get(bot.get_all_channels(), name='logs')
    overwrite = discord.PermissionOverwrite()
    overwrite.read_messages = True
    overwrite.send_messages = False
    overwrite.read_message_history = True
    #apply overwrites
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    #dm channel id
    channel_id = channel.id
    await channel.send('This is the log channel')





#Make dad joke generator
@bot.command()
async def dad(ctx):
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()
    #make embed for dad
    embed = discord.Embed(description="", color=0x00ff00)
    embed.add_field(name="Dad Joke", value=data['joke'], inline=True)
    await ctx.send(embed=embed)





@bot.event
async def on_message_edit(before, after):
    channel = discord.utils.get(bot.get_all_channels(), name='logs')
    embed = discord.Embed(title="Message Edited", description="", color=0x00ff00)
    #edited by
    embed.add_field(name="Edited By", value=before.author.mention, inline=True)
    embed.add_field(name="Before", value=before.content, inline=True)
    embed.add_field(name="After", value=after.content, inline=True)
    await channel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    channel = discord.utils.get(bot.get_all_channels(), name='logs')
    embed = discord.Embed(title="Message Deleted", description="", color=0x00ff00)
    #message deleted by
    embed.add_field(name="Deleted By", value=message.author.mention, inline=True)
    embed.add_field(name="Message", value=message.content, inline=True)
    await channel.send(embed=embed)

#Join voice channel
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()






#Leave voice channel
@bot.command()
async def leave(ctx):
    channel = ctx.author.voice.channel
    await channel.disconnect()


#Make gambmle game
@bot.command()
#Make slots game
@commands.has_role('Cooolio')
async def slots(ctx):
    #make slots game
    embed = discord.Embed(title="Slots", description="", color=0x00ff00)
    embed.add_field(name="Slot 1", value=random.choice(['🍎', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🍒', '🍑', '🍍']), inline=True)
    embed.add_field(name="Slot 2", value=random.choice(['🍎', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🍒', '🍑', '🍍']), inline=True)
    embed.add_field(name="Slot 3", value=random.choice(['🍎', '🍊', '🍋', '🍌', '🍉', '🍇', '🍓', '🍒', '🍑', '🍍']), inline=True)
    await ctx.send(embed=embed)




@bot.command()
async def ip(ctx, ip):
    #ip = input("Enter the IP address of the server: ")
    response = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=a6ee9b65681b4b72b951011c53cb41fd&ip={}'.format(ip))
    dataGoBrr = response.json()
    #make embed for ip
    embed = discord.Embed(title="IP Information", description="", color=0x00ff00)
    embed.add_field(name="IP", value=dataGoBrr['ip'], inline=True)
    embed.add_field(name="Country", value=dataGoBrr['country_name'], inline=True)
    embed.add_field(name="City", value=dataGoBrr['city'], inline=True)
    embed.add_field(name="Latitude", value=dataGoBrr['latitude'], inline=True)
    embed.add_field(name="Longitude", value=dataGoBrr['longitude'], inline=True)
    embed.add_field(name="Zipcode", value=dataGoBrr['zipcode'], inline=True)
    #timezone has subfields
    embed.add_field(name="Timezone", value=dataGoBrr['time_zone']['name'], inline=True)
    embed.add_field(name="ISP", value=dataGoBrr['isp'], inline=True)
    embed.add_field(name="Organization", value=dataGoBrr['organization'], inline=True)
    embed.add_field(name="Current Time", value=dataGoBrr['time_zone']['current_time'], inline=True)
    await ctx.send(embed=embed)



@bot.command()
async def howto(ctx):
    embed = discord.Embed(title='Help', description='Help for the bot', color=0x00ff00)
    embed.add_field(name='!test', value='test command', inline=False)
    embed.add_field(name='!encrypt <message>', value='encrypts a message', inline=False)
    embed.add_field(name='!decrypt <encrypted message>', value='decrypts an encrypted message (Remove b and colon)', inline=False)
    embed.add_field(name='!ip <ip>', value='gets the ip information', inline=False)
    embed.add_field(name='!howto', value='shows this message', inline=False)
    await ctx.send(embed=embed)





bot.run(token)