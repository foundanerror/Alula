import asyncio,aiohttp

help_commands = {"fun","moderation"}


api_link = "http://api.sasaki.me:4444/"
thumbnail_image = 'https://cdn.discordapp.com/attachments/777647584746537003/823371836313829406/Alula.png'


help_descriptions = [
    ("!help fun","`Shows list of fun commands`",False),
    ("!help moderation","`Shows list of moderation commands`",False)
]


command_info = {
    "fun":{
        "!alarm":{
            "name":"alarm",
            "description":"`!alarm`"},
        "!amazing":{
            "name":"AMAZING",
            "description":"`!amazing description`"},
        "!ask":{
            "name":"ask",
            "description":"`!ask @User description`"},
        "!baka":{
            "name":"baka",
            "description":"`!baka @User`"},
        "!bite":{
            "name":"bite",
            "description":"`!bite @User`"},
        },
    "moderation":{}
}



    
async def request_api(cmdname):
    async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api.sasaki.me:4444/{cmdname}") as response:
                image = await response.text()
                return image

