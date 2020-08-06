from search_engine_parser import GoogleSearch, DuckDuckGoSearch, BingSearch
import os
import json
import shutil
from os import system
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import youtube_dl
import discord
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from discord.utils import get as ge
import nest_asyncio
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
import pyjokes
from datetime import datetime
import praw
import urllib.request
import requests
import datetime
from requests import get
import random
from fake_useragent import UserAgent
from tinydb import TinyDB, Query
from bs4 import BeautifulSoup

############### PYBOT #############################


client = commands.Bot(command_prefix=commands.when_mentioned_or("v!", "V!"))
client.remove_command('help')


@client.event
async def on_ready():
    # update_news.start()
    await client.change_presence(activity=discord.Game("Cs GO"))
    print("Bot is Ready. ")


@client.event
async def on_member_join(ctx):
    x = datetime.datetime.now()
    user_role = discord.utils.get(ctx.guild.roles, name="Members")
    await ctx.add_roles(user_role)
    await ctx.send(f"Hi There{ctx.mention}! You Have The Role Of {user_role}")
    text_channel = client.get_channel(699270059993858121)
    role_select = client.get_channel(670006104989761540)
    print(f"{ctx} has joined a server.")
    ment = (
        f"**Welcome to Test Server {ctx}! we hope you enjoy your stay :slight_smile:**\n\n")
    channels_1 = (
        f"**Feel Free To Come say Hi in {text_channel.mention} Also Grab Yourself a Role in {role_select.mention}**\n")
    embed = discord.Embed(

        colour=discord.Color.from_rgb(54, 57, 63),
        #description= (f'{ment} {channels_1}')
    )
    embed.add_field(name=f'{x.strftime("%D")}', value=(f'{ment} {channels_1}'))
    await client.get_channel(665224791627792385).send(embed=embed)
    print(f"{ctx} has joined the server.")


@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")
    await client.get_channel(699270007594549340).send(f"{member} has left")


@client.command()
async def joke(ctx):
    await ctx.send(f'{pyjokes.get_joke()} {ctx.author.mention} ')


@client.command()
async def add(ctx):
    input_user = ctx.message.content.replace('v!add', '').replace(' ', '')
    with open('naming.txt', 'r+') as e:
        read = e.read()
        read_to_num = int(read) + 10
        write_new_number = str(read_to_num)
    with open('naming.txt', 'w') as e:
        write = e.write(f"{write_new_number}\n")

    name_2 = "./emojis/picture" + write_new_number + ".png"
    url = f'{input_user[5::]}'
    r = requests.get(url)
    with open(name_2, 'wb') as outfile:
        outfile.write(r.content)
    db = TinyDB('db.json')
    db.insert({'name': f'e!{input_user[0:5]}', 'link': f'{name_2}'})


@client.command()
async def add_gif(ctx):
    input_user = ctx.message.content.replace('v!add_gif', '').replace(' ', '')
    with open('naming.txt', 'r+') as e:
        read = e.read()
        read_to_num = int(read) + 10
        write_new_number = str(read_to_num)
    with open('naming.txt', 'w') as e:
        write = e.write(f"{write_new_number}\n")

    name_2 = "./emojis/picture" + write_new_number + ".gif"
    url = f'{input_user[5::]}'
    print(url)
    r = requests.get(url)
    with open(name_2, 'wb') as outfile:
        outfile.write(r.content)
    db = TinyDB('db.json')
    db.insert({'name': f'e!{input_user[0:5]}', 'link': f'{name_2}'})


@client.command()
async def gn(ctx):
    if ctx.author.id == 257500867568205824:
        await ctx.send("Better luck Next Time Tijs")
    elif ctx.author.id != 265463365751668736:
        await ctx.send("Sorry you do not have permission to use this command")
    else:
        await ctx.send("Bye! Cruel World")
        await ctx.send(f'{exit()}')


@client.command()
async def java(ctx):
    await ctx.send("https://discord.gg/BEvEefy")


@client.command()
async def rn(ctx, member: discord.Member, *, name: str):
    await member.edit(nick=name)


@client.command()
async def rename(ctx, member: discord.Member, *, reason=None):
    name = ctx.author.name
    await ctx.guild.me.edit(reason=reason, nick=name)
    await ctx.send(file=discord.File("./u.gif"))
    return await ctx.guild.me.edit(reason=reason, nick="Pybot!")


