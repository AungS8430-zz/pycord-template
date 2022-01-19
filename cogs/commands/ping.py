import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(
        name='ping',
        description='Check bot latency.'
    )
    async def ping(self, ctx):
        embed = discord.Embed(
            title = '🏓|Pong!',
            description = f'Latency: {self.bot.latency} ms',
            color = discord.Color.green()
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(PingCog(bot))