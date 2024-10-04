import requests  # Importa la biblioteca requests para hacer solicitudes HTTP
import pandas as pd  # Importa la biblioteca pandas para trabajar con datos en forma de DataFrame

# Función para leer el archivo Excel
def leer_excel(ruta_archivo):
    # Carga el archivo Excel en un DataFrame
    df = pd.read_excel(ruta_archivo)
    # Verifica que las columnas 'nom_estab' y 'raz_social' estén presentes en el DataFrame
    if 'nom_estab' in df.columns and 'raz_social' in df.columns:
        # Devuelve un DataFrame que solo contiene las columnas necesarias
        return df[['nom_estab', 'raz_social']]
    else:
        # Si faltan las columnas, lanza una excepción
        raise Exception("Las columnas 'nom_estab' y 'raz_social' no se encuentran en el archivo Excel.")

# Función para buscar en DuckDuckGo usando la API
def buscar_en_duckduckgo(query):
    # Formatea la URL de la API de DuckDuckGo con la consulta y especifica que el formato de respuesta sea JSON
    url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1"
    try:
        # Realiza una solicitud GET a la API
        response = requests.get(url)
        # Lanza un error si la solicitud falla (código de estado 4xx o 5xx)
        response.raise_for_status()
        # Devuelve la respuesta en formato JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # Si ocurre un error en la solicitud, imprime el error
        print(f"Error en la búsqueda: {e}")
        return {}  # Devuelve un diccionario vacío en caso de error

# Función principal para generar resultados de búsqueda
def generar_resultados_busqueda(ruta_archivo):
    # Llama a la función para leer el archivo Excel y obtiene el DataFrame
    df = leer_excel(ruta_archivo)
    resultados = []  # Inicializa una lista vacía para almacenar los resultados

    # Itera sobre cada fila del DataFrame
    for index, row in df.iterrows():
        nom_estab = row['nom_estab']  # Obtiene el nombre del establecimiento
        raz_social = row['raz_social']  # Obtiene la razón social
        # Crea una consulta concatenando el nombre del establecimiento y la razón social
        query = f"{nom_estab} {raz_social}"
        print(f"Buscando: {query}")  # Imprime el query que se está buscando

        # Realiza la búsqueda en DuckDuckGo
        resultados_busqueda = buscar_en_duckduckgo(query)
        print(resultados_busqueda)  # Imprime la respuesta de la API

        # Procesa y guarda los resultados
        if 'RelatedTopics' in resultados_busqueda:  # Verifica si hay temas relacionados en la respuesta
            # Itera sobre cada elemento en 'RelatedTopics'
            for item in resultados_busqueda['RelatedTopics']:
                # Verifica que el item tenga 'Text' y 'FirstURL'
                if 'Text' in item and 'FirstURL' in item:
                    # Agrega un diccionario con el título, enlace y descripción de cada resultado
                    resultados.append({
                        'titulo': item['Text'],
                        'link': item['FirstURL'],
                        'descripcion': item.get('Result', '')  # Usa .get() para evitar KeyError
                    })

    return resultados  # Devuelve la lista de resultados

# Llamada al código principal
if __name__ == "__main__":
    # Define la ruta del archivo Excel que contiene los datos
    ruta_excel = 'C:/Users//INEGI/APIs/denue.xlsx'

    # Llama a la función para generar resultados de búsqueda
    resultados_busqueda = generar_resultados_busqueda(ruta_excel)

    # Imprimir los resultados
    for resultado in resultados_busqueda:
        # Imprime el título de cada resultado
        print(f"Título: {resultado['titulo']}")
        # Imprime el enlace de cada resultado
        print(f"Enlace: {resultado['link']}")
        # Imprime la descripción de cada resultado
        print(f"Descripción: {resultado['descripcion']}")
        print()  # Imprime una línea en blanco para separar los resultados
