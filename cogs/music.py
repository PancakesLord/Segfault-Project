import discord

from youtube_dl import YoutubeDL
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

        # all the music related stuff
        self.is_playing = False
        self.is_paused = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio/best',
                            'extractaudio': True,
                            'audioformat': 'mp3',
                            'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                            'restrictfilenames': True,
                            'noplaylist': True,
                            'nocheckcertificate': True,
                            'ignoreerrors': False,
                            'logtostderr': False,
                            'quiet': True,
                            'no_warnings': True,
                            'default_search': 'auto',
                            'source_address': '0.0.0.0', }

        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                               'options': '-vn'}

        self.vc = None

    # searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
                print(info)
            except Exception as e:
                print(e)
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            # get the first url
            m_url = self.music_queue[0][0]['source']

            # remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())

        else:
            self.is_playing = False

    # infinite loop checking
    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            # try to connect to voice channel if you are not already connected
            if self.vc is None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()

                # in case we fail to connect
                if self.vc is None:
                    await ctx.send("Je n'arrive pas à me connecter au salon vocal !")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])

            # remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print('Module: Music is ready !')

    @commands.command(name="summon", aliases=["join"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def summon(self, ctx):
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            # you need to be connected so that the bot knows where to go
            await ctx.send("Vous devez être connecté à un salon vocal !")

        else:
            await voice_channel.connect()

    @summon.error
    async def summon_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")

    @commands.command(name="play", aliases=["p"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def play(self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            # you need to be connected so that the bot knows where to go
            await ctx.send("Vous devez être connecté à un salon vocal !")

        elif self.is_paused:
            self.vc.resume()

        else:
            song = self.search_yt(query)
            if type(song) == bool:
                await ctx.send("Je n'arrive pas à lancer la musique.")

            else:
                await ctx.send(f"La musique: `{song['title']}` a bien été ajouté à la file d'attente !")
                self.music_queue.append([song, voice_channel])

                if not self.is_playing:
                    await self.play_music(ctx)

    @play.error
    async def play_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention} il manque des arguments !\nUtilisation: "
                           f"`{self.client.command_prefix}[play|p] <titre music>`")

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")

    @commands.command(name="pause", aliases=["stop"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def pause(self, ctx):
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.vc.pause()

        elif self.is_paused:
            await ctx.send(f"La musique est déjà en pause ! Faites `{self.client.command_prefix}[resume|r]`"
                           " pour la relancer.")

    @pause.error
    async def pause_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")

    @commands.command(name="resume", aliases=["r"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def resume(self, ctx):
        if self.is_paused:
            self.vc.resume()

        else:
            await ctx.send("La musique n'est pas en pause !")

    @resume.error
    async def resume_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")

    @commands.command(name="skip", aliases=["s"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def skip(self, ctx):
        if self.vc is not None and self.vc:
            self.vc.stop()
            # try to play next in the queue if it exists
            await self.play_music(ctx)

    @skip.error
    async def skip_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")

    @commands.command(name="queue", aliases=["q"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def queue(self, ctx):

        if len(self.music_queue) > 1:
            await ctx.send(f"Actuellement jouée: {self.music_queue[0][0]['title']}")

            for i in range(1, len(self.music_queue)):
                await ctx.send(f"{i - 1}) {self.music_queue[i][0]['title']}")

        elif len(self.music_queue) == 1:
            await ctx.send(f"Actuellement jouée: {self.music_queue[0][0]['title']}")

        else:
            await ctx.send("Aucune musique présente dans la file d'attente !")

    @queue.error
    async def queue_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")

    @commands.command(name="clearqueue", aliases=["cq"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def clearqueue(self, ctx):

        self.music_queue = [self.music_queue[0]]
        await ctx.send("La file d'attente a bien été vidée !")

    @clearqueue.error
    async def clearqueue_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")

    @commands.command(name="leave", aliases=["disconnect"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def leave(self, ctx):
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()

    @leave.error
    async def leave_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")

    @commands.command(name="now_playing", aliases=["np"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def now_playing(self, ctx):
        if len(self.music_queue) > 0:
            await ctx.send(f"Actuellement jouée: {self.music_queue[0][0]['title']}")

        else:
            await ctx.send(f"Aucune musique n'est actuellement entrain de se jouer.")

    @now_playing.error
    async def now_playing_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} du calme ! La commande est en cooldown !")


def setup(client):
    client.add_cog(Music(client))
