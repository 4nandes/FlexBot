import discord
from bs4 import BeautifulSoup
from urllib.request import urlopen


client = discord.Client()
botSecret = open("botSecret.txt","r")
code = botSecret.read()
skillNames = {0:'Overall', 1:'Attack', 2:'Defence', 
            3:'Strength', 4:'Hitpoints', 5:'Ranged', 
            6:'Prayer', 7:'Magic', 8:'Cooking', 
            9:'Woodcutting', 10:'Fletching', 11:'Fishing', 
            12:'Firemaking', 13:'Crafting', 14:'Smithing', 
            15:'Mining', 16:'Herblore', 17:'Agility', 
            18:'Thieving', 19:'Slayer', 20:'Farming', 
            21:'Runecrafting', 22:'Hunter', 23:'Construction'}
book = {'overall':0, 'attack':1, 'defence':2, 
        'strength':3, 'hitpoints':4, 'ranged':5, 
        'prayer':6, 'magic':7, 'cooking':8, 
        'woodcutting':9, 'fletching':10, 'fishing':11, 
        'firemaking':12, 'crafting':13, 'smithing':14, 
        'mining':15, 'herblore':16, 'agility':17, 
        'thieving':18, 'slayer':19, 'farming':20, 
        'runecrafting':21, 'hunter':22, 'construction':23}


@client.event
async def on_message(message):
    if message.author == client.user:
	    return
    if message.content.startswith("$flex"):
        await client.send_message(message.author, "Enter the name of your account: ")
        unCaller = await client.wait_for_message(timeout=15.0, author=message.author)
        unCaller = unCaller.content
        await client.send_message(message.author, "Enter the name of the account that we are flexing on today: ")
        unRec = await client.wait_for_message(timeout=15.0, author=message.author)
        unRec = unRec.content
        unCaller = unCaller.replace(" ","%20")
        unRec = unRec.replace(" ","%20")
        try:
            sauce = urlopen("http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=" + unCaller)
            soup = BeautifulSoup(sauce,'lxml')
            dataCaller = soup.get_text().split("\n")
            ranch = urlopen("http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player="  + unRec)
            stew = BeautifulSoup(ranch,'lxml')
            dataRec = stew.get_text().split("\n")
        except:
            await client.send_message(message.author, "That is not a valid username")
            return

        unRec = unRec.replace("%20"," ")
        unCaller = unCaller.replace("%20"," ")
        await client.send_message(message.author, "What skill are you comparing?")
        skill = await client.wait_for_message(timeout=15.0, author=message.author)
        skill = skill.content
        try:
            lvlCaller = dataCaller[book[skill]].split(",") 
            lvlRec = dataRec[book[skill]].split(",")
            if lvlCaller[1] > lvlRec[1]:
                await client.send_message(message.channel, "You ever show off your lvl.%d in %s just to flex on them %s niggas?\n**Flex Strength:** %d Levels %s XP\n\n*(%s is lvl.%d %s with %s XP)*" %(int(lvlCaller[1]),skill,unRec,(int(lvlCaller[1]) - int(lvlRec[1])),"{:,}".format((int(lvlCaller[2]) - int(lvlRec[2]))),unCaller,int(lvlCaller[1]),skill,"{:,}".format(int(lvlCaller[2]))))
        except:
            await client.send_message(message.author, "That skill does not exist")
            return
        return
    elif message.content.startswith("$stats"):
        await client.send_message(message.author, "Enter the name of your accout: ")
        Caller = await client.wait_for_message(timeout=15.0, author=message.author)
        try:
            sauce = urlopen("http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=" + Caller.content)
            soup = BeautifulSoup(sauce,'lxml')
        except:
            await client.send_message(message.author, "That user does not exist")
            return
        dataCaller = soup.get_text().split("\n")
        Caller = Caller.content.replace("%20"," ")
        msg = "```"
        msg += Caller + "'s stats:\n\n"
        for x in range(0,24):
            info = dataCaller[x].split(",")
            adder = "-" + skillNames[x] + ("."*(20-len(skillNames[x]))) + "Lvl: " + info[1] +(" "*(4-len(info[1]))) + " XP: " + "{:,}".format(int(info[2])) + "\n"
            msg += adder
        msg += "```"
        await client.send_message(message.channel, msg)
        return
             
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    await client.change_presence(game=discord.Game(name="you sleep", type=3))
    print(client.user.id)
    print('------')

client.run(code)

