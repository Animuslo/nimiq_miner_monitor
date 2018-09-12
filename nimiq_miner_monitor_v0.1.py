#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version 0.1

import requests
import discord
from discord.ext import commands
import datetime
import asyncio
import pytz
from termcolor import colored, cprint


'''Initial set-up done through console '''

cprint('Welcome to the initial set-up!','green',attrs=['underline', 'bold'])
discord_token = str(input('\n Please provide token for discord: '))
bot_prefix = str(input('\n-->Please provide prefix you would like to have bot listening to:'))
print(f'You selected: {bot_prefix} as a command ')
welcome_channel = str(input('\n-->Copy and paste the channel ID (number) of one of your channels on discord:'))  # <--- Insert the channel ID to where you want to receive updates on miners
print(f'Channel id where further instructions will be sent:{welcome_channel}\n'
      f'Next copy and paste the wallet in format XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXXX')
wallet_address = str(input('Wallet address:'))
print(f'You have entered wallet address: {wallet_address}')
cprint(f'Setup has completed. Use{bot_prefix}help on your own discord for available commands','green', attrs=['underline', 'bold'])

offline_status = 'offline'  # Offline status to be compared to the miners JSON value

bot = commands.Bot(command_prefix=f'{bot_prefix}')  # <-- Prefix for the bot which can be changed
bot.remove_command('help')  # removing the old help command

'''SIMPLE ON READY CHECK AND INFO MESSAGE FOR USER'''


@bot.event
async def on_ready():
    print('Data has been successfully obtained: please use further Discord for actions')
    print(f'bot logged in as {bot.user.name} with id {bot.user.id}')
    cprint('+'*100, 'green', attrs=['bold'])
    welcome_message_channel = bot.get_channel(id=welcome_channel)
    welcome_embed = discord.Embed(colour= discord.Colour.dark_orange())
    welcome_embed.add_field(name='Welcome Miner', value=f'I am glad I can be of an-assistance to you. In order for you '
                                                        f'to get help at anytime on my commands please use ***{bot_prefix}'
                                                        f'help*** and I will get back to you ASAP.\nMost of the commands '
                                                        f'available are done with the loops'
                                                        f' so you just need to turn them on on the channels of your choice.'
                                                        f' I also need read and write permissions in order for me to be'
                                                        f' your buttler :). You can find me also on GitHub: https://github.com/Animuslo/'
                                                        f'butler_for_miners.git', inline=False)
    welcome_embed.add_field(name='Available commands', value=f'Help: {bot_prefix}help'
                                                                     f'', inline=False)
    welcome_embed.set_footer(text='For additional information you can contact @Animus#4608 through Sushipool community\n'
                                  'or send an e-mail to: MissionMoon@rocketship.com ')

    await bot.send_message(welcome_message_channel,embed=welcome_embed)


'''Designing json from wallet input for nimiq safe and sushipool'''


def json_address_for_nimiq_core():
    sequence_list = wallet_address.split()
    new_string = '+'.join(map(str,sequence_list))
    nimiq_core_wallet_json = 'https://api.nimiqx.com/account/'
    url = nimiq_core_wallet_json + new_string
    return url


def json_address_for_sushi():
    sequence_list = wallet_address.split()
    new_string_sushi = '%20'.join(map(str, sequence_list))
    sushi_pool_connect = 'https://api.sushipool.com/api/v1/stats/profile/'
    url_sushi = sushi_pool_connect+new_string_sushi
    return url_sushi


'''WALLET SIZE (NIM) FORMATTER'''


def wallet_status():
    url_wallet = json_address_for_nimiq_core()
    nimiq_core = requests.get(url_wallet).json()
    wallet_state = nimiq_core['balance']
    balance_formatted = format(wallet_state/100000,'.2f')
    return balance_formatted


'''TIME & DATE OUTPUT FORMATTER'''


def time():
    # Time
    utc = 'UTC +3'
    d = datetime.datetime.now()
    timezone = pytz.timezone('Europe/Helsinki')
    d_aware = timezone.localize(d)
    final_time = d_aware.strftime("%d/%m %H:%M {}".format(utc))
    return final_time


'''Creating help'''


@bot.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    help_message_embed = discord.Embed(colour=discord.Colour.dark_gold())
    help_message_embed.set_author(name='Command list:')
    help_message_embed.add_field(name=f'{bot_prefix}simple_monitor <seconds>', value=f'Creates a loop based on selected time interval (seconds),'
                                                                                     f'to auto-check the state of the miners:\n'
                                                                                     f':red_circle: - Offline/not mining\n'
                                                                                     f':white_check_mark: - Online and mining'
                                                                                     f'\n***Example***: {bot_prefix}simpe_monitor 60\n'
                                                                                   f'monitors miners every 60 seconds', inline=False)
    help_message_embed.add_field(name=f'{bot_prefix}wallet_check', value=f'On-demand checks the balance of the wallet', inline=False)
    help_message_embed.add_field(name=f'{bot_prefix}transactions', value=f'On-demand check the last 4 transactions')
    help_message_embed.add_field(name=f'{bot_prefix}network', value=f'On-demand checks the status of Nimiq network')
    await bot.send_message(author, embed=help_message_embed)

