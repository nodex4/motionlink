# general libraries
import discord
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries
import test


# create terminal view
class SelectTest(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.select(placeholder = "Select a command...", min_values = 1, max_values = 1, options = [ 
            discord.SelectOption(
                label="11111",
                description="1111111111111111111111111111."
            ),
            discord.SelectOption(
                label="22222222",
                description="2222222222222222222222222222"
            ),
            discord.SelectOption(
                label="3333333",
                description="2222222222222222222222222222"
            )
        ]
    )

    async def select(self, interaction, select):
        global command
        command = select.values[0]
        await interaction.response.defer()
    
class ButtonTest(discord.ui.View):
    def __init__(self):
        super().__init__()
    

    @discord.ui.button(label='✘', style=discord.ButtonStyle.red, row=4)
    async def pressedN(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=">>> test", view=self)


    @discord.ui.button(label='0', style=discord.ButtonStyle.grey, row=4)
    async def pressed0(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=">>> test", view=self)

    @discord.ui.button(label='✔', style=discord.ButtonStyle.green, row=4)
    async def pressedY(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="test")
    async def test(self, interaction) -> None:
        """ Do test stuff """
        view = SelectTest()
        view2 = ButtonTest()
        await interaction.response.send_message(">>> some text", view=view, ephemeral=True)
        await interaction.followup.send(view=view2, ephemeral=True)
    




# setup function
async def setup(bot):
    await bot.add_cog(Test(bot))