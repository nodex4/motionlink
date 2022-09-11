# general libraries
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries
import typing


# create server cog
class Server(commands.GroupCog, name="server"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        super().__init__()

    
    @app_commands.command(name="setup")
    @app_commands.checks.has_permissions(administrator=True)
    async def server_setup(self, interaction) -> None:
        """ Let MotionLink setup your server's channels and roles. """
        await interaction.response.send_message("> Server **Setup** Starting in:")
        await interaction.channel.send("> **3**")
        time.sleep(1)
        await interaction.channel.send("> **2**")
        time.sleep(1)
        await interaction.channel.send("> **1**")
        time.sleep(1)
        try:
            for c in interaction.guild.channels:
                await c.delete()
            for r in interaction.guild.roles:
                await r.delete()
            for c in interaction.guild.categories:
                await c.delete()
        except:
            pass


        await interaction.guild.create_category("『 IMPORTANT 』")
        important = discord.utils.get(interaction.guild.categories, name="『 IMPORTANT 』")
        await interaction.guild.create_text_channel("💬》welcome", category=important)
        await interaction.guild.create_text_channel("⚠️》rules", category=important)
        await interaction.guild.create_text_channel("🔈》announcements", category=important)

        await interaction.guild.create_category("『 General 』")
        general = discord.utils.get(interaction.guild.categories, name="『 General 』")
        await interaction.guild.create_text_channel("💬》general", category=general)
        await interaction.guild.create_voice_channel("🎙️》general", category=general)



    @app_commands.command(name="purge")
    @app_commands.checks.has_permissions(administrator=True)
    async def server_purge(self, interaction, specific: typing.Literal['channels', 'roles', 'categories']) -> None:
        """ Delete all channels and roles in a server. """
        await interaction.response.send_message("> Server **Purge** Starting in:")
        await interaction.channel.send("> **3**")
        time.sleep(1)
        await interaction.channel.send("> **2**")
        time.sleep(1)
        await interaction.channel.send("> **1**")
        time.sleep(1)

        if specific.lower() == "channels":
            try:
                for c in interaction.guild.channels:
                    await c.delete()
            except:
                pass
        if specific.lower() == "roles":
            try:
                for r in interaction.guild.roles:
                    await r.delete()
            except:
                pass
        if specific.lower() == "categories":
            try:
                for r in interaction.guild.categories:
                    await r.delete()
            except:
                pass
        else:
            try:
                for c in interaction.guild.channels:
                    await c.delete()
                for r in interaction.guild.roles:
                    await r.delete()
                for c in interaction.guild.categories:
                    await c.delete()
            except:
                pass

# setup function
async def setup(bot):
    await bot.add_cog(Server(bot))