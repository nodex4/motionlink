# general libraries
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries
import test


# create test cog
class Test(commands.GroupCog, name="test"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        super().__init__()

    @app_commands.command(name="one")
    @app_commands.describe(var="Something to help udnerstand the variable.")
    async def coin(self, interaction, var: str) -> None:
        """ Do test one stuff... """
        await interaction.response.send_message(f"**test two happened** {var}")

    @app_commands.command(name="two")
    async def dice(self, interaction) -> None:
        """ Do some test two stuff. """
        await interaction.response.send_message("**test two happened**")


# setup function
async def setup(bot):
    await bot.add_cog(Test(bot))
