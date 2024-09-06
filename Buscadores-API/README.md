# Credenciales necesarias 

## Requisitos Adicionales

Para ejecutar este proyecto, necesitarás obtener credenciales específicas para utilizar las APIs de Google, DuckDuckGo y WolframAlpha. A continuación, se detallan los pasos para obtener estas credenciales:

### API de Google

- **API Key y CSE ID**: Necesitarás una clave de API (`API Key`) y un ID de motor de búsqueda personalizado (`CSE ID`) para utilizar la API de búsqueda de Google.
  - **Obtener API Key**: Regístrate en [Google Cloud Console](https://console.cloud.google.com/), crea un proyecto nuevo, habilita la API de Búsqueda Personalizada y genera una clave de API.
  - **Obtener CSE ID**: Crea un motor de búsqueda personalizado en [Google Custom Search Engine](https://cse.google.com/cse/), configura las opciones según tus necesidades y copia el ID del motor de búsqueda.

### DuckDuckGo

- **URL de la API**: DuckDuckGo ofrece una API de búsqueda pública que no requiere una clave de API. La URL base para realizar búsquedas es `https://api.duckduckgo.com/`. Consulta la documentación en [DuckDuckGo API Documentation](https://duckduckgo.com/api).

### WolframAlpha

- **App ID**: Para utilizar la API de WolframAlpha, necesitas un identificador de aplicación (`App ID`).
  - **Obtener App ID**: Regístrate en [WolframAlpha Developer Portal](https://developer.wolframalpha.com/portal/myapps/index.html) y crea una nueva aplicación para obtener tu `App ID`.

# Ejecutar los script

## Requisitos

Una vez generado las credenciales de las APIs, es necesario tener los siguientes requisitos:

1. **Python**: Asegúrate de tener Python instalado en tu sistema. Puedes verificar la instalación ejecutando el siguiente comando en la terminal:

    ```bash
    python --version
    ```

    Si no tienes Python instalado, puedes descargarlo e instalarlo desde [python.org](https://www.python.org/).

2. **Librería Requests**: Este proyecto utiliza la librería `Requests` para realizar solicitudes HTTP. Instálala usando el siguiente comando en la terminal:

    ```bash
    pip install requests
    ```

## Ejecución

Una vez que tengas Python y la librería `Requests` instalados, podrás ejecutar el código sin problemas. Simplemente abre tu terminal, navega hasta el directorio del proyecto, y ejecuta el archivo Python deseado:

```bash
python nombre_del_archivo.py

