import discord
import random
from discord.ext import commands

# the prefix used before typing the command
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Ready to Go!')

# checking ping
# .ping


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

# creating a yes or no asnwer with the question starting with 'should'
# .should I play video games right now?


@client.command(aliases=['should'])
async def yesno(ctx, *, question):
    responses = ['No!', 'Maybe next time!', 'Sure.', 'Very well, why not.',
                 'Give it a shot!', 'Maybe next time!', 'You sure?']
    await ctx.send(f'{random.choice(responses)}')

# clear the server chat history, with role restrictions
# .clear 10 - deletes 10 messages / .clear - clears 2 messages


@client.command()
@commands.has_role('enterrole')
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount+1)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('Sorry! You do not have access to remove message!')


client.run('entertoken')
