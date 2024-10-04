# Proyecto de Consultas con APIs de Google y Wolfram Alpha

Este proyecto permite realizar consultas automatizadas utilizando las APIs de Google, DuckDuckGo y Wolfram Alpha a partir de los datos del **DENUE (Directorio Estadístico Nacional de Unidades Económicas)**. Los scripts están diseñados para interactuar con los datos proporcionados en un archivo Excel y realizar búsquedas personalizadas de manera eficiente.

## Requisitos Previos

Antes de ejecutar los scripts, asegúrate de contar con las siguientes herramientas y configuraciones:

### 1. Python 3

Este proyecto está desarrollado en Python, por lo que es necesario tener **Python 3** instalado. Puedes descargar la última versión desde [python.org](https://www.python.org/downloads/).

### 2. Archivo Excel del DENUE

El archivo Excel del DENUE será la base para las consultas. Este archivo contiene información sobre las unidades económicas que deseas buscar a través de las APIs.

### 3. Claves de API

Debes obtener las claves de las APIs de Google y Wolfram Alpha para que el proyecto pueda realizar las consultas adecuadas. A continuación, te indicamos cómo obtenerlas:

#### Clave de la API de Google

1. Dirígete a [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un nuevo proyecto.
3. En la sección de **API y Servicios**, habilita la **Google Custom Search API**.
4. Genera una **clave de API** y guarda el **ID del motor de búsqueda personalizado (Custom Search Engine)**.

#### Clave de la API de Wolfram Alpha

1. Regístrate en [Wolfram Alpha Developer Portal](https://developer.wolframalpha.com/).
2. Crea una nueva aplicación y genera una clave de API para acceder a sus servicios.

## Instalación de Dependencias

Una vez que tengas las claves de API, es necesario instalar las bibliotecas de Python que permiten la interacción con las APIs y la manipulación de datos en formato Excel.

Ejecuta el siguiente comando para instalar las dependencias:

```bash
pip install google-api-python-client pandas
 ```

## Configuración y Ejecución de los Scripts

### 1. Configuración

Antes de ejecutar los scripts, asegúrate de:

- **Haber configurado correctamente las claves de API.**
- **Haber especificado la ruta correcta del archivo Excel del DENUE en los scripts.**

### 2. Ejecución

Para ejecutar los scripts, abre una terminal o línea de comandos y utiliza el siguiente formato:

```bash
python nombre_del_script.py
