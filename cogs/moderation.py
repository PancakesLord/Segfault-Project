import time
import traceback
import sys
import discord
import csv

from discord.ext import commands
from discord.ext.commands import has_permissions


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print('Module: Moderation is ready !')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} a été désactivée.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} ne peut pas être utilisée dans les messages privés.')

            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'
                return await ctx.send('Je ne trouve pas ce membre dans la liste. Réessayer.')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command(name="kick", pass_context=True)  # Commandes
    @has_permissions(kick_members=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if not member:
            await ctx.send("Cette personne n'existe pas !")
            return

        elif member == ctx.author:
            await ctx.send("Vous ne pouvez pas vous auto-expulser.")
            return

        expulsion = discord.Embed(title=f"{member.display_name} a été expulsé par {ctx.author.name}",
                                  description=f"Raison: {reason}",
                                  colour=member.colour)
        expulsion.set_thumbnail(url=member.avatar_url)

        await member.kick(reason=reason)
        await ctx.send(embed=expulsion)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Veuillez mentionner le membre à kick.\nUtilisation: "
                           f"`{self.client.command_prefix}kick <mention>`")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !"
                f"\nPermissions requises: Expulser des membres")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="ban", pass_context=True)
    @has_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if not member:
            await ctx.send("Cette personne n'existe pas !")
            return

        elif member == ctx.author:
            await ctx.send("Vous ne pouvez pas vous auto-bannir.")
            return

        bannissement = discord.Embed(title=f"{member.display_name} a été banni(e) par {ctx.author.name}",
                                     description=f"Raison: {reason}",
                                     colour=member.colour)
        bannissement.set_thumbnail(url=member.avatar_url)

        await member.kick(reason=reason)
        await ctx.send(embed=bannissement)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Veuillez mentionner le membre à bannir.\nUtilisation:"
                f" `{self.client.command_prefix}ban <mention> <raison>`")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !"
                f"\nPermissions requises: Expulser des membres et Bannir des membres")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="unban", pass_context=True)
    @has_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        # ici, le nom et le num de l'utilisateur vont être séparé en au lvl du # (le # sera suppr)
        if not member:
            await ctx.send("Cette personne n'existe pas !")
            pass

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} est désormais débanni !")
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Veuillez spécifier le membre à débannir.\nUtilisation: "
                           f"`{self.client.command_prefix}unban <tag ou mention>`")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !"
                f"\nPermissions requises: Expulser des membres et Bannir des membres")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="clear", aliases=["purge"], pass_context=True)
    @has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def clear(self, ctx, amount: int):
        amount += 1
        await ctx.channel.purge(limit=amount)

        amount -= 1
        await ctx.send(f"{amount} messages supprimés !")

        time.sleep(0.5)
        await ctx.channel.purge(limit=1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Veuillez spécifier le nombre de messages à supprimer.\nUtilisation: "
                           f"`{self.client.command_prefix}clear <nombre de messages à supprimer>`")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !"
                f"\nPermissions requises: Gérer les messages")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="create_category", aliases=["ccy"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def create_category(self, ctx, *args):

        for category in args:
            await ctx.guild.create_category(str(category.lower()))

    @commands.command(name="get_categories", aliases=["gc"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def get_categories(self, ctx):
        i = 0
        for cat in ctx.guild.categories:

            cat_embed = discord.Embed(title=f'{cat.name}',
                                      description=f'Discord ID: {cat.id}\nNumero: {i}',
                                      colour=discord.Colour.dark_blue())

            await ctx.send(embed=cat_embed)
            i += 1

    @get_categories.error
    async def get_categories_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !\nPermission "
                "requise: Gérer les salons")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="create_channels", aliases=["ccs"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def create_channels(self, ctx, *args):
        cat_index = int(args[0])
        channels = args[1:]

        for channel in channels:
            await ctx.guild.categories[cat_index].create_text_channel(name=str(channel.lower()).strip())

    @create_channels.error
    async def create_channels_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !\nPermission "
                "requise: Gérer les salons")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")



def setup(client):
    client.add_cog(Moderation(client))
