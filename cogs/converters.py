import discord,aiohttp,random
from discord.ext import commands
from cogs import data


class Convert(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")


    @commands.command()
    async def alarm(self,ctx,user: discord.User = None):
        image = await data.request_api(ctx.command.name)
        embed = discord.Embed(title=f'ALARM!')
        embed.set_image(url=image)
        await ctx.send(embed=embed)


    @commands.command()
    async def amazing(self,ctx,user: discord.User = None):
        image = await data.request_api(ctx.command.name)
        embed = discord.Embed(title=f'Amazing!')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def ask(self,ctx,user:discord.User=None,*,description=""):
        image = await data.request_api(ctx.command.name)
        if user:
            embed = discord.Embed(title=f'{ctx.author.name} asks {user.name} {description}')
        else:
            embed = discord.Embed(title=f'{ctx.author.name} asks {description}')

        embed.set_image(url=image)
        await ctx.send(embed=embed)


    @commands.command()
    async def baka(self,ctx,user: discord.User = None):
        image = await data.request_api(ctx.command.name)
        if user:
            embed = discord.Embed(title=f'{ctx.author.name} calls {user.name} baka!',colour = 0x3333FF,)
        else:
            embed = discord.Embed(title=f'{ctx.author.name} calls someone baka!',colour = 0x3333FF,)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def bite(self,ctx,user: discord.User = None):
        image = await data.request_api(ctx.command.name)
        if user:
            embed = discord.Embed(title=f'{ctx.author.name} bites {user.name}')
        else:
            embed = discord.Embed(title=f'{ctx.author.name} bites someone')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Convert(client))