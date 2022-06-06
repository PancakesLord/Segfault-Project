import discord

from discord.ext import commands


class AboutMe(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print('Module: AboutMe is ready !')

    @commands.command(name="github")
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def github(self, ctx):
        github = discord.Embed(title=f'Version de {self.client.user.name}',
                               description=f"{self.client.version}",
                               colour=discord.Colour.from_rgb(202, 14, 244))

        github.add_field(name="Lien du Github",
                         value="https://github.com/PancakesLord/Segfault-Project",
                         inline=False)

        github.set_thumbnail(url=self.client.user.avatar_url)

        await ctx.send(embed=github)

    @github.error
    async def github_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="version", aliases=['vers'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def version(self, ctx):

        version = discord.Embed(title=f'Version de {self.client.user.name}',
                                description=f"{self.client.version}",
                                colour=discord.Colour.from_rgb(202, 14, 244))

        version.add_field(name="Lien du Github",
                          value="https://github.com/PancakesLord/Segfault-Project",
                          inline=False)

        version.set_thumbnail(url=self.client.user.avatar_url)

        await ctx.send(embed=version)

    @version.error
    async def version_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")


def setup(client):
    client.add_cog(AboutMe(client))
