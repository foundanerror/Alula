import discord,aiohttp,random
from discord.ext import commands


class Convert(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")


    @commands.command()
    async def alarm(self,ctx,user: discord.User = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api.sasaki.me:4444/alarm") as response:
                image = await response.text()
        embed = discord.Embed(title=f'Alarm!')
        embed.set_image(url=image)
        await ctx.send(embed=embed)


    @commands.command()
    async def amazing(self,ctx,user: discord.User = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api.sasaki.me:4444/amazing") as response:
                image = await response.text()
        embed = discord.Embed(title=f'Amazing!')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def ask(self,ctx,user: discord.User = None,*,description):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api.sasaki.me:4444/ask") as response:
                image = await response.text()
        if user:
            embed = discord.Embed(title=f'{ctx.author.name} asks {user.name}: {description}')
        else:
            embed = discord.Embed(title=f'{ctx.author.name} asks someone: {description}')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def baka(self,ctx,user: discord.User = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api.sasaki.me:4444/baka") as response:
                image = await response.text()
        if user:
            embed = discord.Embed(title=f'{ctx.author.name} calls {user.name} baka!')
        else:
            embed = discord.Embed(title=f'{ctx.author.name} calls someone baka!')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def bite(self,ctx,user: discord.User = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api.sasaki.me:4444/bite") as response:
                image = await response.text()
        if user:
            embed = discord.Embed(title=f'{ctx.author.name} bites {user.name}')
        else:
            embed = discord.Embed(title=f'{ctx.author.name} bites someone')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Convert(client))