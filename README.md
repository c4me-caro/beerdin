# BeerDin 🍺

Este es un bot de Discord desarrollado en Python que se encarga de recolectar métricas y datos de servidores de Discord, incluyendo el uso de emoticonos, mensajes, y estadísticas de voz.
Utiliza bases de datos PostgreSQL y MongoDB para almacenar y gestionar los datos, respetando la privacidad de los usuarios.

## Descripción
Este bot se conecta a un servidor de Discord y recolecta información sobre el servidor, como la cantidad de mensajes enviados, emoticonos más usados, tiempo en llamadas de voz y estadísticas de usuarios. Los datos son almacenados temporalmente en bases de datos PostgreSQL y MongoDB para un uso específico. Los usuarios pueden personalizar el comportamiento del bot mediante un archivo `.env` para gestionar las configuraciones como el prefijo de comandos, el idioma y las claves de acceso a la base de datos.

## Cómo instalar dependencias

1. **Clona el repositorio:**
   Si aún no has clonado el repositorio, puedes hacerlo con el siguiente comando:

   ```bash
   git clone https://github.com/TU_USUARIO/discord-bot.git

2. **Crear y activar un entorno virtual:**

   Crea un entorno virtual para el proyecto:
   ```bash
   python -m venv venv
   ```

   Activa el entorno virtual:

   * En Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

   * En Windows:
     ```bash
     .\venv\Scripts\activate
     ```

3. **Instalar las dependencias:**

   Con el entorno virtual activado, instala las dependencias necesarias con el siguiente comando:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configurar las variables de entorno:**
Crea un archivo .env en la raíz del proyecto utilizando el archivo .env.example como plantilla. Rellena las variables necesarias:
     ```bash
      cp .env.example .env

Luego, edita el archivo .env y reemplaza los valores de ejemplo por los correctos:
   ```bash
      DISCORD_TOKEN=TU_TOKEN_AQUI
      MONGO_URL=TU_URL_MONGO_DB_AQUI
      LANGUAGE="ES"
      PREFIX="!"
   ```

## Cómo arrancar el proyecto
1. **Iniciar el bot:**
Con las dependencias instaladas y el archivo .env configurado, puedes arrancar el bot ejecutando el siguiente comando:
    ``` bash
    python bot.py
    
Verás un mensaje en la terminal indicando que el bot ha iniciado correctamente:
    ``` Bash
    
      ✅ Se ha iniciado correctamente como <nombre_del_bot>
2. Acceder a la base de datos:
Asegúrate de que las conexiones a las bases de datos (PostgreSQL y MongoDB) estén correctamente configuradas en el archivo .env para que el bot pueda almacenar los datos correctamente.

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
