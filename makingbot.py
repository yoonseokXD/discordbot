import asyncio, discord
from asyncio import events
from discord import message
from discord.ext import commands



app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
	print('log in on ... :')
	print(app.user.name)
	print("connection succesfully")
	await app.change_presence(status=discord.Status.online, activity=None)

@app.event
async def on_message(message):
		if message.author == app.user:
			return


@app.command()
async def 재획아(ctx,*,text = None):
	if(text != None):
		await ctx.send(text)
	else:
		await ctx.send("왜 말을못하냐구!")

@app.command()
async def 쿨라썬(ctx,*,text = None):
	if (text == None):
		await ctx.send("이병찬 아직도 여깄냐? 탕탕탕")
	else:
		await ctx.send("뭐래 쿨라썬같은게")


app.run('ODIwNjE5NzMxOTY3MDE3MDEw.YE3zrg.aQnPfX-FAZBlZYw5kOqgvhoCXZg')

