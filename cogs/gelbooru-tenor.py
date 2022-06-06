import discord
import TenGiphPy
import os

from discord.ext import commands
from dotenv import load_dotenv
from pygelbooru import Gelbooru

load_dotenv()
gelbooru = Gelbooru()

token = os.getenv("CLIENT_ID")
tenor_token = os.getenv("TENOR_TOKEN")
giphy_token = os.getenv("KEY_GIPHY")


class Cogbooru(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.BLACKLIST = ['shota', 'lolicon', "shotacon", 'nude', 'hentai', 'nsfw', 'gangbang', 'creampie', 'yaoi',
                          'yuri', 'sweatdrop', 'furry', 'ass',
                          'fuck', 'sex', 'cock', 'breast', 'big breast', 'panties', 'loli', 'pussy', 'naked']
        self.char = "'"

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print("Module: Gelbooru is ready !")

    @commands.command(name="sfwbooru", aliases=['booru'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def sfwbooru(self, ctx, *args):

        if len(args) == 0:
            result = str(await gelbooru.random_post(tags=["1girl"], exclude_tags=self.BLACKLIST))
            embed = discord.Embed(colour=ctx.author.colour)
            embed.add_field(name="Il manque un tag !", value=f"Veuillez mettre des tags suivants votre "
                                                             f"requête.\nExemple d'utilisation: "
                                                             f"`{self.client.command_prefix}[sfwbooru|booru] "
                                                             f"1girl neko`")
            embed.set_image(url=result)
            embed.set_footer(text='Image provided by Gelbooru.com')
            await ctx.send(embed=embed)

        request1 = list(args)
        final_request = list(request1)

        for item in final_request:
            if item in self.BLACKLIST:
                await ctx.send(
                    f'{ctx.author.name} je ne peux pas répondre à votre requête, en effet, cette dernière contient des '
                    f'mots interdits dans un salon sfw ! Si vous souhaitez utiliser des tags nsfw, veuillez les '
                    f'utiliser la commande: `{self.client.command_prefix}hbooru <tags>`, dans le salon approprié.')
            else:
                result = str(await gelbooru.random_post(tags=request1, exclude_tags=self.BLACKLIST))
                embed = discord.Embed(colour=ctx.author.colour, timestamp=ctx.message.created_at)
                embed.set_image(url=result)
                embed.set_footer(text="Image provided by Gelbooru.com")
                await ctx.send(embed=embed)

    @sfwbooru.error
    async def sfwbooru_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="nsfwbooru", aliases=['hbooru', 'hentaibooru'])
    @commands.is_nsfw()
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def nsfwbooru(self, ctx, *args):

        if len(args) == 0:
            result = str(await gelbooru.random_post(tags=["porn"], exclude_tags=['loli', 'shota', 'lolicon',
                                                                                 "shotacon", "low lolicon",
                                                                                 "low shotacon", "low_lolicon",
                                                                                 "low_shotacon", "child",
                                                                                 "children"]))
            embed = discord.Embed(colour=ctx.author.colour)
            embed.add_field(name="Il manque un tag !", value=f"Veuillez mettre des tags suivants votre "
                                                             f"requête.\nExemple d'utilisation: "
                                                             f"`{self.client.command_prefix}["
                                                             f"nsfwbooru|hbooru|hentaibooru] 1girl, hentai`")
            embed.set_image(url=result)
            embed.set_footer(text='Image provided by Gelbooru.com')
            await ctx.send(embed=embed)

        request1 = list(args)
        blacklist = ['loli', 'shota', 'lolicon',
                     "shotacon", "low lolicon",
                     "low shotacon", "low_lolicon",
                     "low_shotacon", "child",
                     "children"]

        for item in request1:
            if item in blacklist:
                await ctx.send(f"{ctx.author.name} vous utilisez un tag interdit ! Voici la liste de ces derniers: \
                                    {blacklist}.")
            else:
                result = str(await gelbooru.random_post(tags=request1, exclude_tags=blacklist))
                embed = discord.Embed(colour=ctx.author.colour, timestamp=ctx.message.created_at)
                embed.set_image(url=result)
                embed.set_footer(text="Image provided by Gelbooru.com")
                await ctx.send(embed=embed)

    @nsfwbooru.error
    async def nsfwbooru_error(self, ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            await ctx.send(f"{ctx.author.mention}, cette commande ne peut s'effectuer uniquement dans un salon nsfw !")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="tgif", aliases=['tenor'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def tgif(self, ctx, *, tag):

        t = TenGiphPy.Tenor(token=tenor_token)
        result = t.random(tag)

        embed = discord.Embed(colour=discord.Colour.from_rgb(9, 232, 217))
        embed.set_image(url=result)
        embed.set_footer(text="Gif provided by Tenor")

        await ctx.send(embed=embed)

    @tgif.error
    async def tgif_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en recharge.")

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} il manque le tag de recherche du gif !\nUtilisation: "
                           f"`{self.client.command_prefix}[tgif|tenor] <tag(s)>`")

    @commands.command(name="ggif", aliases=['giphy'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def ggif(self, ctx, *, tag):

        g = TenGiphPy.Giphy(token=giphy_token)
        result = g.random(tag=tag)['data']['images']['downsized_large']['url']

        embed = discord.Embed(colour=discord.Colour.dark_teal())
        embed.set_image(url=result)
        embed.set_footer(text="Gif provided by Giphy")

        await ctx.send(embed=embed)

    @ggif.error
    async def ggif_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en recharge.")

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} il manque le tag de recherche du gif !\nUtilisation: "
                           f"`{self.client.command_prefix}[ggif|giphy] <tag(s)>`")


def setup(client):
    client.add_cog(Cogbooru(client))
