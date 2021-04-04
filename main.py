
from discord.ext import commands
import discord
bot = commands.Bot(command_prefix="~")

#cogs are basically clases and models






@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="DA VINCI ??"))

    print('ya boi is rrrrrrrrrrrrrrrrrrrrrrrrready UP')

bot.load_extension(f'Cogs.test')
bot.load_extension(f'Cogs.gamble')
bot.load_extension(f'Cogs.Images')



bot.run('yoru discord bot token here')

