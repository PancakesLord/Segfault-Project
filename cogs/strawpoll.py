import discord
import aiohttp

from discord.ext import commands


class Strawpoll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print('Module: Strawpoll is ready !')

    @commands.command(name="create_poll", aliases=['poll', 'strawpoll'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def create_poll(self, ctx, *,request):

        args = request.split("&")

        if len(args) < 3:
            await ctx.send(f"{ctx.author.mention} il manque des arguments pour créer le strawpoll "
                           "(Minimum un titre et deux options)!\nUtilisation: "
                           f"`{self.client.command_prefix}[create_poll|poll|strawpoll] "
                           "<titre>&<option1>&...&<option n>`")
            return None

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        "https://www.strawpoll.me/api/v2/polls",
                        json={
                            "title": args[0],
                            "options": args[1:],
                            "multi": "false",
                            "private": "true"
                        },
                        headers={"Content-Type": "application/json"}
                ) as response:
                    json = await response.json()
                    strawpoll_id = json["id"]

                await ctx.send(f"{ctx.author.mention} a lancé un strawpoll portant sur `{args[0]}` !\nAller voter à "
                               f"cette adresse: https://strawpoll.me/{strawpoll_id}")

        except Exception as e:
            await ctx.send(f'{ctx.author.mention} une erreur inconnue est survenue lors de la création du strawpoll !'
                           '\nErreur: '
                           f'{e}')

    @create_poll.error
    async def create_poll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} il manque des arguments pour créer le strawpoll "
                           "(Minimum un titre et deux options)!\nUtilisation: "
                           f"`{self.client.command_prefix}[create_poll|poll|strawpoll] "
                           "<titre>&<option1>&...&<option n>`")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")


def setup(client):
    client.add_cog(Strawpoll(client))
