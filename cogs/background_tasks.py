import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(['Testing','Still Testing'])

class background_tasks(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.")
        self.change_status.start()
    

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Activity(type= discord.ActivityType.watching,name= f'Over {len(self.client.guilds)} Servers, Prefix: !'))
    



def setup(client):
    client.add_cog(background_tasks(client))
