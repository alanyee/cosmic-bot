import json
import random

import discord
from discord.ext import commands

aliens = open("alien_scrape.txt", 'r').read().split('\n\n\n')

alien_dict = {}
COLORS = frozenset(("Pink", "White", "Green", "Yellow", "Purple", "Red", "Blue", "Orange"))

for alien in aliens:
    (key, _) = alien.split('[')
    alien_dict[key.strip().lower()] = alien

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def alien(ctx, *args):
    alien_name = " ".join(args).lower()
    if alien_name in alien_dict:
        await ctx.send(alien_dict[alien_name])
    else:
        await ctx.send("Could not find alien named {alien_name}".format(
            alien_name=alien_name))

@bot.command()
async def color(ctx, *args):
    if 3 <= len(args) <= 8:
        await ctx.send(", ".join(map(str, zip(args, random.sample(COLORS, len(args))))))
    else:
        await ctx.send(f"Having {len(args)} players is not within the 3-8 player ruleset")

@bot.command()
async def colors(ctx):
    players = [member.nick if member.nick is not None else member.name for voice_channel in ctx.guild.voice_channels for member in voice_channel.members]
    if 3 <= len(players) <= 8:
        await ctx.send(", ".join(map(str, zip(players, random.sample(COLORS, len(players))))))
    else:
        await ctx.send(f"Having {len(players)} players is not within the 3-8 player ruleset")


with open('./secret_config.json', 'r') as f:
    data = json.load(f)

bot.run(data["token"])
