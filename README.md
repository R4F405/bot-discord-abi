# Bot de Discord: Arena Breakout Infinite Wiki

Este bot proporciona información en tiempo real sobre el juego "Arena Breakout: Infinite" obteniendo datos de su Wiki de Fandom.

## Comandos

El bot utiliza **Slash Commands** (`/`). Escribe `/abi` para ver las opciones disponibles.

### `/abi municion [nombre]`
Busca información sobre un tipo de munición.
- Ejemplo: `/abi municion 5.56x45`

### `/abi llave [nombre]`
Busca información sobre una llave.
- Ejemplo: `/abi llave Motel Main Guest Room`

### `/abi mapa [nombre]`
Muestra el mapa solicitado.
- Ejemplo: `/abi mapa Farm`

## Requisitos

- Python 3.9+
- Una cuenta de desarrollador de Discord (para obtener el Token).

## Configuración en Discord Developer Portal

Antes de instalar el código, necesitas crear la aplicación en Discord:

1.  Ve al [Discord Developer Portal](https://discord.com/developers/applications).
2.  Haz clic en **New Application** y dale un nombre (ej: "ABI Wiki Bot").
3.  Ve a la pestaña **Bot** (menú lateral) y haz clic en **Add Bot**.
4.  **Token**: Haz clic en **Reset Token** para generar tu token. **Cópialo y guárdalo**, lo necesitarás para el archivo `.env`.
5.  **Privileged Gateway Intents** (Importante):
    - Desplázate hacia abajo en la pestaña **Bot**.
    - Activa **MESSAGE CONTENT INTENT**. Esto es necesario para que el bot pueda leer los comandos que empiezan con `/abi`.
    - Guarda los cambios (**Save Changes**).
6.  **Invitar al Bot**:
    - Ve a la pestaña **OAuth2** -> **URL Generator**.
    - En **SCOPES**, selecciona `bot` y `applications.commands`.
    - En **BOT PERMISSIONS**, selecciona:
        - `View Channels`
        - `Send Messages`
        - `Embed Links` (Crítico para mostrar las imágenes y stats)
        - `Read Message History`
    - Copia la URL generada abajo y ábrela en tu navegador para invitar al bot a tu servidor.

## Solución de Problemas

### Los comandos de barra (/) no aparecen
- Los comandos globales pueden tardar hasta una hora en propagarse a todos los servidores.
- Intenta reiniciar tu cliente de Discord.
- Si el bot ya estaba en el servidor, puede que necesites expulsarlo y volverlo a invitar con el scope `applications.commands`.

## Instalación

1.  **Clonar el repositorio** (o descargar los archivos).
2.  **Crear un entorno virtual** (recomendado):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```
3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configurar variables de entorno**:
    - Renombra `.env.example` a `.env`.
    - Pega tu Token de Discord en `DISCORD_TOKEN`.

## Ejecución

Para iniciar el bot:

```bash
python src/bot.py
```

## Estructura del Proyecto

- `src/bot.py`: Punto de entrada.
- `src/cogs/abi.py`: Comandos del bot.
- `src/services/wiki_service.py`: Lógica de scraping (BeautifulSoup + Fandom API).
- `src/utils/embeds.py`: Generación de respuestas visuales (Embeds).

## Notas de Desarrollo

Si la wiki cambia su estructura HTML, es posible que necesites ajustar los selectores en `src/services/wiki_service.py` para extraer correctamente los datos de las tablas.
