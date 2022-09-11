# general libraries
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries
import test


# create trop cog
class Test(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="test")
    @app_commands.describe(
        number="Choose a number.",
        member="Choose a member."
    )
    async def ping(self, interaction, number: int, member: discord.Member) -> None:
        """ This is the description for the cog command """
        interaction.response.defer()
        interaction.followup.send(">>>Testing...")


# setup function
async def setup(bot):
    await bot.add_cog(Test(bot))
