from src.services.wiki_service import WikiService

def test_scraping():
    service = WikiService()
    
    print("--- Test Munición (M995) ---")
    ammo = service.get_ammo_info("M995")
    if ammo:
        print(f"Encontrado: {ammo['title']}")
        print(f"Daño: {ammo['base_damage']}")
        print(f"Penetración: {ammo['penetration']}")
    else:
        print("FALLO: No se encontró M995")

    print("\n--- Test Llave (Motel 201) ---")
    key = service.get_key_info("Motel 201")
    if key:
        print(f"Encontrado: {key['title']}")
        print(f"Resumen: {key['summary'][:50]}...")
    else:
        print("FALLO: No se encontró Motel 201")

    print("\n--- Test Mapa (Farm) ---")
    mapa = service.get_map_info("Farm")
    if mapa:
        print(f"Encontrado: {mapa['title']}")
        print(f"Imagen: {mapa['image']}")
    else:
        print("FALLO: No se encontró Farm")

if __name__ == "__main__":
    test_scraping()
