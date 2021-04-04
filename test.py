
from discord.ext import commands

import random
from TextToOwO.owo import text_to_owo
class Test(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hey , how are you doing ? ")
    @commands.command()
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))

def setup(bot):
    bot.add_cog(Test(bot))