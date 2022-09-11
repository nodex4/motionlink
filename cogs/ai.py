# general libraries
import os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
import discord.utils

# cog specific libraries
import openai
import replicate



load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# create ai cog
class AI(commands.GroupCog, name="ai"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        super().__init__()

    @app_commands.command(name="text")
    @app_commands.describe(
    inquirie="Type in what you want to ask / inquire the ai with."
)
    async def ai_text(self, interaction, inquirie: str) -> None:
        """ Inquire an AI to correct, create, or interact with text. """
        await interaction.response.defer()
        response = openai.Completion.create(
          model="text-davinci-002",
          prompt=inquirie,
          temperature=0.3,
          max_tokens=2048,
          top_p=1.0,
          frequency_penalty=0.8,
          presence_penalty=0.0
        )
        response = response["choices"][0]["text"].split("\n",2)[2]
        await interaction.followup.send(f">>> {response}")

    @app_commands.command(name="image")
    @app_commands.describe(
    prompt="Type in what you want the AI to turn into a graphical illustration."
)
    async def ai_image(self, interaction, prompt: str) -> None:
        """ Inquire an AI to turn your prompt into a graphical illustration. """
        # await interaction.response.send_message("this funciton is not made yet")
        await interaction.response.defer()

        # msg = await ctx.send(f"“{prompt}”\n> Generating...")

        model = replicate.models.get("stability-ai/stable-diffusion")
        image = model.predict(prompt=prompt)[0]
        await interaction.followup.send(f">>> {image}")


# setup function
async def setup(bot):
    await bot.add_cog(AI(bot))