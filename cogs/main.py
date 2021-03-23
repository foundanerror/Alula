import discord,aiohttp,random,json
from discord.ext import commands
from datetime import datetime
from cogs import data

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")

    @commands.command()
    async def help(self,ctx,cmdname):
        if cmdname in data.command_info:
            inline1 = 0
            inline2 = 2
            print(cmdname.title())
            embed = discord.Embed(
                title = f"{cmdname.title()} commands!",
                description = f'Basic {cmdname} commands',
                colour = 0x3333FF,
                timestamp = datetime.utcnow()
                )
            embed.set_thumbnail(url=data.thumbnail_image)
            if len(data.command_info[cmdname]) == 0:
                await ctx.send("currently not finished")
            else:
                for value in data.command_info[cmdname]:
                    cmd = data.command_info[cmdname][value]
                    if inline1 < inline2:
                        embed.add_field(name=cmd["name"].title(),value=cmd["description"],inline=True)
                        inline1 = inline1 + 1
                    elif inline1 == inline2:
                        embed.add_field(name=cmd["name"].title(),value=cmd["description"],inline=False)
                        inline1 = 0
                await ctx.send(embed=embed)
        else:
            await ctx.send("Not a help command, say !help to see list of help commands")


    @help.error
    async def help_error(self,ctx,error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = 'Help',
                description = 'Basic help commands',
                colour = 0x3333FF,
                timestamp = datetime.utcnow()
            )
            for name, value, inline in data.help_descriptions:
                embed.add_field(name=name,value=value,inline=False)
            embed.set_thumbnail(url=data.thumbnail_image)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Main(client))