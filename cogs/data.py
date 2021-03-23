

help_commands = {"fun","moderation"}

fun = [
    ("!slap","`!slap @user`")
]



thumbnail_image = 'https://cdn.discordapp.com/attachments/777647584746537003/823371836313829406/Alula.png'


help_descriptions = [
    ("!help fun","`Shows list of fun commands`",False),
    ("!help moderation","`Shows list of moderation commands`",False)
]


command_info = {
    "fun":{
        "!slap":{
            "name":"slap",
            "description":"`!slap @User`"},
        "!ask":{
            "name":"ask",
            "description":"`!ask @User description`"}
    },
    "moderation":{}
}

if "fun" in command_info:
    print("ok")

    


