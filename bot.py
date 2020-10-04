import discord
import sys, os
import asyncio
import json
import keep_alive
from discord import DMChannel
from pathlib import Path
from fnmatch import filter
from discord.ext.commands import Bot
from discord.ext import commands
from helper import cmderr, sprint
from classes import Bot


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("我準備好要上戰場了！！！")

@bot.event
async def on_member_join(member, data, guild):
    channel = bot.get_channel(759677671448772618)
    await channel.send(f'歡迎{member}加入小N的粉絲團!! :yum: :yum: :yum: :N_:')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(759677810674630656)
    await channel.send(f'{member}和我們說88 :cry: :cry: :cry: ')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}[ms]')

@bot.command()
async def youtube(ctx):
    await ctx.send("https://www.youtube.com/c/小Nsmalln")

@bot.command()
async def yt(ctx):
    await ctx.send("https://www.youtube.com/c/小Nsmalln")

@bot.command()
async def 粉絲專頁(ctx):
    await ctx.send("https://m.facebook.com/RMSmallN/")

@bot.command()
async def facebook(ctx):
    await ctx.send("https://m.facebook.com/RMSmallN/")

@bot.command()
async def fb(ctx):
    await ctx.send("https://m.facebook.com/RMSmallN/")

@bot.command()
async def ig(ctx):
    await ctx.send("https://www.instagram.com/wu_ming1/?hl=zh-tw")

@bot.command()
async def hi(ctx):
    await ctx.send("叫我嗎？ :face_with_monocle: :face_with_monocle::face_with_monocle:")

@bot.command()
async def 贊助(ctx):
    await ctx.send("https://payment.ecpay.com.tw/Broadcaster/Donate/9B054FBC4A03403D5489B8F13F46F887")

@bot.command()
async def N(ctx):
  await ctx.send("哈囉我叫史邁恩(小N)，每周一三五禮拜日晚上6:30在Youtube遊戲頻道不定期更新！記得訂閱開小鈴鐺bell")

@bot.command()
async def n(ctx):
  await ctx.send("哈囉我叫史邁恩(小N)，每周一三五禮拜日晚上6:30在Youtube遊戲頻道不定期更新！記得訂閱開小鈴鐺bell")

@bot.command()
async def 安安(ctx):
    await ctx.send("安安")
    await ctx.send("~~~")

@bot.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)

@bot.command()
async def 指令製作(ctx):
    await ctx.send("猴子@3807")

@commands.Cog.listener()
async def on_reaction_add(ctx,self,reaction,user):
    await ctx.message.send(user)
    await ctx.message.send(reaction)

@bot.command()
async def sos(ctx):
    embed=discord.Embed(title="指令說明", color=0xff0000)

    embed.add_field(name="ping", value="顯示我的延遲", inline=True)
    embed.add_field(name="youtube", value="顯示小N的yt", inline=True)
    embed.add_field(name="yt", value="顯示小N的yt", inline=True)
    embed.add_field(name="粉絲專頁", value="顯示小N的FB", inline=True)
    embed.add_field(name="facebook", value="顯示小N的FB", inline=True)
    embed.add_field(name="fb", value="顯示小N的FB", inline=True)
    embed.add_field(name="ig", value="顯示小N的IG", inline=True)
    embed.add_field(name="贊助", value="贊助小N", inline=True)
    embed.add_field(name="help", value="顯示help", inline=True)
    embed.add_field(name="sos", value="顯示該表", inline=True)
    embed.add_field(name="N", value="顯示小N的資料", inline=True)
    embed.add_field(name="n", value="顯示小N的資料", inline=True)
    embed.add_field(name="say", value="!say 加要我說的話", inline=True)
    embed.add_field(name="安安", value="和我聊天", inline=True)
    embed.add_field(name="hi", value="想和我聊天？？？", inline=True)
    embed.add_field(name="指令製作", value="顯示指令製作人", inline=True)
    embed.set_footer(text="作者：猴子@3807")

    await ctx.send(embed= embed)


bot.run('NzU5Mzg2NDkwMDEwMzM3MzUw.X28vxw.bX0JNG6C4YIaGwjECnpzpry8wOU')

