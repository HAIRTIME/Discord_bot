import discord
from discord.ext import commands
from bot_token import token, my_channel


bot = commands.Bot(command_prefix="", case_insensitive=True);

#on ready event
@bot.event
async def on_ready():
    print("HAIRTIME BOT ENGAGED!");

#regular command
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!");

#command with text to speech enabled
@bot.command()
async def hairtime(ctx):
    await ctx.send("IT'S HAIRTIME!!", tts=True);

#test command with additional argument
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

#reply to specific text
@bot.event
async def on_message(message):
        
    if message.author.bot: return

    if message.content == "IT\'S HAIRTIME!!":
        general_channel = bot.get_channel(my_channel);
        await general_channel.send("IT'S HAIRTIME!!", tts=True);
    
    await bot.process_commands(message);

bot.run(token);  # Don't reveal your bot token, regenerate it asap if you do
