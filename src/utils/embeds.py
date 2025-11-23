import discord

class EmbedBuilder:
    @staticmethod
    def create_basic_embed(title, description, url=None, color=discord.Color.blue()):
        embed = discord.Embed(title=title, description=description, color=color, url=url)
        embed.set_footer(text="Arena Breakout: Infinite Wiki Bot")
        return embed

    @staticmethod
    def create_image_embed(title, image_url, url=None, color=discord.Color.green()):
        embed = discord.Embed(title=title, color=color, url=url)
        if image_url:
            embed.set_image(url=image_url)
        embed.set_footer(text="Arena Breakout: Infinite Wiki Bot")
        return embed

    @staticmethod
    def create_ammo_embed(data):
        embed = discord.Embed(
            title=f"Munición: {data['title']}",
            url=data['url'],
            color=discord.Color.orange()
        )
        embed.add_field(name="Daño Base", value=data['base_damage'], inline=True)
        embed.add_field(name="Clase de Penetración", value=data['penetration'], inline=True)
        
        if data['image']:
            embed.set_thumbnail(url=data['image'])
            
        embed.set_footer(text="Datos extraídos de la Wiki")
        return embed

    @staticmethod
    def create_key_embed(data):
        embed = discord.Embed(
            title=f"Llave: {data['title']}",
            description=data['summary'],
            url=data['url'],
            color=discord.Color.gold()
        )
        if data['image']:
            embed.set_image(url=data['image'])
        return embed
