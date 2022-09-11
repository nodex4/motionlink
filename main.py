# import neccesarey libraries for discord.py
import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands
import typing
import discord.utils

# initialize diuscord token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")


# initialize bot
class Bot(commands.Bot):
    async def setup_hook(self):
        await bot.add_cog(Events(bot))    # Events
        await load_extensions()


bot = Bot(command_prefix=('!'), intents=discord.Intents.all(),
          application_id="977995844097802240")


# style stuff
pri = '\033[0;0m'  # reset color
sec = '\033[1;34m'  # secondary color
acc = '\033[1;36m'  # accent color


# create event cog
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        cls()
        print(f"""\n{pri}MotionLink is online and connected to: """)
        print(f"""----------------------------------------------------""", end=' ')
        # guild = discord.utils.get(bot.guilds)
        for guild in bot.guilds:
            print(f"""\n{sec}{guild.name} {acc}[{guild.id}]""", end=' ')
        print(f"""\n{pri}----------------------------------------------------""")
        print(f"""\n{pri}Log:""")


# add a command to sync the command tree lcoally or globally
@bot.command()
async def sync(ctx, guilds: commands.Greedy[discord.Object]) -> None:
    if not guilds:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f">>> The command tree has been **globally** copied.")



if __name__ == "__main__":
    bot.run(TOKEN)