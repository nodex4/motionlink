# general libraries
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries



# create ping cong
class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="ping")
    @app_commands.describe(
    times="The amount of pings that should be conducted.",
    member="The user you wish to ping.",
    message="What the user should be told while being pinged.",
    ghost="If you want these pings do be ghost-pings."
)
    async def ping(self, interaction, times: int, member: discord.Member, message: str, ghost: bool = False) -> None:
        """ Ping a user because you dont wanna type. """
        if ghost:
            for i in range(times):
                await interaction.channel.send(f"Ayo {member.mention}, {message}", delete_after=3)
                #delete last message
        else:
            for i in range(times):
                await interaction.channel.send(f"Ayo {member.mention}, {message}")



# setup function
async def setup(bot):
    await bot.add_cog(Ping(bot))