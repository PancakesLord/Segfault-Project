import csv
import discord
import random

from PIL import Image
from discord.ext import commands


class JDR(commands.Cog):
    def __init__(self, client):
        self.client = client

    @staticmethod
    def avg(arr):
        return sum(arr) // len(arr)

    def avg_color_image(self, img):
        R = []
        G = []
        B = []

        width, height = img.size
        for x in range(width):
            for y in range(height):
                data = img.getpixel((x, y))
                R.append(data[0])
                G.append(data[1])
                B.append(data[2])

        return self.avg(R), self.avg(G), self.avg(B)

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print('Module: JDR is ready !')

    @commands.command(name="fiche", aliases=["file"])
    @commands.cooldown(rate=2, per=5, type=commands.BucketType.user)
    async def fiche(self, ctx, id_fiche):

        try:
            id_fiche = int(id_fiche)

        except ValueError:
            await ctx.send(f"{ctx.author.mention} vous devez entrer le numéro d'une fiche !")
            return

        id_fiche -= 1

        if id_fiche <= 0:
            id_fiche = 0

        with open("./cogs/jdr_ressources/fiches.csv", "r") as f:
            reader = tuple(csv.DictReader(f, delimiter=","))

            try:
                fiche = reader[id_fiche]

            except IndexError:
                await ctx.send(f"{ctx.author.mention} cette fiche n'existe pas !")
                return

        file_path = f"./cogs/jdr_ressources/npc_images/{fiche['Image']}"
        file = discord.File(file_path)
        avg_color = self.avg_color_image(Image.open(file_path))

        file_embed = discord.Embed(colour=discord.Colour.from_rgb(avg_color[0], avg_color[1], avg_color[2]),
                                   title=f"Fiche de {fiche['Prénom']}")

        file_embed.add_field(name="Nom",
                             value=f"{fiche['Nom']}",
                             inline=False)

        file_embed.add_field(name="Prénom",
                             value=f"{fiche['Prénom']}",
                             inline=False)

        file_embed.set_image(url=f"attachment://{fiche['Image']}")
        await ctx.send(embed=file_embed, file=file)

    @fiche.error
    async def fiche_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} cette commande est en recharge !")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} vous devez préciser le numéro de la fiche que "
                           f"vous souhaitez afficher !\nUtilisation: "
                           f"`{self.client.command_prefix}[fiche|file] <numéro de la fiche>`")

    @commands.command(name="areas", aliases=["zone"])
    @commands.cooldown(rate=2, per=5, type=commands.BucketType.user)
    async def areas(self, ctx, id_area):

        try:
            id_area = int(id_area)

        except ValueError:
            await ctx.send(f"{ctx.author.mention} vous devez entrer le numéro d'une fiche !")
            return

        id_area -= 1

        if id_area <= 0:
            id_area = 0

        with open("./cogs/jdr_ressources/areas.csv", "r") as f:
            reader = tuple(csv.DictReader(f, delimiter=";"))

            try:
                area = reader[id_area]

            except IndexError:
                await ctx.send(f"{ctx.author.mention} cette zone n'existe pas !")
                return

        file_one_path = f"./cogs/jdr_ressources/areas/{area['Image_une']}"
        file_one = discord.File(file_one_path)

        avg_color = self.avg_color_image(Image.open(file_one_path))

        file_embed = discord.Embed(colour=discord.Colour.from_rgb(avg_color[0], avg_color[1], avg_color[2]),
                                   title=f"{area['Nom']}",
                                   description=f"{area['Description']}")

        file_embed.set_image(url=f"attachment://{area['Image_une']}")
        await ctx.send(embed=file_embed, file=file_one)

        if area['Image_deux'] != "None":
            file_two_path = f"./cogs/jdr_ressources/areas/{area['Image_deux']}"
            file_two = discord.File(file_two_path)

            avg_color = self.avg_color_image(Image.open(file_two_path))

            file_two_embed = discord.Embed(title="", colour=discord.Colour.from_rgb(avg_color[0], avg_color[1],
                                                                                    avg_color[2]))
            file_two_embed.set_image(url=f"attachment://{area['Image_deux']}")

            await ctx.send(embed=file_two_embed, file=file_two)

    @areas.error
    async def areas_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} cette commande est en recharge !")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} vous devez préciser le numéro de la zone que "
                           f"vous souhaitez afficher !\nUtilisation: "
                           f"`{self.client.command_prefix}[area|zone] <numéro de la zone>`")

    @commands.command(name="synopsis", aliases=["aventure"])
    @commands.cooldown(rate=2, per=5, type=commands.BucketType.user)
    async def synopsis(self, ctx, id_synopsis):

        try:
            id_synopsis = int(id_synopsis)

        except ValueError:
            await ctx.send(f"{ctx.author.mention} vous devez entrer le numéro d'une fiche !")
            return

        id_synopsis -= 1

        if id_synopsis <= 0:
            id_synopsis = 0

        with open("./cogs/jdr_ressources/synopsis.csv", "r") as f:
            reader = tuple(csv.DictReader(f, delimiter=";"))

            try:
                synopsis = reader[id_synopsis]

            except IndexError:
                await ctx.send(f"{ctx.author.mention} ce synopsis n'existe pas !")
                return

        if synopsis["Thumbnail"] == "None":
            synopsis["Thumbnail"] = None

        with open(f'./cogs/jdr_ressources/synopsis/{synopsis["Fichier"]}', "r") as f:
            text = str(f.read()).split(" ")
            result_old = ""
            result = ""
            i = 1

            for word in text:

                result += word + " "

                if len(result) >= 4000:
                    embed_synopsis = discord.Embed(colour=discord.Colour.from_rgb(
                        int(synopsis["Red"]),
                        int(synopsis["Green"]),
                        int(synopsis["Blue"])
                    ),
                        title=f"{synopsis['Nom']} (page {i})",
                        description=f"{result_old}")

                    if synopsis["Thumbnail"] is not None:

                        embed_synopsis.set_thumbnail(url=f"{synopsis['Thumbnail']}")
                        await ctx.send(embed=embed_synopsis)

                    else:
                        await ctx.send(embed=embed_synopsis)

                    i += 1
                    result = ""
                    result_old = ""

                result_old += word + " "

            if len(result) > 0:
                embed_synopsis = discord.Embed(colour=discord.Colour.from_rgb(
                    int(synopsis["Red"]),
                    int(synopsis["Green"]),
                    int(synopsis["Blue"])
                ),
                    title=f"{synopsis['Nom']} (page {i})",
                    description=f"{result}")

                if synopsis["Thumbnail"] is not None:
                    embed_synopsis.set_thumbnail(url=f"{synopsis['Thumbnail']}")
                    await ctx.send(embed=embed_synopsis)

                else:
                    await ctx.send(embed=embed_synopsis)

    @synopsis.error
    async def synopsis_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} cette commande est en recharge !")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} vous devez préciser le numéro du synopsis que "
                           f"vous souhaitez afficher !\nUtilisation: "
                           f"`{self.client.command_prefix}[synopsis|aventure] <numéro du synopsis>`")

    @commands.command(name='dice', aliases=["roll"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def dice(self, ctx, number, rnumber=1):

        try:
            number = int(number)
            rnumber = int(rnumber)

            if rnumber <= 0:
                rnumber = 1

            for _ in range(rnumber):
                await ctx.send(f"Le résultat est: {random.randint(1, number)}")

        except ValueError:
            await ctx.send(f"{ctx.author.mention} il faut entrer un nombre au lieu de {number} !\nUtilisation: "
                           f"`{self.client.command_prefix}[dice|roll] <taille du dé>`")

    @dice.error
    async def dice_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} il faut entrer un nombre !\nUtilisation: "
                           f"`{self.client.command_prefix}[dice|roll] <taille du dé>`")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")


def setup(client):
    client.add_cog(JDR(client))
