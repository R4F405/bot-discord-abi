import discord
import asyncio
import os
from dotenv import load_dotenv
from discord.ext import commands

# Cargar variables de entorno
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos slash.")
    except Exception as e:
        print(f"Error sincronizando comandos: {e}")
    print('------')

async def load_extensions():
    try:
        # Intentar cargar como si estuviéramos dentro de src/
        await bot.load_extension('cogs.abi')
        print("Cog 'abi' cargado correctamente.")
    except commands.ExtensionNotFound:
        try:
            # Intentar cargar con prefijo src. si estamos en root
            await bot.load_extension('src.cogs.abi')
            print("Cog 'abi' cargado correctamente (src).")
        except Exception as e:
            print(f"Error cargando cog 'abi': {e}")
    except Exception as e:
        print(f"Error cargando cog 'abi': {e}")

async def main():
    if not DISCORD_TOKEN:
        print("Error: DISCORD_TOKEN no configurado en .env")
        return

    async with bot:
        await load_extensions()
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Manejo limpio de Ctrl+C
        pass