'''SIMPLE MONITOR
-> Loops over the registered miners and provides status of the miner with red circle or white check mark 
-> Custom interval'''


@bot.command(pass_context=True)
async def simple_monitor(ctx, interval: int):
    while True:
        status = 'online'
        time_of_update = time()
        json_address = json_address_for_sushi()
        headers = {
            'User-Agent': 'SushiSensei 1.0',
        }     
        data = requests.get(json_address, headers).json()
        devices = data['devices']
        destination = ctx.message.channel

        simple_monitor_embed= discord.Embed(name='Miner state', colour=discord.Colour.dark_gold())

        for device in devices:
            miner_name = device['name']
            miner_status = device['device_status']

            if miner_status != status:
                simple_monitor_embed.add_field(name=f'Device: {miner_name}', value=f':red_circle:', inline=False)
            else:
                simple_monitor_embed.add_field(name=f'Device: {miner_name}', value=f':white_check_mark:', inline=False)

        simple_monitor_embed.set_footer(text=f'Status updated on {time_of_update}')
        await bot.say(destination, embed=simple_monitor_embed)
        await asyncio.sleep(interval)

'''WALLET DATA'''


@bot.command(pass_context=True)
async def wallet_check(ctx):
    destination = ctx.message.channel
    nimiq_wallet_json = json_address_for_nimiq_core()
    data = requests.get(nimiq_wallet_json).json()
    wallet_address = data['address']  # obtaining wallet address
    balance = data['balance']         # obtaining nimiq amount
    nimiq_sum = format(balance/100000, '.2f')
    # check_transactions = data['transactions']

    wallet_state_embed = discord.Embed(name='Wallet state', colour=discord.Colour.gold())
    wallet_state_embed.add_field(name='Data for wallet:', value=f'{wallet_address}')
    wallet_state_embed.add_field(name='Balance:', value=f'{nimiq_sum} NIM', inline=False)
    await bot.say(destination, embed=wallet_state_embed)

'''LAST 4 TRANSACTIONS'''


@bot.command(pass_context = True)
async def transactions(ctx):
    destination = ctx.message.channel
    nimiq_transaction = json_address_for_nimiq_core()
    data = requests.get(nimiq_transaction).json()
    transaction_list = data['transactions']

    for transaction in transaction_list[:3]:
        from_label= transaction['from_label']
        from_address = transaction['from_address']
        to_address = transaction['to_address']
        to_label = transaction['to_label']
        nimiq_amount_bag = transaction['value']
        real_trans_value = format(nimiq_amount_bag/100000, '.2f')

        time_stamp = transaction['timestamp']
        time = datetime.datetime.fromtimestamp(time_stamp)
        time_formatted = time.strftime('%H:%M:%S %Y-%m-%d ')

        transaction_embed = discord.Embed(name='Transaction history',colour=discord.Colour.green())
        transaction_embed.add_field(name=f'Timestamp', value=f'{time_formatted}')
        transaction_embed.add_field(name=f'From: {from_label}', value=f'{from_address}', inline=False)
        transaction_embed.add_field(name=f'To:{to_label}', value=f'{to_address}')
        transaction_embed.add_field(name=f'Amount', value=f'{real_trans_value} NIM', inline=False)
        await bot.say(destination, embed=transaction_embed)


'''NIMIQ NETWORK STATS'''


@bot.command(pass_context = True)
async def network(ctx):
    time_of_status = time()
    destination_network = ctx.message.channel
    nimiq_network = 'https://api.nimiqx.com/network-stats/'
    network_stats = requests.get(nimiq_network).json()
    hash_rate = network_stats['hashrate']
    mh_sec = format(hash_rate / 1000000, '.2f')
    block_height = network_stats['height']
    las_found = network_stats['last_found']
    in_minutes = datetime.timedelta(seconds=float(las_found))
    last_reward = network_stats['last_reward']
    calculated_nim = format(last_reward/100000, '.3f')
    nim_day_kh = network_stats['nim_day_kh']

    network_embed = discord.Embed(name='Network status', colour=discord.Colour.dark_gold())
    network_embed.add_field(name='Statistical data for Nimiq network', value=f'Network Hashrate:{mh_sec}MH/S\n'
                                                                             f'Last Block Found: {in_minutes} ago\n'
                                                                             f'Current Block: #{block_height}\n'
                                                                             f'Last Reward: {calculated_nim}\n'
                                                                             f'NIM/KH/Day: {nim_day_kh}NIM')
    network_embed.set_footer(text =f'Status on network obtained @: {time_of_status}')
    await bot.say(destination_network, embed=network_embed)

bot.run(discord_token) #insert token for discord