if __name__ == "__main__":
	# Initialise
	if sys.platform == 'win32':
		loop = asyncio.ProactorEventLoop()
	else:
		loop = asyncio.get_event_loop()
	os.chdir(Path(__file__).resolve().parent)

	def get_prefix(bot, ctx):
		if not ctx.guild:
			return commands.when_mentioned_or('/', 'libereuse')(bot, ctx)
		with open('settings.json') as jfile:
			prefixes = json.load(jfile)
		if str(ctx.guild.id) not in prefixes:
			return commands.when_mentioned_or('/', 'libereuse')(bot, ctx)
		prefix = prefixes[str(ctx.guild.id)]
		return commands.when_mentioned_or(prefix)(bot, ctx)

	bot = Bot(command_prefix=get_prefix, pm_help=None, loop=loop)

	ext_path = "cmds"

	@bot.event
	async def on_ready():
		sprint('Logged in as {}\n'.format(bot.user))

	@bot.check
	async def useable(ctx):
		try:
			blacklist = ctx.bot.settings['blacklist']
			if not bot.is_ready() or ctx.author.bot:
				return False
			elif isinstance(ctx.channel, DMChannel):
				return False
			elif ctx.author.id == bot.owner_id:
				return True
			elif not ctx.channel.permissions_for(ctx.guild.me).send_messages:
				return False
			elif (ctx.author.id in blacklist['userID']) or (ctx.channel.id in blacklist['channelID']) or (ctx.guild.id in blacklist['guildID']):
				return False
			return True
		except Exception as e:
			raise RuntimeError from e

	@bot.command()
	@commands.is_owner()
	async def reload(ctx, component: str):
		"""Reload a component."""
		if component == 'settings':
			with open("settings.json", "r", encoding="utf8") as file:
				ctx.bot.settings = json.load(file, encoding='utf8')
			await ctx.send('Reloaded settings.')
			return
		await wildcardCheck(ctx, "reload", component)
	@bot.command()
	@commands.is_owner()
	async def unload(ctx, component: str):
		"""Unload a component."""
		await wildcardCheck(ctx, "unload", component)
	@bot.command()
	@commands.is_owner()
	async def load(ctx, component: str):
		"""Load a component."""
		await wildcardCheck(ctx, "load", component)

	async def wildcardCheck(ctx, method: str, query: str) -> None:
		if not method in ('load', 'unload', 'reload'):
			raise ValueError("Unsupported method {}.".format(method))
		msg = await ctx.send("{}ing component...".format(method.capitalize()))
		files = os.listdir(ext_path)
		files = [file[:-3] for file in os.listdir(ext_path) if file.endswith(".py")]
		components = filter(files, query)
		if method == 'reload':
			for comp in components:
				bot.reload_extension(f"{ext_path}.{comp}")
		elif method == 'unload':
			for comp in components:
				bot.unload_extension(f"{ext_path}.{comp}")
		elif method == 'load':
			for comp in components:
				bot.load_extension(f"{ext_path}.{comp}")
		components = ["`"+x+"`" for x in components]
		if not len(components) == 0:
			await msg.edit(content=f"{method.capitalize()}ed {', '.join(components)} component.")
		else:
			await msg.edit(content="No component matches your query.")

	@reload.error
	@unload.error
	@load.error
	async def errReload(ctx, e):
		await cmderr(ctx, e, 
			commands_errors_NotOwner='r'+'Only owner can use this command.', 
			commands_errors_MissingRequiredArgument="r"+f'Please specify a component to {ctx.command.name}.',
			commands_errors_ExtensionNotLoaded="r"+f"Can't {ctx.command.name}.  Extension hasn't been loaded.",
			commands_errors_NoEntryPointError="r"+"Extension doesn't have an entry point. (Missing `setup` function)",
			commands_errors_ExtensionNotFound="r"+"Extension not found.")

	for file in os.listdir(ext_path):
		if file.endswith(".py"):
			name = file[:-3]
			bot.load_extension(f"{ext_path}.{name}")
	
	keep_alive.keep_alive()
	bot.run(bot.settings['token'])
