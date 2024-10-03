import requests  # Importa la biblioteca requests para enviar solicitudes HTTP
from bs4 import BeautifulSoup  # Importa BeautifulSoup para analizar HTML
import pandas as pd  # Importa pandas para manipular datos en formato tabular
import time #Importa la libreria para el tiempo transcurrido

# Leer el archivo Excel
excel_file = 'C:/Users/Ernesto/Downloads/denue.csv'  # Ruta al archivo CSV
df = pd.read_csv(excel_file)  # Lee el archivo CSV del DataFrame de pandas

#Inicializa el temporizador del tiempo transcurrido
start_time = time.time()
# Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    # Obtener el valor de las columnas 'nom_estab' y 'raz_social'
    query_name = row.get('nom_estab', '')  
    query_reason = row.get('raz_social', '')  
    
    # Seleccionar el valor de consulta: nombre o razón social
    if query_name:
        query = query_name  # Usa el nombre de la unidad económica si está presente
    elif query_reason:
        query = query_reason  # Usa la razón social si el nombre no está presente
    else:
        continue  # Si no hay datos para buscar, pasa a la siguiente fila
    
    # Construir la URL de búsqueda en Google
    url = f'https://www.google.com/search?q={query}'  # URL de búsqueda con el término de consulta
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }  # Encabezado para simular una solicitud desde un navegador web
    response = requests.get(url, headers=headers)  # Enviar la solicitud GET a Google
    
    # Analizar la respuesta HTML
    soup = BeautifulSoup(response.text, 'html.parser')  # Crear un objeto BeautifulSoup para analizar el HTML
    
    # Extraer los resultados de la búsqueda
    results = soup.find_all('div', class_='g')  # Encontrar todos los resultados de búsqueda en divs con clase 'g'
    
    print(f"Resultados para: {query}")  # Imprimir el término de búsqueda actual
    
    # Iterar sobre cada resultado de búsqueda
    for result in results:
        # Extraer el título del resultado
        title_tag = result.find('h3')  # Buscar la etiqueta h3 para el título
        if title_tag:
            title = title_tag.text  # Obtener el texto del título
        else:
            title = 'No title'  # Si no hay título, establecer como 'No title'
        
        # Extraer el enlace del resultado
        link_tag = result.find('a', href=True)  # Buscar la etiqueta a con atributo href
        if link_tag:
            link = link_tag['href']  # Obtener el enlace
        else:
            link = 'No link'  # Si no hay enlace, establecer como 'No link'
        
        # Extraer la descripción del resultado
        description_tag = result.find('span', class_='aCOpRe')  # Buscar la etiqueta span con clase 'aCOpRe'
        if description_tag:
            description = description_tag.text  # Obtener el texto de la descripción
        else:
            description = 'No description'  # Si no hay descripción, establecer como 'No description'
        
        # Imprimir los detalles del resultado
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Description: {description}")
        print("-" * 80)  # Imprimir una línea separadora para claridad
        
        # Calcula el tiempo transcurrido y lo imprime al finalizar
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")
