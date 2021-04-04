
import random

from TextToOwO.owo import text_to_owo

from discord.ext import commands


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.command()
    async def rng(self, ctx):

        n = random.randrange(1,100)
        await ctx.send(n)



    @commands.command()
    async def flip(self, ctx):
        m = random.randint(0, 1)
        await ctx.send("Heads" if m == 0 else "Tails")

def setup(bot):
    bot.add_cog(Gamble(bot))