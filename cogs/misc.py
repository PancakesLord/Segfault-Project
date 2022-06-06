import discord
import random

from discord.ext import commands
from discord.ext.commands import has_permissions


class Miscellaneous(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print('Module: Miscellaneous is ready !')

    @commands.command(name="members", aliases=['membres'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def members(self, ctx):
        guild = ctx.message.guild
        await ctx.send(f"""Il y a {guild.member_count} membres sur votre serveur !""")

    @members.error
    async def members_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="say", aliases=['dire', 'talk'], pass_context=True)
    @has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def say(self, ctx, *, content):
        contenu = content
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{contenu}")

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Veuillez spécifier ce que je dois dire.\nExemple d'utilisation: "
                           f"{self.client.command_prefix}say Hello !")

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                "Vous n'avez pas les permissions suffisantes pour me faire dire quelquechose.\nPermissions Requises: "
                "Gérer les messages")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='avatar')
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member):
        avatar_link = member.avatar_url
        embed = discord.Embed(colour=member.color, title=f'Avatar de {member}')
        embed.set_image(url=avatar_link)
        await ctx.send(embed=embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            avatar_link = ctx.author.avatar_url
            embed = discord.Embed(colour=ctx.author.color, title=f'Avatar de {ctx.author}')
            embed.set_image(url=avatar_link)
            await ctx.send(embed=embed)

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='userinfo', aliases=["user", "lookup"])
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def userinfo(self, ctx, member: discord.Member):

        if not member.bot:
            lol = "Non, ce n'est pas un bot"
        else:
            lol = "Oui, c'est un bot"

        if member.nick is None:
            pseudo = 'Aucun'
        else:
            pseudo = member.nick

        roles = [role for role in member.roles]

        info = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
        info.set_author(name=f"Informations sur {member}")
        info.set_thumbnail(url=member.avatar_url)
        info.set_footer(text=f'Demandées par {ctx.author}', icon_url=ctx.author.avatar_url)

        info.add_field(name="Id:", value=member.id, inline=False)
        info.add_field(name="Nom:", value=member.display_name, inline=False)
        info.add_field(name="Pseudo sur le serveur:", value=f"{pseudo}", inline=False)
        info.add_field(name="Nom du Serveur:", value=member.guild, inline=False)
        info.add_field(name="Compte créé le:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                       inline=False)
        info.add_field(name="A rejoind le serveur le:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                       inline=False)
        info.add_field(name="Rôle principal:", value=member.top_role.mention, inline=False)
        info.add_field(name=f"Roles ({len(roles)})", value=" ".join(role.mention for role in roles), inline=False)
        # info.add_field(name=f"Nombre d'avertissement", value=f"{warnings_number}")
        info.add_field(name="Bot ?", value=f"{lol}", inline=False)

        await ctx.send(embed=info)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "Veuillez mentionner la personne dont vous souhaitez voir les informations.\nSi vous souhaitez voir "
                f"vos propres informations, faites: {self.client.command_prefix}me")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='me')
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    async def me(self, ctx):
        author = ctx.author

        if not author.bot:
            lol = "Non, je ne suis pas un bot"
        else:
            lol = "Oui, je suis un bot"

        if author.nick is None:
            pseudo = 'Aucun'
        else:
            pseudo = author.nick

        roles = [role for role in author.roles]

        info = discord.Embed(colour=author.color, timestamp=ctx.message.created_at)
        info.set_author(name=f"Informations sur {author}")
        info.set_thumbnail(url=author.avatar_url)
        info.set_footer(text=f'Demandées par {ctx.author}', icon_url=ctx.author.avatar_url)

        info.add_field(name="Id:", value=author.id, inline=False)
        info.add_field(name="Nom:", value=author.name, inline=False)
        info.add_field(name="Pseudo sur le serveur:", value=f"{pseudo}", inline=False)
        info.add_field(name="Nom du Serveur:", value=author.guild, inline=False)
        info.add_field(name="Compte créé le:", value=author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                       inline=False)
        info.add_field(name="A rejoind le serveur le:", value=author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                       inline=False)
        info.add_field(name="Rôle principal:", value=author.top_role.mention, inline=False)
        info.add_field(name=f"Roles ({len(roles)})", value=" ".join(role.mention for role in roles), inline=False)
        # info.add_field(name=f"Nombre d'avertissement", value=f"{warnings_number}")
        info.add_field(name="Bot ?", value=f"{lol}", inline=False)

        await ctx.send(embed=info)

    @me.error
    async def me_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='randomchoose', aliases=["rchoose", "choice"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def randomchoose(self, ctx, *, content):
        choose = list(content.split('|'))
        if len(list(choose)) == 1:
            await ctx.send(
                f"{ctx.author.name}, veuillez me donner deux choses au moins parmis lesquels choisir !\nUtilisation: "
                f"`{self.client.command_prefix}[randomchoose|randchoose|rchoose] <choix 1>| ... |<choix n>`")
        else:
            randchoose = random.choice(choose)
            await ctx.send(f"À votre place, je choisirai: {randchoose}.")

    @randomchoose.error
    async def randomchoose_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"{ctx.author.name}, vous devez me donner les choses avec lesquels vous hésitez !\nUtilisation:  "
                f"`{self.client.command_prefix}[randomchoose|randchoose|rchoose] <choix 1>| ... |<choix n>`")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='pancake', aliases=["pancakes"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def pancake(self, ctx):

        file_path = "./cogs/ressources/pancakes_pixel.png"
        file = discord.File(file_path)

        pancake = discord.Embed(title="Make Pancakes Great Again !",
                                colour=discord.Colour.from_rgb(231, 153, 79))

        pancake.add_field(name="Principale différence",
                          value="La crêpes n'a pas de levure et de beurre.",
                          inline=False)

        pancake.add_field(name="Recette du Pancake, selon Cyril Lignac",
                          value="https://cuisine.journaldesfemmes.fr/recette/1008340-pancakes-de-cyril-lignac",
                          inline=False)

        pancake.add_field(name="Recette de la Crêpe, selon Cyril Lignac",
                          value="https://www.femmeactuelle.fr/cuisine/recettes-de-cuisine/"
                                "cyril-lignac-sa-recette-facile-et-rapide-de-pate-a-crepes-2094799",
                          inline=False)

        pancake.set_thumbnail(url="attachment://pancakes_pixel.png")
        pancake.set_image(url="https://c.tenor.com/eSIwH2yEbXwAAAAd/pancakes-strawberries.gif")

        await ctx.send(embed=pancake, file=file)

    @pancake.error
    async def pancake_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    # secret command
    @commands.command(name="crepes", aliases=['crêpes', "crepe", "crêpe"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def crepes(self, ctx):
        await ctx.send(f"{ctx.author.mention} je crois que vous vous êtes trompé ! Effectivement, la bonne commande "
                       f"est `{self.client.command_prefix}pancakes` !\nJe sais que certaine personne ne font pas"
                       " la différence: voici donc une explication conscise de ce qui les différencies !")

        await self.pancake(ctx)

    @crepes.error
    async def crepes_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme, cette commande est en recharge !")


def setup(client):
    client.add_cog(Miscellaneous(client))
