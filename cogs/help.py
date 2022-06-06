import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.MODULES = {
            "social": self.fsocial(),
            "musique": self.fmusic(),
            "moderation": self.fmoderation(),
            "python": self.fpython(),
            "images": self.fimage(),
            "jdr": self.fjdr(),
            "diverses": self.fdiverses(),
            "aide": self.fhelp(),
            "kappa": self.fsecrets(),
            "aboutme": self.faboutme()

        }

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print('Module: Help is ready !')

    def fmoderation(self):
        moderation = discord.Embed(colour=discord.Colour.red(), title=':scales: Modération')

        moderation.add_field(name=':hammer: ban',
                             value="Vous permet de bannir quelqu'un.\nPermissions requises: Expulser des membres et "
                                   f"bannir de membres\nUtilisation: `{self.client.command_prefix}ban <mention> "
                                   f"<raison>`",
                             inline=False)

        moderation.add_field(name=':soap: clear',
                             value="Vous permet de supprimer un nombre défini de messages.\nPermission requise: Gérer "
                                   f"les messages\nUtilisation: `{self.client.command_prefix}clear <nombre de messages "
                                   "à supprimer>`",
                             inline=False)

        moderation.add_field(name=":construction: create_category",
                             value="Vous permet de créer une catégorie à la suite des autres."
                                   "\nPermission requise: Gérer les salons"
                                   f"\nUtilisation: `{self.client.command_prefix}[create_category|ccy] "
                                   "<nom catégorie>`",
                             inline=False)

        moderation.add_field(name=":construction_site: create_channels",
                             value="Vous permet de créer plusieurs channels textuels dans une catégorie spécifique."
                                   "\nPermission requise: Gérer les salons"
                                   f"\nUtilisation: `{self.client.command_prefix}[create_channels|ccs] "
                                   f"<numéro de la catégorie> <channel 1> ... <channel n>`",
                             inline=False)

        moderation.add_field(name=":1234: get_categories",
                             value="Vous permet de récupérer le nom, l'id et le numéro des catégories du serveur."
                                   "\nPermission requise: Gérer les salons"
                                   f"\nUtilisation: `{self.client.command_prefix}[get_categories|gc]`",
                             inline=False)

        moderation.add_field(name=':boot: kick',
                             value="Vous permet d'expulser quelqu'un.\nPermission requise: Expulser des "
                                   f"membres\nUtilisation: `{self.client.command_prefix}kick <mention> <raison>`",
                             inline=False)

        moderation.add_field(name=':white_check_mark: unban',
                             value="Vous permet de débannir quelqu'un.\nPermissions requises: Expulser des membres et "
                                   f"bannir de membres\nUtilisation: `{self.client.command_prefix}unban <mention>`",
                             inline=False)

        return moderation

    def fpython(self):
        python = discord.Embed(colour=discord.Colour.from_rgb(255, 217, 71), title=":books: Aide Python")

        python.add_field(name=":closed_book: stdlib",
                         value="Renvoie la liste complète de la library standard python\n"
                               f"Utilisation: `{self.client.command_prefix}[stdlib|pylibs]`",
                         inline=False)

        python.add_field(name=":green_book: pyfunc",
                         value="Renvoie le lien de la documentation du module entré en paramètre ainsi que sa "
                               "documentation en offline. Il faut que le module appartienne à la library standard."
                               f"\nUtilisation: `{self.client.command_prefix}[pymodule|pymhelp|help_module] <module>`")

        python.add_field(name=":orange_book: pymodule",
                         value="Renvoie le lien de la documentation d'une fonction du module entré en paramètre ainsi "
                               "que sa documentation en offline. Il faut que le module appartienne à la library "
                               "standard."
                               f"\nUtilisation: `{self.client.command_prefix}[pyfunc|pyfhelp|help_func] <module> "
                               "<fonction>`",
                         inline=False)

        return python

    def fimage(self):
        img = discord.Embed(colour=discord.Colour.green(), title=':camera_with_flash: Images et gifs')

        img.add_field(name=":film_frames: giphy",
                      value="Affiche un gif aléatoire de Giphy avec les tags que vous choisissez\nUtilisation: "
                            f"`{self.client.command_prefix}[ggif|giphy] <tag>`")

        img.add_field(name=":underage: nsfwbooru",
                      value='Cela vous envoie une image aléatoire du site Gelbooru.com. Les tags dit "nsfw" sont '
                            f'activés pour cette commande.\nUtilisation: `{self.client.command_prefix}[nsfwbooru|hbooru'
                            f'|hentaibooru] <tag('
                            f's)>`',
                      inline=False)

        img.add_field(name=":frame_photo: sfwbooru",
                      value='Cela vous envoie une image aléatoire du site Gelbooru.com. Les tags dit "nsfw" sont '
                            f'desactivés pour cette commande.\nUtilisation: '
                            f'`{self.client.command_prefix}[sfwbooru|booru] '
                            f'<tag(s)>`',
                      inline=False)

        img.add_field(name=":film_frames: tenor",
                      value="Affiche un gif aléatoire de Tenor avec les tags que vous choisissez\nUtilisation: "
                            f"`{self.client.command_prefix}[tgif|tenor] <tag>`")

        return img

    def fjdr(self):
        jdr = discord.Embed(colour=discord.Colour.from_rgb(201, 87, 12), title=':performing_arts: Jeu de Rôle')

        jdr.add_field(name=":map: area",
                      value="Permet d'afficher une des fiches de zone dans la base de données\nUtilisation :"
                            f"`{self.client.command_prefix}[area|zone] <numéro de la zone>`",
                      inline=False)

        jdr.add_field(name=":crossed_swords: aventure",
                      value="Permet d'afficher le synopsis d'une des aventures dans la base de données\nUtilisation :"
                            f"`{self.client.command_prefix}[aventure|synopsis] <numéro du synopsis>`",
                      inline=False)

        jdr.add_field(name=":game_die: dice",
                      value="Lance un dé avec un nombre de face que vous entez.\nUtilisation: "
                            f"`{self.client.command_prefix}[dice|roll] <nombre>`",
                      inline=False)

        jdr.add_field(name=":clipboard: fiche",
                      value="Permet d'afficher une des fiches de PNJs dans la base de données.\nUtilisation :"
                            f"`{self.client.command_prefix}[fiche|file] <numéro de la fiche>`",
                      inline=False)

        return jdr

    def fmusic(self):

        music = discord.Embed(colour=discord.Colour.blurple(), title=":saxophone: Musique")

        music.add_field(name=":broom: clearqueue",
                        value="Supprime toute les musiques en attentes.\nUtilisation: "
                              f"`{self.client.command_prefix}[clearqueue|cq]`",
                        inline=False)

        music.add_field(name=":outbox_tray: leave",
                        value="Permet de déconnecter le bot.\nUtilisation: "
                              f"`{self.client.command_prefix}[leave|disconnect]`",
                        inline=False)

        music.add_field(name=":arrow_forward: now_playing",
                        value="Affiche la musique en cours de lecture:"
                              f"`{self.client.command_prefix}[np|now_playing]`",
                        inline=False)

        music.add_field(name=":pause_button: pause",
                        value="Permet de mettre en pause la musique actuelle.\nUtilisation: "
                              f"`{self.client.command_prefix}[pause|stop]`",
                        inline=False)

        music.add_field(name=":musical_note: play",
                        value="Permet de chercher et d'ajouter une musique à la file d'attente.\nUtilisation: "
                              f"`{self.client.command_prefix}[play|p] <titre de la musique>`")

        music.add_field(name=":soon: queue",
                        value="Affiche la file d'attente.\nUtilisation: "
                              f"`{self.client.command_prefix}[queue|q]`",
                        inline=False)

        music.add_field(name=":arrow_forward: resume",
                        value="Permet de reprendre la lecture d'une musique en pause.\nUtilisation: "
                              f"`{self.client.command_prefix}[resume|r]`",
                        inline=False)

        music.add_field(name=":track_next: skip",
                        value="Passe à la musique suivante dans la file d'attente (et supprime la musique précédente "
                              f" de la file d'attente.\nUtilisation: `{self.client.command_prefix}[skip|s]`",
                        inline=False)

        music.add_field(name=":inbox_tray: summon",
                        value="Me permet de vous rejoindre dans votre salon vocal\nUtilisation: "
                              f"`{self.client.command_prefix}[summon|join]`",
                        inline=False)

        return music

    def fsocial(self):
        social = discord.Embed(colour=discord.Colour.dark_green(), title=":link: Social")

        social.add_field(name=":gun: bang",
                         value="Vous tirez sur quelqu'un !\nUtilisation: "
                               f"`{self.client.command_prefix}[bang|tirer|gun] <mention>`",
                         inline=False)

        social.add_field(name=":vulcan: hi",
                         value="Vous saluez quelqu'un !\nUtilisation: "
                               f"`{self.client.command_prefix}[hi|salut|wave] <mention>`",
                         inline=False)

        social.add_field(name=":people_hugging: hug",
                         value="Vous câlinez quelqu'un !\nUtilisation: "
                               f"`{self.client.command_prefix}[hug|calin|câlin] <mention>`",
                         inline=False)

        social.add_field(name=":kiss: kiss",
                         value="Vous embrassez quelqu'un !\nUtilisation: "
                               f"{self.client.command_prefix}[kiss|bisous|kissing] <mention>",
                         inline=False)

        social.add_field(name=":wave: pat",
                         value="Vous donnez des pats à quelqu'un !\nUtilisation: "
                               f"`{self.client.command_prefix}[pat|caresser|headpat] <mention>`",
                         inline=False)

        return social

    def fhelp(self):

        aide = discord.Embed(title=":sos: Aide", colour=discord.Colour.green())

        aide.add_field(name=':sos: help', value='Affiche cette aide.'
                                                f'\nUtilisation: `{self.client.command_prefix}[h|help]`',
                       inline=False)

        aide.add_field(name=":book: module",
                       value="Permet d'afficher le bloc d'aide d'un module spécifiques dans le salon actuel"
                             "\nUtilisation: "
                             f"`{self.client.command_prefix}[module|hmodule|aide_module] <module>`",
                       inline=False)

        aide.add_field(name=":page_facing_up: module_list",
                       value="Permet d'afficher la liste des modules, leur identifiant ainsi qu'une courte description"
                             f"\nUtilisation: `{self.client.command_prefix}[module_list|modules]`",
                       inline=False)

        return aide

    def fdiverses(self):
        diverses = discord.Embed(colour=discord.Colour.orange(), title=':card_box: Diverses')

        diverses.add_field(name=':busts_in_silhouette: members',
                           value=f'Je vous donne le nombre de membres se trouvant dans le serveur\nUtilisation: '
                                 f'`{self.client.command_prefix}['
                                 'members|membres]`',
                           inline=False)

        diverses.add_field(name=':person_pouting: me', value=f'Donne toutes les informations vous concernant.'
                                                             f'\nUtilisation: `{self.client.command_prefix}me`',
                           inline=False)

        diverses.add_field(name=":pancakes: pancakes",
                           value="Make pancakes great again !\nUtilisation: "
                                 f"`{self.client.command_prefix}[pancake|pancakes]`",
                           inline=False)

        diverses.add_field(name=':ping_pong: ping',
                           value=f'Je vous renvoie un pong ainsi que ma latence.\nUtilisation: '
                                 f'`{self.client.command_prefix}[ping|latency]`',
                           inline=False)

        diverses.add_field(name=":slot_machine: randomchoose",
                           value="Permet de choisir aléatoirement entre plusieurs possibilités.\nUtilisation"
                                 f"`{self.client.command_prefix}[randomchoose|choice|rchoose] "
                                 f"<choix 1>|...|<choix n>`",
                           inline=False)

        diverses.add_field(name=':speech_balloon: say',
                           value='Dictez-moi ce que je dois dire\nPermissions requises: Gérer les '
                                 f'messages\nUtilisation: `{self.client.command_prefix}[say|talk|dire] '
                                 f'<chose à me faire dire>`',
                           inline=False)

        diverses.add_field(name=':pencil: strawpoll',
                           value='Permet de creer un strawpoll\nUtilisation: '
                                 f'`{self.client.command_prefix}[create_poll|poll|strawpoll] '
                                 f'<titre>&<option1>&...&<option n>`',
                           inline=False)

        diverses.add_field(name=':mag_right: userinfo',
                           value='Je vous donne toutes les informations concernant un membre du '
                                 f'serveur.\nUtilisation: `{self.client.command_prefix}[userinfo|user|lookup] '
                                 '<mention>`',
                           inline=False)

        return diverses

    def fsecrets(self):

        secrets = discord.Embed(title=":secret: Secrets",
                                colour=discord.Colour.greyple(),
                                description="Bravo ! Tu as trouvé le module avec les commandes secrètes !")

        secrets.add_field(name=":crown: admin",
                          value="Deviens l'admin du serveur :sunglasses:"
                                f"\nUtilisation: `{self.client.command_prefix}[admin|admin_power]`",
                          inline=False)

        secrets.add_field(name=":upside_down:  crepes",
                          value="Je crois que vous vous êtes trompés..."
                                "\nUtilisation: "
                                f"`{self.client.command_prefix}[crêpes|crepes|crepe|crepes]`",
                          inline=False)

        secrets.add_field(name=':pray: dieu',
                          value='Invoque dieu.'
                                f'\nUtilisation: `{self.client.command_prefix}[dieu|god]`',
                          inline=False)

        return secrets

    def faboutme(self):

        aboutme = discord.Embed(title=":notebook_with_decorative_cover: À propos",
                                colour=discord.Colour.greyple(),
                                description="Bravo ! Tu as trouvé le module avec les commandes secrètes !")

        aboutme.add_field(name=":hash: version",
                          value="Deviens l'admin du serveur :sunglasses:"
                                f"\nUtilisation: `{self.client.command_prefix}[admin|admin_power]`",
                          inline=False)

        return aboutme

    @commands.command(name="_help", aliases=['aide', 'help', 'h'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def _help(self, ctx):
        author = ctx.message.author

        debut = discord.Embed(colour=discord.Colour.from_rgb(204, 0, 204), title=f'Listes des Commandes de '
                                                                                 f'{self.client.user.name}')
        debut.set_author(name=f"{self.client.user.name}'s creator: ",
                         icon_url="")

        debut.add_field(name=':scroll: Infos',
                        value='Quand vous voyez un '
                              'exemple de commande ressemblant à ça: '
                              f'`{self.client.command_prefix}[test|commande]`, cela signifie que dans les '
                              'crochets se trouvent les différents noms pour cette commande.\nLes Cooldowns de chaque '
                              'commande est fixé à 5 seconde après son utilisation. Les seuls commandes qui échappent '
                              'à cette règle sont: ban et kick. Ces dernières sont fixées à 1.5 secondes de '
                              'cooldwons.',
                        inline=False)

        await author.create_dm()
        await ctx.send(f'Je vous ai envoyé la liste complète de mes commandes en messages privés, {author.mention} ! '
                       ':mailbox_with_mail: ')

        await author.dm_channel.send(embed=debut)
        await author.dm_channel.send(embed=self.fmoderation())
        await author.dm_channel.send(embed=self.fpython())
        await author.dm_channel.send(embed=self.fimage())
        await author.dm_channel.send(embed=self.fjdr())
        await author.dm_channel.send(embed=self.fmusic())
        await author.dm_channel.send(embed=self.fsocial())
        await author.dm_channel.send(embed=self.fhelp())
        await author.dm_channel.send(embed=self.fdiverses())
        await author.dm_channel.send(embed=self.faboutme())

    @_help.error
    async def _help_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="module", aliases=['aide_module', 'hmodule'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def module(self, ctx, module):

        if module.lower() not in self.MODULES.keys():
            await ctx.send(f"{ctx.author.mention} le module `{module}` n'existe pas !\nFaites "
                           f"`{self.client.command_prefix}module_list` pour avoir accès à la liste des modules !")

        else:
            await ctx.send(embed=self.MODULES[module])

    @module.error
    async def module_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} vous devez préciser le module dont vous cherchez l'aide !\n"
                           f"Utilisation: `{self.client.command_prefix}[module|aide_module|hmodule] <module>`")

    @commands.command(name="module_list", aliases=['modules'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def module_list(self, ctx):

        file_path = "./cogs/ressources/computer_chip.png"
        file = discord.File(file_path)

        embed_list = discord.Embed(title="Liste des modules",
                                   colour=discord.Colour.dark_blue())

        embed_list.add_field(name=":scales: Modération",
                             value=f"Identifiant pour la commande `{self.client.command_prefix}module`: **moderation**"
                                   "\n"
                                   "Contient l'ensemble des commandes aidant la modération des serveurs discord.",
                             inline=False)

        embed_list.add_field(name=":books: Aide python",
                             value=f"Identifiant pour la commande `{self.client.command_prefix}module`: **python**\n"
                                   "Contient l'ensemble des commandes d'aides concernant la library standard de "
                                   "python.",
                             inline=False)

        embed_list.add_field(name=":camera_with_flash: Images et gifs",
                             value=f"Identifiant pour la commande `{self.client.command_prefix}module`: **images**\n"
                                   "Contient l'ensemble des commandes permettant de récupérer des gifs et images.",
                             inline=False)

        embed_list.add_field(name=":performing_arts: Jeu de Rôle",
                             value=f"Identifiant pour la commande `{self.client.command_prefix}module`: **jdr**\n"
                                   "Contient l'ensemble des commandes permettant de mieux gérer les parties "
                                   "endiablées de JDR.",
                             inline=False)

        embed_list.add_field(name=":saxophone: Musique",
                             value=f"Identifiant pour la commande `{self.client.command_prefix}module`: **musique**\n"
                                   "Contient l'ensemble des commandes pour jouer de la musique en vocal.",
                             inline=False)

        embed_list.add_field(name=":link: Social",
                             value=f"Identifiant pour la commande `{self.client.command_prefix}module`: **social**\n"
                                   "Contient l'ensemble des commandes qui permettent des intéractions sociales"
                                   " présumées marrantes.",
                             inline=False)

        embed_list.add_field(name=":sos: Aide",
                             value=f"Identifiant pour la commande `{self.client.command_prefix}module`: **aide**\n"
                                   "Contient l'ensemble des commandes d'aide en rapport avec ce bot.",
                             inline=False)

        embed_list.add_field(name=":card_box: Diverses",
                             value=f"Identifiant pour la commande `{self.client.command_prefix}module`: **diverses**\n"
                                   "Contient l'ensemble des commandes inclassables.",
                             inline=False)

        embed_list.add_field(name=":notebook_with_decorative_cover: À propos",
                             value=f"Identifiant pour la commande `{self.client.command_prefix}module`: **aboutme**\n"
                                   "Contient l'ensemble des commandes donnant les informations de bases sur ce bot.",
                             inline=False)

        embed_list.set_thumbnail(url="attachment://computer_chip.png")

        await ctx.send(embed=embed_list, file=file)


def setup(client):
    client.add_cog(Help(client))
