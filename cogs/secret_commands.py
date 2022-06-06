import discord
import TenGiphPy
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
tenor_token = os.getenv("TENOR_TOKEN")


class SecretCommands(commands.Cog):

    def __int__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Module: SecretCommands is ready !")

    @commands.command(name="admin_power", aliases=['admin', "become_admin", "rick"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def admin_power(self, ctx):
        t = TenGiphPy.Tenor(token=tenor_token)
        result = t.random("rickroll")

        rick = discord.Embed(colour=ctx.author.color, title=f"{ctx.author.name} est devenu un "
                                                            f"admin ! :)")
        rick.set_image(url=result)
        rick.set_footer(text="Gif provided by Tenor")

        await ctx.send(embed=rick)

    @admin_power.error
    async def admin_power_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme, cette commande est en recharge !")

    @commands.command(name="ricardo", aliases=['dieu', 'god'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def ricardo(self, ctx):

        ricardo = discord.Embed(colour=ctx.author.color, title=f"{ctx.author.name} a invoqué "
                                                               f"Dieu ! :)")

        ricardo.set_image(url="https://c.tenor.com/Llnx0bFiXWIAAAAd/ricardo-milos-mijolnir-ricardomilos.gif")
        ricardo.set_footer(text="Gif provided by Tenor")

        await ctx.send(embed=ricardo)

    @ricardo.error
    async def ricardo_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme, cette commande est en recharge !")


def setup(client):
    client.add_cog(SecretCommands(client))
