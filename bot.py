import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'[System] {bot.user} 실행 준비 완료')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'안녕하세요! {ctx.author.mention}!')

bot.run('봇 토큰')
