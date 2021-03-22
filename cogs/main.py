import discord,aiohttp,random
from discord.ext import commands
from datetime import datetime

help_descriptions = [
    ("!help fun","`Shows list of fun commands`",True)
]

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")

    @commands.command()
    async def help(self,ctx,cmdname):
        print("hello")

    @help.error
    async def help_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = 'Help',
                description = 'Basic help commands',
                colour = 0x3333FF,
                timestamp = datetime.utcnow()
            )
            for name, value, inline in help_descriptions:
                embed.add_field(name=name,value=value,inline=inline)
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/777647584746537003/823371836313829406/Alula.png')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Main(client))