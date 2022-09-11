# general libraries
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries
import random

# create random cog
class Random(commands.GroupCog, name="random"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        super().__init__()

    @app_commands.command(name="coin")
    async def coin(self, interaction) -> None:
        """ Flip a coin. """
        sides = ["heads", "tails"]
        choice = random.choice(sides)
        # await ctx.send(f"The coin landed on **{choice}**.")
        await interaction.response.send_message(f"The coin landed on **{choice}**.")

    @app_commands.command(name="dice")
    async def dice(self, interaction) -> None:
        """ Roll a dice with six sides. """
        choice = random.randrange(6)
        await interaction.response.send_message(f"The dice landed on **{choice}**.")


# setup function
async def setup(bot):
    await bot.add_cog(Random(bot))