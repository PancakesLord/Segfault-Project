import discord
import sys

from discord.ext import commands


class CogPython(commands.Cog):
    def __init__(self, client):
        self.client = client

        temp = list(sys.builtin_module_names)

        for i in range(len(temp)):
            if temp[i][0] == "_":
                temp[i] = temp[i][1:]

        self.std_lib = sorted(temp)
        temp = None

        self.help_function_x = ""
        self.char = "'"

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print("Module: Python Helper is ready !")

    @commands.command(name="pyflist", aliases=["function_list"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def pyflist(self, ctx, module):

        module = module.strip()

        self.help_function_x = [f for f in dir(module) if f[0:2] != "__"]

        result = ""
        result_old = ""
        i = 1

        for word in self.help_function_x:
            result += word + "\n"
            if len(result) >= 4000:
                embed_flist = discord.Embed(colour=discord.Colour.from_rgb(255, 217, 71),
                                            title=f'Ensembles des fonctions du module `{module}` (page {i})',
                                            description=f"{result_old}")

                await ctx.send(embed=embed_flist)

                i += 1
                result = ""
                result_old = ""

            result_old += word + "\n"

        if len(result) > 0:
            embed_flist = discord.Embed(colour=discord.Colour.from_rgb(255, 217, 71),
                                        title=f'Ensembles des fonctions du module `{module}` (page {i})',
                                        description=f"{result_old}")

            await ctx.send(embed=embed_flist)

    @commands.command(name="stdlib", aliases=["pylibs"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def stdlib(self, ctx):

        result = ""
        result_old = ""
        i = 1

        for word in self.std_lib:
            result += word + "\n"
            if len(result) >= 4000:
                embed_module = discord.Embed(colour=discord.Colour.from_rgb(255, 217, 71),
                                             title=f'Ensembles des fonctions des modules de la librairie standard'
                                                   f' (page {i})',
                                             description=f"{result_old}")

                await ctx.send(embed=embed_module)

                i += 1
                result = ""
                result_old = ""

            result_old += word + "\n"

        if len(result) > 0:
            embed_module = discord.Embed(colour=discord.Colour.from_rgb(255, 217, 71),
                                         title=f'Ensembles des fonctions des modules de la librairie standard'
                                               f' (page {i})',
                                         description=f"{result_old}")

            await ctx.send(embed=embed_module)

    @stdlib.error
    async def stdlib_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} cette commande est en cooldown !")

    @commands.command(name="pymodule", aliases=['pymhelp', 'help_module'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def pymodule(self, ctx, module):

        try:
            exec(f"import {module}")
            exec(f"self.help_function_x = {module}.__doc__")
            url = f"https://docs.python.org/3/library/{module}.html"

            self.help_function_x = self.help_function_x.split(" ")
            result = ""
            result_old = ""
            i = 1

            for word in self.help_function_x:
                result += word + "\n"
                if len(result) >= 4000:
                    embed_module = discord.Embed(colour=discord.Colour.from_rgb(255, 217, 71),
                                                 title=f'Documentation offline du module `{module}` (page {i})',
                                                 description=f"{result_old}")

                    await ctx.send(embed=embed_module)

                    i += 1
                    result = ""
                    result_old = ""

                result_old += word + "\n"

            if len(result) > 0:
                embed_module = discord.Embed(colour=discord.Colour.from_rgb(255, 217, 71),
                                             title=f'Documentation offline du module `{module}` (page {i})',
                                             description=f"{result_old}")

                await ctx.send(embed=embed_module)

            embed_module = discord.Embed(title=f'{ctx.author.name} voici la documentation en ligne du'
                                               f' module `{module}`',
                                         description=f'\n{url}',
                                         colour=discord.Colour.from_rgb(255, 217, 71))

            await ctx.send(embed=embed_module)

        except ModuleNotFoundError:
            ctx.send(f"{ctx.author.name} ce module n'existe pas dans la library standard !\n"
                     f"Voici la liste des modules de la library standards: "
                     f'{str(self.std_lib).replace("[", "```").replace("]", "```").replace(self.char, "")}')

    @pymodule.error
    async def pymodule_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} précisez le module dont vous voulez la documentation !\nUtilisation: "
                           f"`{self.client.command_prefix}[pymodule|pyhelp|help_module] <module>`")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} cette commande est en cooldown !")

    @commands.command(name="pyfunc", aliases=['help_func'])  # Commandes
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def pyfunc(self, ctx, module, function):

        try:
            exec(f"import {module}")
            exec(f"self.help_function_x = {module}.{function}.__doc__")
            url = f"https://docs.python.org/3/library/{module}.html#{module}.{function}"

            self.help_function_x = self.help_function_x.split(" ")
            i = 1
            result = ""
            result_old = ""

            for word in self.help_function_x:
                result += word + "\n"

                if len(result) >= 4000:
                    embed_function = discord.Embed(colour=discord.Colour.from_rgb(255, 217, 71),
                                                   title=f'Documentation offline de la fonction `{function}` '
                                                         f'du module `{module}` (page {i})',
                                                   description=f"{result_old}")

                    await ctx.send(embed=embed_function)

                    i += 1
                    result = ""
                    result_old = ""

                result_old += word + "\n"

            if len(result) > 0:
                embed_function = discord.Embed(colour=discord.Colour.from_rgb(255, 217, 71),
                                               title=f'Documentation offline de la fonction `{function}` '
                                                     f'du module {module} (page {i})',
                                               description=f"{result}")

                await ctx.send(embed=embed_function)

            embed_function = discord.Embed(title=f'{ctx.author.name} voici la documentation en ligne de la fonction '
                                                 f'`{function} module `{module}`',
                                           description=f'\n{url}',
                                           colour=discord.Colour.from_rgb(255, 217, 71))

            await ctx.send(embed=embed_function)

        except ModuleNotFoundError:
            await ctx.send(f"{ctx.author.mention} ce module n'existe pas dans la library standard !\n"
                           f"Voici la liste des modules de la library standards: "
                           f"{str(self.std_lib).replace('[', '```').replace(']', '```')}")

        except NameError:
            await ctx.send(f"{ctx.author.mention} cette fonction n'appartiens pas au module {module} !")

    @pyfunc.error
    async def pyfunc_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} précisez le module et la fonction dont vous voulez la documentation !"
                           f"\nUtilisation: `{self.client.command_prefix}[pyfunc|pyfhelp|help_func] "
                           f"<module> <fonction>`")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} cette commande est en cooldown !")


def setup(client):
    client.add_cog(CogPython(client))
