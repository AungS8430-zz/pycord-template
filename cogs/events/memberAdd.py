import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
load_dotenv()

class memberAddCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = os.environ.get('welcome_channel_id')
        channel = self.bot.get_channel(channel_id)
        if channel is None:
            print('Welcome channel not found.')
            return
        else:
            embed = discord.Embed(
                title = 'Welcome!',
                description = f'{member.mention} just joined this server!',
                color = discord.Color.blue()
            )
            await channel.send(embed)