# bot.py

import os
import discord
import dotenv
import csv

from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True

Client = discord.Client()
client = commands.Bot(command_prefix="seg!", intents=intents)
client.version = 'Alpha - 1.1'
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,
                                 activity=discord.Game(name=f"{client.command_prefix}help | Program "
                                                            f"received signal SIGSEGV, Segmentation fault"))

    print('Bot has connected to Discord!')


@client.event
async def on_disconnect():
    print("Bot has been disconnect/failed to connect to discord")


@client.event
async def on_member_join(member: discord.Member):
    welcome = discord.Embed(colour=discord.Colour.green(),
                            description=f'Bienvenue {member.display_name} sur {member.guild.name} ! '
                                        f'Nous sommes désormais '
                                        f'{int(member.guild.member_count)} membres !'
                                        f'\nFaites `{client.command_prefix}help` pour voir la '
                                        f'totalité de mes commandes !')

    welcome.set_thumbnail(url=f"{member.guild.icon_url}")
    welcome.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")

    await member.create_dm()
    await member.dm_channel.send(embed=welcome)


@client.command(name="ping", aliases=["latency"])  # Commandes
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def ping(ctx):  # ctx = context, donc: le channel et la rep à l'auteur
    await ctx.send(f":ping_pong: Pong ! Mon ping est de {round(client.latency * 1000)}ms !")


@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Cette commande n'existe pas.\nFaites: {client.command_prefix}help "
                       f"pour avoir la liste complète de mes commandes")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