@client.command()
async def pic(ctx, member: discord.Member):
    await ctx.send(f"{member.avatar_url}")


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 670017726948835350:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = None
        if payload.emoji.name == 'Cpp':
            role = discord.utils.get(guild.roles, name="C++")
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(
                lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print('done')
            else:
                print("member not found")
        else:
            print("Role Not Found")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 670017726948835350:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(
                lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print('done')
            else:
                print("member not found")
        else:
            print("Role Not Found")


@client.command()
async def help(ctx):
    author = ctx.author.mention

    embed = discord.Embed(

        colour=discord.Colour.dark_orange()
    )
    embed.set_author(name="Help")
    embed.add_field(
        name='v!java', value="discord link to java discord", inline=True)
    embed.add_field(name='v!joke', value="returns a joke", inline=True)
    embed.add_field(name='v!rn', value="renames a users nickname", inline=True)
    embed.add_field(name='v!time', value="get's the bots time", inline=True)
    embed.add_field(name='e!list', value="for list of emojis", inline=True)
    embed.add_field(
        name='s!bing', value="searches bing and returns results", inline=True)
    embed.add_field(name='s!youtube',
                    value="searches youtube and returns results", inline=True)
    embed.add_field(name='v!rename',
                    value="renames the bot temporary", inline=True)
    embed.add_field(name='v!help', value="shows this message", inline=True)
    embed.add_field(name='v!player', value="shows music command", inline=True)

    await ctx.send(author, embed=embed)


@client.command()
async def globalCovid(ctx):

    corona = requests.get('https://www.worldometers.info/coronavirus/')
    c_19 = corona.content
    soup = BeautifulSoup(c_19, 'html.parser')
    world = soup.find('span', {'style': 'color:#aaa'})
    world_recovered = soup.find('span', {'style': 'color:#8ACA2B'})
    world_deaths = soup.find_all(class_='maincounter-number')[1]
    world_mild = soup.find('span', {'style': 'color:#8080FF'})
    world_crit = soup.find('span', {'style': 'color:red '})
    world_active = soup.find(class_="number-table-main")
    world = (world.text)
    print(ctx.message.content)
    corona_api = requests.get(
        'https://coronavirus-19-api.herokuapp.com/countries').json()
    data = json.dumps(corona_api)
    data_2 = json.loads(data)
    for item in data_2:
        if "USA" in item['country']:

            print(item['cases'], item['deaths'], item['todayCases'])

    embed = discord.Embed(

        colour=discord.Colour.dark_orange()
    )
    embed.set_author(name="Global(Backup Bot)",
                     icon_url='https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png')
    embed.add_field(name="Corona Cases:", value=f"{world}", inline=True)
    embed.add_field(name="Recovered:",
                    value=f"{world_recovered.text}", inline=True)
    embed.add_field(name="Deaths:", value=f"{world_deaths.text}", inline=True)
    embed.add_field(name="Active Cases:",
                    value=f"{world_active.text}", inline=True)
    embed.add_field(name="Mild Condition:",
                    value=f"{world_mild.text}", inline=True)
    embed.add_field(name="Critical Or Serious:",
                    value=f"{world_crit.text}", inline=True)

    await ctx.send(embed=embed)


@client.command()
async def cc(ctx):
    print(ctx.message.content)
    corona_api = requests.get('https://corona.lmao.ninja/v2/countries').json()
    data = json.dumps(corona_api)
    data_2 = json.loads(data)
    input_country = ctx.message.content.replace(
        "v!cc", '').replace(' ', '').replace('_', ' ')
    states = "usa"
    britan = "uk"
    if states.lower() == str(input_country) or states.upper() == str(input_country):
        str(input_country)
        input_country = input_country.upper()
        print("yes")

    elif britan.lower() == str(input_country) or britan.upper() == str(input_country):
        str(input_country)
        input_country = input_country.upper()

    elif "Faroe islands" in input_country:
        corona_denmark = requests.get(
            'https://www.ssi.dk/aktuelt/sygdomsudbrud/coronavirus')
        my_url = corona_denmark.content
        soup = BeautifulSoup(my_url, 'html.parser')
        dk = soup.find_all("td", {"style": "text-align: right;"})
        denmark_kingdom = []
        for countries in dk:
            denmark_kingdom.append(countries.text.replace(
                '(d)', '').replace('(e)', ''))
        str(input_country)
        input_country = input_country.title()
        print(input_country)
        embed = discord.Embed(


            colour=discord.Colour.dark_orange()
        )
        embed.set_author(
            name='Faroe Islands', icon_url="http://icons.iconarchive.com/icons/wikipedia/flags/256/FO-Faroe-Islands-Flag-icon.png")
        embed.set_thumbnail(
            url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
        embed.add_field(
            name="Cases:", value=f"{denmark_kingdom[5]}", inline=True)
        embed.add_field(name="People Tested:",
                        value=f"{denmark_kingdom[4]}", inline=True)
        embed.add_field(
            name="Deaths:", value=f"{denmark_kingdom[6]}", inline=True)
        await ctx.send(embed=embed)

    else:
        str(input_country)
        input_country = input_country.title()
    print(input_country)
    try:
        for item in data_2:
            if input_country in item['country']:
                corona_denmark = requests.get(
                    'https://www.ssi.dk/aktuelt/sygdomsudbrud/coronavirus')
                my_url = corona_denmark.content
                soup = BeautifulSoup(my_url, 'html.parser')
                dk = soup.find_all("td", {"style": "text-align: right;"})
                denmark_kingdom = []
                for countries in dk:
                    denmark_kingdom.append(countries.text.replace(
                        '(d)', '').replace('(e)', ''))
                if "Denmark" in input_country:

                    print(denmark_kingdom)
                    print(denmark_kingdom[2].replace('\xa0', ''))
                    embed = discord.Embed(

                        colour=discord.Colour.dark_orange()
                    )
                    embed.set_author(
                        name=f'{item["country"]}', icon_url=f"{item['countryInfo']['flag']}")
                    embed.set_thumbnail(
                        url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
                    embed.add_field(
                        name="Cases:", value=f"{item['cases']} (+{item['todayCases']} New Cases)", inline=True)
                    embed.add_field(name="People Tested:",
                                    value=f"{denmark_kingdom[0]}", inline=True)
                    embed.add_field(
                        name='Deaths:', value=f"{item['deaths']} (+{item['todayDeaths']} New Deaths)", inline=True)
                    embed.add_field(name="Recovered:",
                                    value=f"{item['recovered']}", inline=True)
                    embed.add_field(name="Active Cases:",
                                    value=f"{item['active']}", inline=True)
                    embed.add_field(name="Critical Cases:",
                                    value=f"{item['critical']}", inline=True)
                    embed.add_field(
                        name="Case Per Million:", value=f"{item['casesPerOneMillion']}", inline=True)
                    embed.add_field(name="Test Done:",
                                    value=f"{item['tests']}", inline=True)
                    await ctx.send(embed=embed)

                elif "Greenland" in input_country:
                    embed = discord.Embed(

                        colour=discord.Colour.dark_orange()
                    )
                    embed.set_author(
                        name=f'{item["country"]}', icon_url=f"{item['countryInfo']['flag']}")
                    embed.set_thumbnail(
                        url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
                    embed.add_field(
                        name="Cases:", value=f"{item['cases']} (+{item['todayCases']} New Cases)", inline=True)
                    embed.add_field(name="People Tested:",
                                    value=f"{denmark_kingdom[8]}", inline=True)
                    embed.add_field(
                        name='Deaths:', value=f"{item['deaths']} (+{item['todayDeaths']} New Deaths)", inline=True)
                    embed.add_field(name="Recovered:",
                                    value=f"{item['recovered']}", inline=True)
                    embed.add_field(name="Active Cases:",
                                    value=f"{item['active']}", inline=True)
                    embed.add_field(name="Critical Cases:",
                                    value=f"{item['critical']}", inline=True)
                    embed.add_field(
                        name="Case Per Million:", value=f"{item['casesPerOneMillion']}", inline=True)
                    embed.add_field(name="Test Done:",
                                    value=f"{item['tests']}", inline=True)
                    await ctx.send(embed=embed)
                elif input_country == '':
                    embed = discord.Embed(

                        colour=discord.Colour.dark_orange()
                    )
                    embed.set_author(
                        name='Covid Command List', icon_url="https://s.rfi.fr/media/display/54567de6-57ee-11ea-82e4-005056bf87d6/w:1240/p:16x9/2020-02-18t205109z_1645409347_rc243f9ecyr0_rtrmadp_3_china-health.jpg")
                    embed.set_thumbnail(
                        url="https://3mg34c37ntii24dmio2yy6o5-wpengine.netdna-ssl.com/wp-content/uploads/2020/02/Screen-Shot-2020-02-26-at-2.31.27-PM-864x560.png")
                    embed.add_field(name="v!globalcovid",
                                    value="Shows Global Stats", inline=True)
                    embed.add_field(
                        name="v!cc", value="use this command to search country if country has two separate words use '_' example south_africa", inline=True)
                    embed.add_field(
                        name='v!ustate', value="search state in the USA", inline=True)
                    embed.add_field(
                        name="Pybot", value="[Add Bot](https://discordapp.com/api/oauth2/authorize?client_id=660222815038996481&permissions=8&scope=bot)      \n [Join Support Server](https://discord.gg/ZftYpzz) ", inline=False)
                    await ctx.send(embed=embed)
                    break
                elif "Sa" in input_country:
                    break

                else:

                    embed = discord.Embed(

                        colour=discord.Colour.dark_orange()
                    )
            # print(item['cases'],item['deaths'],item['todayCases'])
                    embed.set_author(
                        name=f'{item["country"]}', icon_url=f"{item['countryInfo']['flag']}")
                    embed.set_thumbnail(
                        url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
                    embed.add_field(
                        name="Cases:", value=f"{item['cases']} (+{item['todayCases']} New Cases)", inline=True)
                    embed.add_field(
                        name='Deaths:', value=f"{item['deaths']} (+{item['todayDeaths']} New Deaths)", inline=True)
                    embed.add_field(name="Recovered:",
                                    value=f"{item['recovered']}", inline=True)
                    embed.add_field(name="Active Cases:",
                                    value=f"{item['active']}", inline=True)
                    embed.add_field(name="Critical Cases:",
                                    value=f"{item['critical']}", inline=True)
                    embed.add_field(
                        name="Case Per Million:", value=f"{item['casesPerOneMillion']}", inline=True)
                    embed.add_field(name="Test Done:",
                                    value=f"{item['tests']}", inline=True)
                    print(item['tests'])
                    await ctx.send(embed=embed)
                    return
        else:
            await ctx.send("Sorry couldn't find country please try using the full name of the country.")
            return

    except Exception as e:
        print(f"whoops try again!{e}")
        # await ctx.send("Sorry couldn't find country please try using the full name of the country.")


@client.command()
async def ustate(ctx):
    print(ctx.message.content)
    corona_api_state = requests.get(
        'https://corona.lmao.ninja/v2/states').json()
    data = json.dumps(corona_api_state)
    data_2 = json.loads(data)
    input_country = ctx.message.content.replace(
        "v!ustate", '').replace(' ', '').replace('_', ' ')
    print(input_country.title())

    for item in data_2:
        try:
            if input_country.title() in item['state']:
                embed = discord.Embed(

                    colour=discord.Colour.dark_orange()
                )
                # print(item['cases'],item['deaths'],item['todayCases'])
                embed.set_author(
                    name=f'{input_country}', icon_url="https://cdn4.iconfinder.com/data/icons/healthy-life-line-color-live-long-and-prosper/512/Hand_washing-512.png")
                embed.set_thumbnail(
                    url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
                embed.add_field(
                    name="Cases:", value=f"{item['cases']} (+{item['todayCases']} New Cases)", inline=True)
                embed.add_field(
                    name='Deaths:', value=f"{item['deaths']} (+{item['todayDeaths']} New Deaths)", inline=True)
                #embed.add_field(name="Recovered:", value=f"{item['recovered']}", inline=True)
                embed.add_field(name="Active Cases:",
                                value=f"{item['active']}", inline=True)
                await ctx.send(embed=embed)

        except Exception:
            await ctx.send("whoops try again!")


@client.command()
async def sp(ctx):
    try:
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome('./chromedriver', options=options)
        my_url = "https://health.hydra.africa/#/"
        driver.get(my_url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        provinces = soup.select(".pa-0.ma-0.col.col-4")
        province_list = []
        for province in provinces:
            province_list.append(province.text.replace("remove ", ''))
        print(province_list[0])
        stats = soup.select(".pl-5.col.col-6")
        stats_list = []
        for stat in stats:
            stats_list.append(stat.text)
        print(f"Tests Done: {stats_list[4]}")
        driver.quit()
        embed = discord.Embed(

            colour=discord.Colour.dark_orange()
        )
        # print(item['cases'],item['deaths'],item['todayCases'])
        embed.set_author(
            name='South Africa', icon_url="https://cdn.countryflags.com/thumbs/south-africa/flag-400.png")
        embed.set_thumbnail(
            url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
        embed.add_field(name="Cases:", value=f"{stats_list[0]}", inline=True)
        embed.add_field(name="Recovered:",
                        value=f"{stats_list[1]}", inline=True)
        embed.add_field(name='Deaths:', value=f"{stats_list[2]}", inline=True)
        embed.add_field(name="Gauteng:",
                        value=f"{province_list[0]}", inline=True)
        embed.add_field(name="Western Cape:",
                        value=f"{province_list[1]}", inline=True)
        embed.add_field(name="KwaZulu-Natal:",
                        value=f"{province_list[2]}", inline=True)
        embed.add_field(name="Unknown:",
                        value=f"{province_list[3]}", inline=True)
        embed.add_field(name="Free State:",
                        value=f"{province_list[4]}", inline=True)
        embed.add_field(name="Eastern Cape:",
                        value=f"{province_list[5]}", inline=True)
        embed.add_field(name="Limpopo:",
                        value=f"{province_list[6]}", inline=True)
        embed.add_field(name="Mpumalanga:",
                        value=f"{province_list[7]}", inline=True)
        embed.add_field(name="Northern Cape:",
                        value=f"{province_list[8]}", inline=True)
        embed.add_field(name="North West:",
                        value=f"{province_list[9]}", inline=True)
        embed.add_field(name="Tests in SA:",
                        value=f"{stats_list[4]}", inline=True)

        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"whoops try again!{e}")


@client.command()
async def iceland(ctx):
    ua = UserAgent()
    userAgent = ua.random
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument("window-size=200,768")
    options.add_argument("--start-maximized")
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome('./chromedriver', options=options)
    my_url = "https://e.infogram.com/7327507d-28f5-4e3c-b587-c1680bd790e6?parent_url=https%3A%2F%2Fwww.covid.is%2Ftolulegar-upplysingar&amp;src=embed#async_embed"
    cookie = {'name': 'cookiehub', 'value': 'eyJhbnN3ZXJlZCI6ZmFsc2UsInByZWNvbnNlbnQiOmZhbHNlLCJkbnQiOmZhbHNlLCJjb29raWVMYXdzIjp0cnVlLCJ0b2tlbiI6IiIsImNhdGVnb3JpZXMiOlt7ImNpZCI6MSwiaWQiOiJuZWNlc3NhcnkiLCJ2YWx1ZSI6dHJ1ZX0seyJjaWQiOjMsImlkIjoiYW5hbHl0aWNzIiwidmFsdWUiOmZhbHNlfV19'}
    driver.get(my_url)
    driver.add_cookie(cookie)
    await asyncio.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    iceland_province = soup.select(".igc-table-cell-span")
    iceland_info = soup.select(".igc-textual-figure")
    iceland_prov = []
    ice_stats = []
    for prov in iceland_province:
        iceland_prov.append(prov.text)

    print(iceland_prov)
    for stat in iceland_info:
        ice_stats.append(stat.text.replace('\n', ''))

    print(ice_stats)
    try:
        embed = discord.Embed(

            colour=discord.Colour.dark_orange()
        )

        embed.set_author(
            name='Iceland', icon_url="https://cdn.countryflags.com/thumbs/iceland/flag-400.png")
        embed.set_thumbnail(
            url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
        embed.add_field(name="staðfest smit:",
                        value=f"{ice_stats[0]}", inline=True)
        embed.add_field(name="í einangrun:",
                        value=f"{ice_stats[1]}", inline=True)
        embed.add_field(name='á sjúkrahúsi:',
                        value=f"{ice_stats[2]}", inline=True)
        embed.add_field(name='á gjörgæslu:',
                        value=f"{ice_stats[3]}", inline=True)
        embed.add_field(name='batnað:', value=f"{ice_stats[4]}", inline=True)
        embed.add_field(name='í sóttkví:',
                        value=f"{ice_stats[5]}", inline=True)
        embed.add_field(name='lokið sóttkví:',
                        value=f"{ice_stats[6]}", inline=True)
        embed.add_field(name='sýni:', value=f"{ice_stats[7]}", inline=True)
        embed.add_field(name=f'Höfuðborgarsvæði:',
                        value=f"Smit: {iceland_prov[1]} Sóttkví: {iceland_prov[2]}", inline=True)
        embed.add_field(
            name=f'Suðurnes:', value=f"Smit: {iceland_prov[4]} Sóttkví: {iceland_prov[5]}", inline=True)
        embed.add_field(
            name=f'Suðurland:', value=f"Smit: {iceland_prov[7]} Sóttkví: {iceland_prov[8]}", inline=True)
        embed.add_field(
            name=f'Austurland:', value=f"Smit: {iceland_prov[10]} Sóttkví: {iceland_prov[11]}", inline=True)
        embed.add_field(name=f'Norðurland eystra:',
                        value=f"Smit: {iceland_prov[13]} Sóttkví: {iceland_prov[14]}", inline=True)
        embed.add_field(name=f'Norðurland vestra:',
                        value=f"Smit: {iceland_prov[16]} Sóttkví: {iceland_prov[17]}", inline=True)
        embed.add_field(
            name=f'Vestfirðir:', value=f"Smit: {iceland_prov[19]} Sóttkví: {iceland_prov[20]}", inline=True)
        embed.add_field(
            name=f'Vesturland:', value=f"Smit: {iceland_prov[22]} Sóttkví: {iceland_prov[23]}", inline=True)
        embed.add_field(
            name=f'Óstaðsett:', value=f"Smit: {iceland_prov[25]} Sóttkví: {iceland_prov[26]}", inline=True)
        embed.add_field(
            name=f'Útlönd:', value=f"Smit: {iceland_prov[28]} Sóttkví: {iceland_prov[29]}", inline=True)

        await ctx.send(embed=embed)
    except Exception as e:
        print(e)

    driver.quit()


@client.command()
async def cprov(ctx):
    canada_province = requests.get('https://www.covid-19canada.com/')
    my_url = canada_province.content
    soup = BeautifulSoup(my_url, 'html.parser')
    canada_provinces = []
    cp = soup.select(".status-table")
    update_time = soup.find(class_="pull-right")
    canada_provinces.append(update_time.text.replace("\nReload\n\n\n", '').replace(
        '\n', '').replace(' ', '').replace('latestUpdateat:', ''))

    for provinces in cp:
        # print(countries.text)
        canada_provinces.append(provinces.text)
    embed = discord.Embed(

        colour=discord.Colour.dark_orange()
    )
    # print(item['cases'],item['deaths'],item['todayCases'])
    embed.set_author(name=f'Canada Provinces',
                     icon_url="https://cdn.countryflags.com/thumbs/canada/flag-400.png")
    # embed.set_thumbnail(url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
    embed.add_field(name=f"Total Cases",
                    value=f"{canada_provinces[1]}", inline=True)
    embed.add_field(name=f"Total Deaths",
                    value=f"{canada_provinces[2]}", inline=True)
    embed.add_field(name=f"Total Recovered",
                    value=f"{canada_provinces[3]}", inline=True)
    embed.add_field(name=f"BC Confirmed",
                    value=f"{canada_provinces[4]}", inline=True)
    embed.add_field(name=f"BC Deaths",
                    value=f"{canada_provinces[5]}", inline=True)
    embed.add_field(name=f"BC Recovered",
                    value=f"{canada_provinces[6]}", inline=True)
    embed.add_field(name=f"ON Confirmed",
                    value=f"{canada_provinces[7]}", inline=True)
    embed.add_field(name=f"ON Deaths",
                    value=f"{canada_provinces[8]}", inline=True)
    embed.add_field(name=f"ON Recovered",
                    value=f"{canada_provinces[9]}", inline=True)
    embed.add_field(name=f"QC Confirmed",
                    value=f"{canada_provinces[10]}", inline=True)
    embed.add_field(name=f"QC Deaths",
                    value=f"{canada_provinces[11]}", inline=True)
    embed.add_field(name=f"QC Recovered",
                    value=f"{canada_provinces[12]}", inline=True)
    embed.add_field(name=f"AB Confirmed",
                    value=f"{canada_provinces[13]}", inline=True)
    embed.add_field(name=f"AB Deaths",
                    value=f"{canada_provinces[14]}", inline=True)
    embed.add_field(name=f"AB Recovered",
                    value=f"{canada_provinces[15]}", inline=True)
    embed.add_field(name=f"MB Confirmed",
                    value=f"{canada_provinces[16]}", inline=True)
    embed.add_field(name=f"MB Deaths",
                    value=f"{canada_provinces[17]}", inline=True)
    embed.add_field(name=f"MB Recovered",
                    value=f"{canada_provinces[18]}", inline=True)
    embed.add_field(name=f"NB Confirmed",
                    value=f"{canada_provinces[19]}", inline=True)
    embed.add_field(name=f"NB Deaths",
                    value=f"{canada_provinces[20]}", inline=True)
    embed.add_field(name=f"NB Recovered",
                    value=f"{canada_provinces[21]}", inline=True)
    embed.add_field(name=f"SK Confirmed",
                    value=f"{canada_provinces[22]}", inline=True)
    embed.add_field(name=f"SK Deaths",
                    value=f"{canada_provinces[23]}", inline=True)
    embed.add_field(name=f"SK Recovered",
                    value=f"{canada_provinces[24]}", inline=True)
    embed.add_field(name="Canada Source",
                    value="[Source Link of Data](https://www.covid-19canada.com/)", inline=False)
    embed.set_footer(text=f"Last Updated {canada_provinces[0]}")
    await ctx.send(embed=embed)
    embed = discord.Embed(

        colour=discord.Colour.dark_orange()
    )
    embed.add_field(name=f"PEI Confirmed",
                    value=f"{canada_provinces[25]}", inline=True)
    embed.add_field(name=f"PEI Deaths",
                    value=f"{canada_provinces[26]}", inline=True)
    embed.add_field(name=f"PEI Recovered",
                    value=f"{canada_provinces[27]}", inline=True)
    embed.add_field(name=f"NL Confirmed",
                    value=f"{canada_provinces[28]}", inline=True)
    embed.add_field(name=f"NL Deaths",
                    value=f"{canada_provinces[29]}", inline=True)
    embed.add_field(name=f"NL Recovered",
                    value=f"{canada_provinces[30]}", inline=True)
    embed.add_field(name=f"NS Confirmed",
                    value=f"{canada_provinces[31]}", inline=True)
    embed.add_field(name=f"NS Deaths",
                    value=f"{canada_provinces[32]}", inline=True)
    embed.add_field(name=f"NS Recovered",
                    value=f"{canada_provinces[33]}", inline=True)
    embed.add_field(name=f"YT Confirmed",
                    value=f"{canada_provinces[34]}", inline=True)
    embed.add_field(name=f"YT Deaths",
                    value=f"{canada_provinces[35]}", inline=True)
    embed.add_field(name=f"YT Recovered",
                    value=f"{canada_provinces[36]}", inline=True)
    embed.add_field(name=f"NT Confirmed",
                    value=f"{canada_provinces[37]}", inline=True)
    embed.add_field(name=f"NT Deaths",
                    value=f"{canada_provinces[38]}", inline=True)
    embed.add_field(name=f"NT Recovered",
                    value=f"{canada_provinces[39]}", inline=True)
    embed.add_field(name=f"NU Confirmed",
                    value=f"{canada_provinces[40]}", inline=True)
    embed.add_field(name=f"NU Deaths",
                    value=f"{canada_provinces[41]}", inline=True)
    embed.add_field(name=f"NU Recovered",
                    value=f"{canada_provinces[42]}", inline=True)
    embed.add_field(name="Canada Source",
                    value="[Source Link of Data](https://www.covid-19canada.com/)", inline=False)
    embed.set_footer(text=f"Last Updated {canada_provinces[0]}")
    await ctx.send(embed=embed)


@client.command()
async def india(ctx):
    india_province = requests.get('https://www.mohfw.gov.in/')
    my_url = india_province.content
    soup = BeautifulSoup(my_url, 'html.parser')
    ip = soup.select('td')
    india_provinces = []
    for item in ip:
        india_provinces.append(item.text.replace('\n', ''))
    embed = discord.Embed(

        colour=discord.Colour.dark_orange()
    )
    # print(item['cases'],item['deaths'],item['todayCases'])
    embed.set_author(name='India States Page 1(use v!india2 for page 2)',
                     icon_url="https://cdn.countryflags.com/thumbs/india/flag-400.png")
    # embed.set_thumbnail(url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
    embed.add_field(name="Goa Confirmed:",
                    value=f"{india_provinces[42]}", inline=True)
    embed.add_field(name="Goa Recovered:",
                    value=f"{india_provinces[43]}", inline=True)
    embed.add_field(name="Goa Deaths:",
                    value=f"{india_provinces[44]}", inline=True)
    embed.add_field(name="Gujarat Confirmed:",
                    value=f"{india_provinces[47]}", inline=True)
    embed.add_field(name="Gujarat Recovered:",
                    value=f"{india_provinces[48]}", inline=True)
    embed.add_field(name="Gujarat Deaths:",
                    value=f"{india_provinces[49]}", inline=True)
    embed.add_field(name="Haryana Confirmed:",
                    value=f"{india_provinces[52]}", inline=True)
    embed.add_field(name="Haryana Recovered:",
                    value=f"{india_provinces[53]}", inline=True)
    embed.add_field(name="Haryana Deaths:",
                    value=f"{india_provinces[54]}", inline=True)
    embed.add_field(name="Himachal Pradesh Confirmed:",
                    value=f"{india_provinces[57]}", inline=True)
    embed.add_field(name="Himachal Pradesh Recovered:",
                    value=f"{india_provinces[58]}", inline=True)
    embed.add_field(name="Himachal Pradesh Deaths:",
                    value=f"{india_provinces[59]}", inline=True)
    embed.add_field(name="Jammu and Kashmir Confirmed:",
                    value=f"{india_provinces[62]}", inline=True)
    embed.add_field(name="Jammu and Kashmir Recovered:",
                    value=f"{india_provinces[63]}", inline=True)
    embed.add_field(name="Jammu and Kashmir Deaths:",
                    value=f"{india_provinces[64]}", inline=True)
    embed.add_field(name="Jharkhand Confirmed:",
                    value=f"{india_provinces[67]}", inline=True)
    embed.add_field(name="Jharkhand Recovered:",
                    value=f"{india_provinces[68]}", inline=True)
    embed.add_field(name="Jharkhand Deaths:",
                    value=f"{india_provinces[69]}", inline=True)
    embed.add_field(name="Karnataka Confirmed:",
                    value=f"{india_provinces[72]}", inline=True)
    embed.add_field(name="Karnataka Recovered:",
                    value=f"{india_provinces[73]}", inline=True)
    embed.add_field(name="Karnataka Deaths:",
                    value=f"{india_provinces[74]}", inline=True)
    embed.add_field(name="Kerala Confirmed:",
                    value=f"{india_provinces[77]}", inline=True)
    embed.add_field(name="Kerala Recovered:",
                    value=f"{india_provinces[78]}", inline=True)
    embed.add_field(name="Kerala Deaths:",
                    value=f"{india_provinces[79]}", inline=True)

    await ctx.send(embed=embed)


@client.command()
async def india2(ctx):
    india_province = requests.get('https://www.mohfw.gov.in/')
    my_url = india_province.content
    soup = BeautifulSoup(my_url, 'html.parser')
    ip = soup.select('td')
    india_provinces = []
    for item in ip:
        india_provinces.append(item.text.replace('\n', ''))
    embed = discord.Embed(

        colour=discord.Colour.dark_orange()
    )
    # print(item['cases'],item['deaths'],item['todayCases'])
    embed.set_author(name='India States Page 2(use v!india3 for page 3)',
                     icon_url="https://cdn.countryflags.com/thumbs/india/flag-400.png")
    # embed.set_thumbnail(url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
    embed.add_field(name="Andhra Pradesh Confirmed:",
                    value=f"{india_provinces[2]}", inline=True)
    embed.add_field(name="Andhra Pradesh Recovered:",
                    value=f"{india_provinces[3]}", inline=True)
    embed.add_field(name="Andhra Deaths",
                    value=f"{india_provinces[4]}", inline=True)
    embed.add_field(name="Andaman and Nicobar Islands Confirmed:",
                    value=f"{india_provinces[7]}", inline=True)
    embed.add_field(name="Andaman and Nicobar Islands Recovered:",
                    value=f"{india_provinces[8]}", inline=True)
    embed.add_field(name="Andaman and Nicobar Islands Deaths:",
                    value=f"{india_provinces[9]}", inline=True)
    embed.add_field(name="Arunachal Pradesh Confirmed:",
                    value=f"{india_provinces[12]}", inline=True)
    embed.add_field(name="Arunachal Pradesh Recovered:",
                    value=f"{india_provinces[13]}", inline=True)
    embed.add_field(name="Arunachal Pradesh Deaths:",
                    value=f"{india_provinces[14]}", inline=True)
    embed.add_field(name="Assam Confirmed:",
                    value=f"{india_provinces[17]}", inline=True)
    embed.add_field(name="Assam Recovered:",
                    value=f"{india_provinces[18]}", inline=True)
    embed.add_field(name="Assam Deaths:",
                    value=f"{india_provinces[19]}", inline=True)
    embed.add_field(name="Bihar Confirmed:",
                    value=f"{india_provinces[22]}", inline=True)
    embed.add_field(name="Bihar Recovered:",
                    value=f"{india_provinces[23]}", inline=True)
    embed.add_field(name="Bihar Deaths:",
                    value=f"{india_provinces[24]}", inline=True)
    embed.add_field(name="Chandigarh Confirmed:",
                    value=f"{india_provinces[27]}", inline=True)
    embed.add_field(name="Chandigarh Recovered:",
                    value=f"{india_provinces[28]}", inline=True)
    embed.add_field(name="Chandigarh Deaths:",
                    value=f"{india_provinces[29]}", inline=True)
    embed.add_field(name="Chhattisgarh Confirmed:",
                    value=f"{india_provinces[32]}", inline=True)
    embed.add_field(name="Chhattisgarh Recovered:",
                    value=f"{india_provinces[33]}", inline=True)
    embed.add_field(name="Chhattisgarh Deaths:",
                    value=f"{india_provinces[34]}", inline=True)
    embed.add_field(name="Delhi Confirmed:",
                    value=f"{india_provinces[37]}", inline=True)
    embed.add_field(name="Delhi Recovered:",
                    value=f"{india_provinces[38]}", inline=True)
    embed.add_field(name="Delhi Deaths:",
                    value=f"{india_provinces[39]}", inline=True)

    await ctx.send(embed=embed)


@client.command()
async def india3(ctx):
    india_province = requests.get('https://www.mohfw.gov.in/')
    my_url = india_province.content
    soup = BeautifulSoup(my_url, 'html.parser')
    ip = soup.select('td')
    india_provinces = []
    for item in ip:
        india_provinces.append(item.text.replace('\n', ''))
    embed = discord.Embed(

        colour=discord.Colour.dark_orange()
    )
    # print(item['cases'],item['deaths'],item['todayCases'])
    embed.set_author(name='India States Page 3(use v!india4 for page 4)',
                     icon_url="https://cdn.countryflags.com/thumbs/india/flag-400.png")
    # embed.set_thumbnail(url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
    embed.add_field(name="Ladakh Confirmed:",
                    value=f"{india_provinces[82]}", inline=True)
    embed.add_field(name="Ladakh Recovered:",
                    value=f"{india_provinces[83]}", inline=True)
    embed.add_field(name="Ladakh Deaths:",
                    value=f"{india_provinces[84]}", inline=True)
    embed.add_field(name="Madhya Pradesh Confirmed:",
                    value=f"{india_provinces[87]}", inline=True)
    embed.add_field(name="Madhya Pradesh Recovered:",
                    value=f"{india_provinces[88]}", inline=True)
    embed.add_field(name="Madhya Pradesh Deaths:",
                    value=f"{india_provinces[89]}", inline=True)
    embed.add_field(name="Maharashtra Confirmed:",
                    value=f"{india_provinces[92]}", inline=True)
    embed.add_field(name="Maharashtra Recovered:",
                    value=f"{india_provinces[93]}", inline=True)
    embed.add_field(name="Maharashtra Deaths:",
                    value=f"{india_provinces[94]}", inline=True)
    embed.add_field(name="Manipur Confirmed:",
                    value=f"{india_provinces[97]}", inline=True)
    embed.add_field(name="Manipur Recovered:",
                    value=f"{india_provinces[98]}", inline=True)
    embed.add_field(name="Manipur Deaths:",
                    value=f"{india_provinces[99]}", inline=True)
    embed.add_field(name="Mizoram Confirmed:",
                    value=f"{india_provinces[102]}", inline=True)
    embed.add_field(name="Mizoram Recovered:",
                    value=f"{india_provinces[103]}", inline=True)
    embed.add_field(name="Mizoram Deaths:",
                    value=f"{india_provinces[104]}", inline=True)
    embed.add_field(name="Odisha Confirmed:",
                    value=f"{india_provinces[107]}", inline=True)
    embed.add_field(name="Odisha Recovered:",
                    value=f"{india_provinces[108]}", inline=True)
    embed.add_field(name="Odisha Deaths:",
                    value=f"{india_provinces[109]}", inline=True)
    embed.add_field(name="Puducherry Confirmed:",
                    value=f"{india_provinces[112]}", inline=True)
    embed.add_field(name="Puducherry Recovered:",
                    value=f"{india_provinces[113]}", inline=True)
    embed.add_field(name="Puducherry Deaths:",
                    value=f"{india_provinces[114]}", inline=True)
    embed.add_field(name="Punjab Confirmed:",
                    value=f"{india_provinces[117]}", inline=True)
    embed.add_field(name="Punjab Recovered:",
                    value=f"{india_provinces[118]}", inline=True)
    embed.add_field(name="Punjab Deaths:",
                    value=f"{india_provinces[119]}", inline=True)

    await ctx.send(embed=embed)


@client.command()
async def india4(ctx):
    india_province = requests.get('https://www.mohfw.gov.in/')
    my_url = india_province.content
    soup = BeautifulSoup(my_url, 'html.parser')
    ip = soup.select('td')
    india_provinces = []
    for item in ip:
        india_provinces.append(item.text.replace('\n', ''))
    embed = discord.Embed(

        colour=discord.Colour.dark_orange()
    )
    # print(item['cases'],item['deaths'],item['todayCases'])
    embed.set_author(name='India States Page 4(end of states)',
                     icon_url="https://cdn.countryflags.com/thumbs/india/flag-400.png")
    # embed.set_thumbnail(url="https://1.bp.blogspot.com/-nZlIpLZNuu4/WgTA1oyfe0I/AAAAAAAAVt8/J11C5Bt4C8gxGJJWOgTmAfmjO8o-LyfaQCLcBGAs/s1600/sick-panda.png")
    embed.add_field(name="Rajasthan Confirmed:",
                    value=f"{india_provinces[122]}", inline=True)
    embed.add_field(name="Rajasthan Recovered:",
                    value=f"{india_provinces[123]}", inline=True)
    embed.add_field(name="Rajasthan Deaths:",
                    value=f"{india_provinces[124]}", inline=True)
    embed.add_field(name="Tamil Nadu Confirmed:",
                    value=f"{india_provinces[127]}", inline=True)
    embed.add_field(name="Tamil Nadu Recovered:",
                    value=f"{india_provinces[128]}", inline=True)
    embed.add_field(name="Tamil Nadu Deaths:",
                    value=f"{india_provinces[129]}", inline=True)
    embed.add_field(name="Telengana Confirmed:",
                    value=f"{india_provinces[132]}", inline=True)
    embed.add_field(name="Telengana Recovered:",
                    value=f"{india_provinces[133]}", inline=True)
    embed.add_field(name="Telengana Deaths:",
                    value=f"{india_provinces[134]}", inline=True)
    embed.add_field(name="Tripura Confirmed:",
                    value=f"{india_provinces[137]}", inline=True)
    embed.add_field(name="Tripura Recovered:",
                    value=f"{india_provinces[138]}", inline=True)
    embed.add_field(name="Tripura Deaths:",
                    value=f"{india_provinces[139]}", inline=True)
    embed.add_field(name="Uttarakhand Confirmed:",
                    value=f"{india_provinces[142]}", inline=True)
    embed.add_field(name="Uttarakhand Recovered:",
                    value=f"{india_provinces[143]}", inline=True)
    embed.add_field(name="Uttarakhand Deaths:",
                    value=f"{india_provinces[144]}", inline=True)
    embed.add_field(name="Uttar Pradesh Confirmed:",
                    value=f"{india_provinces[147]}", inline=True)
    embed.add_field(name="Uttar Pradesh Recovered:",
                    value=f"{india_provinces[148]}", inline=True)
    embed.add_field(name="Uttar Pradesh Deaths:",
                    value=f"{india_provinces[149]}", inline=True)
    embed.add_field(name="UWest Bengal Confirmed:",
                    value=f"{india_provinces[152]}", inline=True)
    embed.add_field(name="UWest Bengal Recovered:",
                    value=f"{india_provinces[153]}", inline=True)
    embed.add_field(name="UWest Bengal Deaths:",
                    value=f"{india_provinces[154]}", inline=True)

    await ctx.send(embed=embed)


@client.command()
async def invite(ctx):
    await ctx.send('https://discord.gg/ZftYpzz')


@client.command()
async def servercheck(ctx):
    print(str(len(client.guilds)))
# we need this package otherwise we will get a "RuntimeError: This event loop is already running" error
nest_asyncio.apply()


client.run('Token Here')
