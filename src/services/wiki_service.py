import fandom
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
WIKI_NAME = os.getenv("WIKI_NAME", "arena-breakout-infinite")

class WikiService:
    def __init__(self):
        fandom.set_wiki(WIKI_NAME)

    def search_page(self, query):
        """Busca una página en la wiki y devuelve el título más relevante."""
        try:
            results = fandom.search(query)
            if results:
                return results[0][0] # Retorna el título del primer resultado
            return None
        except Exception as e:
            print(f"Error buscando '{query}': {e}")
            return None

    def get_page_content(self, title):
        """Obtiene el objeto página de fandom."""
        try:
            return fandom.page(title)
        except Exception as e:
            print(f"Error obteniendo página '{title}': {e}")
            return None

    def get_ammo_info(self, query):
        """Obtiene información específica de munición."""
        title = self.search_page(query)
        if not title:
            return None

        page = self.get_page_content(title)
        if not page:
            return None

        # Fandom a veces no devuelve todo el HTML estructurado en 'content', 
        # así que hacemos una petición directa para parsear con BS4 si es necesario.
        # Sin embargo, fandom-py tiene .html que devuelve el raw html del contenido.
        
        # Estrategia: Usar requests directamente a la URL para asegurar tener toda la tabla
        # ya que la API de fandom a veces recorta infoboxes.
        try:
            response = requests.get(page.url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Buscar la infobox o tabla de datos
            # La estructura puede variar, pero buscamos patrones comunes en wikis de juegos
            # Usualmente <aside class="portable-infobox"> o tablas
            
            infobox = soup.find('aside', {'class': 'portable-infobox'})
            data = {
                'title': page.title,
                'url': page.url,
                'image': page.images[0] if page.images else None,
                'base_damage': 'N/A',
                'penetration': 'N/A'
            }

            if infobox:
                # Intento 1: Buscar por data-source (común en Fandom)
                # Inspecting common fandom structures: <div class="pi-data" data-source="Base Damage">
                
                # Buscar Daño
                damage_node = infobox.find('div', {'data-source': lambda x: x and ('damage' in x.lower() or 'daño' in x.lower())})
                if damage_node:
                    value_node = damage_node.find('div', {'class': 'pi-data-value'})
                    if value_node:
                        data['base_damage'] = value_node.get_text(strip=True)

                # Buscar Penetración
                pen_node = infobox.find('div', {'data-source': lambda x: x and ('class' in x.lower() or 'penetration' in x.lower())})
                if pen_node:
                    value_node = pen_node.find('div', {'class': 'pi-data-value'})
                    if value_node:
                        data['penetration'] = value_node.get_text(strip=True)

                # Intento 2: Si data-source falla, iterar filas como antes (fallback)
                if data['base_damage'] == 'N/A' or data['penetration'] == 'N/A':
                    rows = infobox.find_all('div', {'class': 'pi-item'})
                    for row in rows:
                        label = row.find('h3', {'class': 'pi-data-label'})
                        value = row.find('div', {'class': 'pi-data-value'})
                        
                        if label and value:
                            label_text = label.get_text(strip=True).lower()
                            value_text = value.get_text(strip=True)
                            
                            if data['base_damage'] == 'N/A' and ('damage' in label_text or 'daño' in label_text):
                                data['base_damage'] = value_text
                            elif data['penetration'] == 'N/A' and ('penetration' in label_text or 'class' in label_text):
                                data['penetration'] = value_text

            
            return data

        except Exception as e:
            print(f"Error parseando munición '{title}': {e}")
            return None

    def get_key_info(self, query):
        """Obtiene información de llaves."""
        title = self.search_page(query)
        if not title:
            return None
        
        page = self.get_page_content(title)
        if not page:
            return None

        return {
            'title': page.title,
            'url': page.url,
            'summary': page.summary[:500] + "..." if len(page.summary) > 500 else page.summary,
            'image': page.images[0] if page.images else None
        }

    def get_map_info(self, query):
        """Obtiene información de mapas."""
        title = self.search_page(query)
        if not title:
            return None
        
        page = self.get_page_content(title)
        if not page:
            return None
            
        # Para mapas, idealmente buscamos la imagen que contenga "Map" o "Extraction" en el nombre
        # o simplemente la primera imagen grande.
        map_image = None
        if page.images:
            for img in page.images:
                if 'map' in img.lower() or 'extraction' in img.lower():
                    map_image = img
                    break
            if not map_image:
                map_image = page.images[0]

        return {
            'title': page.title,
            'url': page.url,
            'image': map_image
        }
