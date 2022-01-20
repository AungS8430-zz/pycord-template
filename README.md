# **A Pycord Template with some example!**
## Getting Started:
1. Clone this repository using 
```bash
git clone https://github.com/AungS8430/pycord-template.git
```
2. If you have discord.py installed, please do ```pip uninstall discord.py``` first.
3. You must have **Python 3.8 or above** installed ( I use Python 3.8.12).
4. Do 
```bash
pip install -r requirements.txt
``` 
to install requirements.
5. Go to `.env`, and insert your bot's token and welcome channel ID into the file. **You must keep your bot's token private!**
6. To run this basic bot, run 
```bash
python 3.8 main.py
``` 
in the same directory as your bot.
## Adding Commands or Events:
### Add commands:
1. Create a new Python file in `/cogs/commands`
2. Add this code in the file
```python
import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option #, SlashCommandGroup if you want to create a category.
class CogName(commands.Cog): # Replace 'CogName' with your cog name.
    def __init__(self, bot):
        self.bot = bot
    category = SlashCommandGroup('Category name', 'Category description')
    @slash_command( #change it into @category.command( if you use category.
        name='command name here',
        description='commnad description here',
    )
    async def commandname(self, ctx, option: Option(str, 'This is option', required=True)):
        embed = discord.Embed(
            title='hello',
            description=f'{option}',
            color=discord.Color.green()
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(CogName(bot))
```
3. Add the file directory into `main.py` in this format `cogs.commands.filename`
### Add event:
1. Create a new Python file in `/cogs/events`
2. Add this code in the file
```python
import discord
from discord.ext import commands, tasks

class CogName(commands.Cog): # Replace 'CogName' with your cog name.
    def __init__(self, bot):
        self.bot = bot
    @command.Cog.listener()
    async def eventname(self, ...):
        # do something
    
def setup(bot):
    bot.add_cog(CogName(bot))
```
4. Add the file directory into `main.py` in this format `cogs.event.filename`
