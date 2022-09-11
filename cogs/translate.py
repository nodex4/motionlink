# general libraries
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries
from translate import Translator
from langdetect import detect



# create translate cog
class Translate(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="chinese")
    @app_commands.describe(
        text="The text that should be translated."
    )
    async def chinese(self, interaction, text: str) -> None:
        """ Translate text between english and chinese """
        language = detect("text")
        if language == "en":
            translator = Translator(from_lang="english", to_lang="chinese")
        else:
            translator = Translator(from_lang="chinese", to_lang="english")

        translation = translator.translate(text)
        await interaction.response.send_message(f">>> {translation}", ephemeral=True)


# setup function
async def setup(bot):
    await bot.add_cog(Translate(bot))