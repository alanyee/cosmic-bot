import json
import random

from discord.ext import commands

aliens = open("alien_scrape.txt", 'r').read().split('\n\n\n')

alien_dict = {}
colors = ("Pink", "White", "Green", "Yellow", "Purple", "Red", "Blue", "Orange")

for alien in aliens:
    (key, _) = alien.split('[')
    alien_dict[key.strip().lower()] = alien

bot = commands.Bot(command_prefix='!')


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
    if len(args) > 8:
        await ctx.send("Having {len(args)} players is above the 8 player maximum")
    else:
        await ctx.send(", ".join(map(str, zip(args, random.sample(colors, len(args))))))


with open('./secret_config.json', 'r') as f:
    data = json.load(f)

bot.run(data["token"])
