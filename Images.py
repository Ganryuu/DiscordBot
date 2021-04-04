import aiohttp
from discord.ext import commands
import discord
import random
import praw
REDDIT_APP_ID ='your reddit app id here'
REDDIT_APP_SECRET ='your reddit app seceret here '
#reddit.config
Subs = ['funny', 'meme', 'Greentext']
class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_SECRET, user_agent="ShadeBot:%s:1.0"%REDDIT_APP_ID)
    @commands.command()
    async def anon(self, ctx, subreddit: str= ""):
        async with ctx.channel.typing():
            if self.reddit:
                #start working
                chosen_subreddit = Subs[2]
                if  subreddit:
                    if subreddit in Subs:
                        chosen_subreddit = subreddit
                submissions = self.reddit.subreddit(chosen_subreddit).hot()

                post_picked = random.randint(1,100)
                for i in range(0, post_picked):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.url)

            else :

                await ctx.send("This is not working , contact devs.")


def setup(bot):
    bot.add_cog(Images(bot))
