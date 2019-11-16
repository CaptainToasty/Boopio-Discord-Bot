import discord, asyncio, dbl, random



client = discord.Client()

#Token for the bot
token = ""


#Text files containing Lucio Quotes and arrays for each file
lucioHealingFile = open("HealingQuotes.txt", "r")
lucioQuotesFile = open("LucioQuotes.txt", "r")
lucioQuotes = [x.rstrip() for x in lucioQuotesFile]
lucioHealing = [x.rstrip() for x in lucioHealingFile]


#notifies server owner when the bot starts up
#Sets the bots game status to Playing Lucio Ball
@client.event
async def on_ready():
	print("We have logged in as {0.user}.".format(client))
	await client.change_presence(activity=discord.Game(name="Lucio Ball"))


#the commands for the bot
@client.event
async def on_message(message):
	
	#removes the case sensitiveness of the commands
	message.content = message.content.lower()
	
	#prevents the bot from replying to itself
	if message.author == client.user:
		return
		
	if message.content.startswith("!help"):
		await message.channel.send("'!help','!boop', and 'i need healing' are the only commands.\n'!boop' sends a random lucio quote to a random server member.\n'I need healing' send a healing quote to the user who sent the command.\nAll the commands are **NOT** case sensitive.")
		
	
		
	#posts a random lucio healing response from lucioHealing
	if message.content.startswith("i need healing"):
		await message.channel.send("<@{}> {}".format(message.author.id,random.choice(lucioHealing)))
		
	
	#posts a random lucio quote to a random user
	if message.content.startswith("!boop"):
		#gets all the member's id for mentioning
		members = [x.id for x in client.get_all_members() if x != client.user]
		#picks a random lucio quote
		msg = random.choice(lucioQuotes)
		#picks a random member's id
		number = random.randrange(0,len(members))
		randomMember = members[number]
		
		await message.channel.send("<@{}> {}".format(randomMember,msg))
	




client.run(token)



