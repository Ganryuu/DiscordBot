from discord.ext import commands
import random
bot = commands.Bot(command_prefix="~")

@commands.command(brief="lazy tester , tester lazy , lazy tester ")
async def test(ctx):
    await ctx.send("Testing works as intended")

bot.add_command(test)

@commands.command(brief="decomposes the sentence you just said")
async def repeat(ctx, *args):
    if len(args) > 0 :
        await ctx.send("this mf really just said")
        await ctx.send(args)
    else :
        await ctx.send("please enter an argument")
bot.add_command(repeat)

@commands.command(brief="dice game")
async def dice(ctx):
        n = random.randrange(1, 6)
        await ctx.send(n)
bot.add_command(dice)
@commands.command(brief="coin flip game")
async def flip(ctx):
        n = random.randint(0, 1)
        await ctx.send("Heads" if n==1 else "Tails")

bot.add_command(flip)
bot.run('YOUR BOT TOKEN HERE !!')
