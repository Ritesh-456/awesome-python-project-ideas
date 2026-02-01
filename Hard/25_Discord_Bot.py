import discord
from discord.ext import commands
import random
import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello', help='Responds with a greeting')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command(name='roll', help='Rolls a dice. Usage: !roll [number of sides]')
async def roll(ctx, sides: int = 6):
    if sides < 2:
        await ctx.send("Number of sides must be at least 2!")
        return
    result = random.randint(1, sides)
    await ctx.send(f'{ctx.author.mention} rolled a {result} on a {sides}-sided die!')

@bot.command(name='flip', help='Flips a coin')
async def flip(ctx):
    result = random.choice(['Heads', 'Tails'])
    await ctx.send(f'{ctx.author.mention} flipped {result}!')

@bot.command(name='time', help='Shows current time')
async def time(ctx):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f'Current time: {current_time}')

@bot.command(name='ping', help='Shows bot latency')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')

@bot.command(name='quote', help='Provides an inspirational quote')
async def quote(ctx):
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "The best way to predict the future is to create it. - Peter Drucker"
    ]
    quote = random.choice(quotes)
    await ctx.send(quote)

@bot.command(name='serverinfo', help='Shows server information')
async def serverinfo(ctx):
    server = ctx.guild
    embed = discord.Embed(title=f"{server.name} Info", color=0x00ff00)
    embed.add_field(name="Server ID", value=server.id, inline=True)
    embed.add_field(name="Member Count", value=server.member_count, inline=True)
    embed.add_field(name="Created At", value=server.created_at.strftime("%Y-%m-%d"), inline=True)
    embed.set_thumbnail(url=server.icon.url if server.icon else None)
    await ctx.send(embed=embed)

@bot.command(name='userinfo', help='Shows user information')
async def userinfo(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    embed = discord.Embed(title=f"{member.name}#{member.discriminator}", color=member.color)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Respond to mentions
    if bot.user.mentioned_in(message):
        await message.channel.send(f"Hello {message.author.mention}! How can I help you?")

    await bot.process_commands(message)

# Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token
bot.run('YOUR_BOT_TOKEN_HERE')