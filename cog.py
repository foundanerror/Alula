import discord, os
from discord.ext import commands, tasks
from re import search

client = commands.Bot(command_prefix = "!", intents=discord.Intents.all())
    
@client.command()
async def reload(ctx, extension):
    if str(extension) == 'all':
        for filename in os.listdir('./cogs'):
            if filename.endswith(".py"):
                client.reload_extension(f'cogs.{filename[:-3]}')
                await ctx.send(f"Loading: {filename}")
                await ctx.send(f"Finished loading: {filename}")
    else:
        try:
            client.reload_extension(f'cogs.{extension}')
            await ctx.send(f"Reloading {extension}.py")
            await ctx.send(f"Finished loading: {extension}")
        except:
            await ctx.send('Error occured reloading extension')       

for filename in os.listdir('./cogs'):
    if filename.endswith(".py") and not search('data', filename):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loading: {filename}")

client.run("ODE3MjExNTg5MDE0NzE2NDQ2.YEGNmQ.WFkEBWJPu08MXOsQmZsgZvigUlk")