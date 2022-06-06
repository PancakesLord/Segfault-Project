import discord
import TenGiphPy
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
tenor_token = os.getenv("TENOR_TOKEN")


class Social(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.t = TenGiphPy.Tenor(tenor_token)

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print('Module: Social is ready !')

    @commands.command(name="hug", aliases=['calin', 'câlin'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member = None):

        if member is None:
            member = self.client.user.name

        elif ctx.author == member:

            embed_hug = discord.Embed(title=f":pleading_face: {ctx.author.name} a bien besoins d'un câlin !",
                                      color=discord.Colour.orange(),
                                      timestamp=ctx.message.created_at)

            embed_hug.set_image(url="https://c.tenor.com/t5lYAeU4S-wAAAAC/i-want-a-hug-hug.gif")
            await ctx.send(embed=embed_hug)
            return
        else:
            member = member.display_name

        hug_gif = self.t.random("hug anime")

        embed_hug = discord.Embed(title=f":people_hugging: {ctx.author.name} fait un câlin à {member} !",
                                  color=discord.Colour.orange(),
                                  timestamp=ctx.message.created_at)

        embed_hug.set_image(url=hug_gif)

        await ctx.send(embed=embed_hug)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.author.name} cette commande est en recharge !')

    @commands.command(name="bang", aliases=['gun', 'tirer'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def bang(self, ctx, member: discord.Member = None):

        if member is None:
            member = self.client.user.name

        elif member == ctx.author:

            embed_bang = discord.Embed(title=f":skull: {ctx.author.name} essaie de se suicider !",
                                       description="(Mais échoue)",
                                       color=discord.Colour.from_rgb(175, 32, 19),
                                       timestamp=ctx.message.created_at)

            embed_bang.set_image(url="https://c.tenor.com/iRRfRNU7IGMAAAAC/iwakura-lain-suicide.gif")
            await ctx.send(embed=embed_bang)
            return

        else:
            member = member.display_name

        bang_gif = self.t.random("gun anime")

        embed_bang = discord.Embed(title=f":skull: {ctx.author.name} tire sur {member} !",
                                   color=discord.Colour.from_rgb(175, 32, 19),
                                   timestamp=ctx.message.created_at)

        embed_bang.set_image(url=bang_gif)
        await ctx.send(embed=embed_bang)

    @bang.error
    async def bang_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.author.name} cette commande est en recharge !')

    @commands.command(name="kiss", aliases=['bisous', 'kissing'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member = None):

        if member is None:
            member = self.client.user.name

        elif member == ctx.author:

            embed_kiss = discord.Embed(title=f":pleading_face: {ctx.author.name} a bien besoins d'un bisous !",
                                       color=discord.Colour.from_rgb(255, 0, 238),
                                       timestamp=ctx.message.created_at)

            embed_kiss.set_image(url="https://i.giphy.com/media/R25RGeYR5uWXe/giphy.webp")
            await ctx.send(embed=embed_kiss)
            return

        else:
            member = member.display_name

        kiss_gif = self.t.random("kiss anime")

        embed_kiss = discord.Embed(title=f":heartbeat:  {ctx.author.name} embrasse {member} !",
                                   color=discord.Colour.from_rgb(255, 0, 238),
                                   timestamp=ctx.message.created_at)

        embed_kiss.set_image(url=kiss_gif)
        await ctx.send(embed=embed_kiss)

    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.author.name} cette commande est en recharge !')

    @commands.command(name="pat", aliases=['headpat', 'caresser'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member = None):

        if member is None:
            member = self.client.user.name

        elif member == ctx.author:

            embed_pat = discord.Embed(title=f":pleading_face: {ctx.author.name} veut des pats !",
                                      color=discord.Colour.from_rgb(255, 0, 238),
                                      timestamp=ctx.message.created_at)

            embed_pat.set_image(url="https://c.tenor.com/WQtx7mtec-UAAAAd/pats-kitty.gif")
            await ctx.send(embed=embed_pat)
            return

        else:
            member = member.display_name

        pat_gif = self.t.random("pat anime")

        embed_pat = discord.Embed(title=f":wave: {ctx.author.name} donne des pats à {member} !",
                                  color=discord.Colour.from_rgb(255, 0, 238),
                                  timestamp=ctx.message.created_at)

        embed_pat.set_image(url=pat_gif)
        await ctx.send(embed=embed_pat)

    @pat.error
    async def pat_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.author.name} cette commande est en recharge !')

    @commands.command(name="hi", aliases=['salut', "wave"])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def hi(self, ctx, member: discord.Member = None):

        hi_gif = self.t.random("wave anime")

        if (member is None) or (member == ctx.author):

            embed_hi = discord.Embed(title=f":vulcan: {ctx.author.name} vous salut !",
                                     color=discord.Colour.from_rgb(255, 0, 238),
                                     timestamp=ctx.message.created_at)

            embed_hi.set_image(url=hi_gif)
            await ctx.send(embed=embed_hi)
            return

        else:
            member = member.display_name

        embed_hi = discord.Embed(title=f":wave: {ctx.author.name} salut {member} !",
                                 color=discord.Colour.from_rgb(255, 0, 238),
                                 timestamp=ctx.message.created_at)

        embed_hi.set_image(url=hi_gif)
        await ctx.send(embed=embed_hi)

    @hi.error
    async def hi_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.author.name} cette commande est en recharge !')

    @commands.command(name="hi", aliases=['salut', "wave"])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def hi(self, ctx, member: discord.Member = None):

        hi_gif = self.t.random("wave anime")

        if (member is None) or (member == ctx.author):

            embed_hi = discord.Embed(title=f":vulcan: {ctx.author.name} vous salut !",
                                     color=discord.Colour.from_rgb(255, 0, 238),
                                     timestamp=ctx.message.created_at)

            embed_hi.set_image(url=hi_gif)
            await ctx.send(embed=embed_hi)
            return

        else:
            member = member.display_name

        embed_hi = discord.Embed(title=f":wave: {ctx.author.name} salut {member} !",
                                 color=discord.Colour.from_rgb(255, 0, 238),
                                 timestamp=ctx.message.created_at)

        embed_hi.set_image(url=hi_gif)
        await ctx.send(embed=embed_hi)

    @hi.error
    async def hi_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.author.name} cette commande est en recharge !')


def setup(client):
    client.add_cog(Social(client))
