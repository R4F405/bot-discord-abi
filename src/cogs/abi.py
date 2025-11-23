import discord
from discord import app_commands
from discord.ext import commands
try:
    from src.services.wiki_service import WikiService
    from src.utils.embeds import EmbedBuilder
except ImportError:
    from services.wiki_service import WikiService
    from utils.embeds import EmbedBuilder

class ABICommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.wiki_service = WikiService()

    # Crear un grupo de comandos /abi
    abi_group = app_commands.Group(name="abi", description="Comandos de Arena Breakout Infinite")

    @abi_group.command(name="municion", description="Busca información de munición")
    async def ammo(self, interaction: discord.Interaction, nombre: str):
        await interaction.response.defer()
        data = self.wiki_service.get_ammo_info(nombre)
        
        if data:
            embed = EmbedBuilder.create_ammo_embed(data)
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"No encontré información sobre munición '{nombre}' en la Wiki.")

    @abi_group.command(name="llave", description="Busca información de llaves")
    async def key(self, interaction: discord.Interaction, nombre: str):
        await interaction.response.defer()
        data = self.wiki_service.get_key_info(nombre)
        
        if data:
            embed = EmbedBuilder.create_key_embed(data)
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"No encontré información sobre la llave '{nombre}' en la Wiki.")

    @abi_group.command(name="mapa", description="Busca mapas")
    async def map(self, interaction: discord.Interaction, nombre: str):
        await interaction.response.defer()
        data = self.wiki_service.get_map_info(nombre)
        
        if data:
            embed = EmbedBuilder.create_image_embed(
                title=f"Mapa: {data['title']}",
                image_url=data['image'],
                url=data['url']
            )
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(f"No encontré información sobre el mapa '{nombre}' en la Wiki.")

async def setup(bot):
    await bot.add_cog(ABICommands(bot))
