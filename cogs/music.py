# general libraries
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import nacl


# create music cog
class Music(commands.GroupCog, name="music"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        super().__init__()

    @app_commands.command(name="play")
    @app_commands.describe(
        song="Which song / playlist would you like to play?"
    )
    async def music_play(self, interaction, song: str) -> None:
        """ Play any song you want using motionlink."""
        channel = interaction.user.voice.channel
        voice = discord.utils.get(interaction.guild.voice_client, guild=interaction.guild)
        voice = interaction.guild.voice_client
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        await interaction.response.defer()
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        if not voice.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(song, download=False)
            song = info['url']
            voice.play(FFmpegPCMAudio(song, **FFMPEG_OPTIONS))
            voice.is_playing()
            await interaction.followup.send(">>> Bot is playing")
        else:
            await interaction.followup.send(">>> Bot is already playing")

#     @app_commands.command(name="image")
#     @app_commands.describe(
#     prompt="Type in what you want the AI to turn into a graphical illustration."
# )
#     async def ai_image(self, interaction, prompt: str) -> None:
#         """ Inquire an AI to turn your prompt into a graphical illustration. """
#         # await interaction.response.send_message("this funciton is not made yet")
#         await interaction.response.defer()

#         # msg = await ctx.send(f"“{prompt}”\n> Generating...")

#         model = replicate.models.get("stability-ai/stable-diffusion")
#         image = model.predict(prompt=prompt)[0]
#         await interaction.followup.send(f">>> {image}")


# setup function
async def setup(bot):
    await bot.add_cog(Music(bot))
