from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time #Importa la libreria para el tiempo transcurrido

# Configuración de Selenium con Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecuta Chrome en modo headless (sin ventana)
chrome_service = Service(executable_path='C:/Users/Ernesto/Desktop/chrome/chromedriver.exe')  # Ruta a tu chromedriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
# Se crea una instancia del navegador Chrome en modo headless (sin interfaz gráfica), utilizando el driver de Chrome.

# Lee el archivo Excel
excel_file = 'C:/Users/Ernesto/Downloads/denue.csv'  # Ruta al archivo CSV
df = pd.read_csv(excel_file)  # Lee el archivo CSV del DataFrame de pandas
# Se lee el archivo Excel que contiene los datos, almacenándolos en un DataFrame de pandas (df).

#Inicializa el temporizador del tiempo transcurrido
start_time = time.time()

# Se itera sobre cada fila del DataFrame
for index, row in df.iterrows():
    # Se recorre cada fila del DataFrame (df) fila por fila. 'index' es el índice de la fila y 'row' es el contenido de la fila.

    # Se utilizan los campos 'nom_estab' es el nombre de la unidad económica y 'raz_social' la razón social
    query_name = row.get('nom_estab', '')
    query_reason = row.get('raz_social', '')
    # Se extraen los valores de las columnas 'nom_estab' (nombre del establecimiento) y 'raz_social' (razón social) de cada fila.
    # Si no existe, se asigna una cadena vacía ('').

    # Selecciona el valor de búsqueda: nombre de la unidad económica o razón social
    if query_name:
        query = query_name
    elif query_reason:
        query = query_reason
    else:
        continue  # Salta si no hay un término de búsqueda
    # Se selecciona qué valor usar como término de búsqueda.
    # Si el nombre del establecimiento está disponible, se usa. Si no, se intenta con la razón social.
    # Si ninguno está disponible, se omite esa fila con 'continue'.

    # Realiza la búsqueda en Google
    driver.get(f'https://www.google.com/search?q={query}')
    time.sleep(2)  # Espera a que la página cargue completamente
    # Se realiza una búsqueda en Google usando el término 'query' y se carga la página de resultados.
    # Luego, se espera 2 segundos para asegurarse de que la página se haya cargado completamente.

    # Extrae los resultados de búsqueda
    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
    # Se encuentran todos los resultados de búsqueda usando el selector CSS 'div.g', que selecciona los contenedores de cada resultado.

    print(f"Resultados para: {query}")

    # Itera sobre cada resultado en la página
    for result in results:
        try:
            title = result.find_element(By.TAG_NAME, 'h3').text  # Extraer el título
        except:
            title = 'No title'
        # Se intenta extraer el título del resultado de búsqueda utilizando la etiqueta HTML <h3>.
        # Si no se encuentra, se asigna 'No title'.

        try:
            link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')  # Extraer el link
        except:
            link = 'No link'
        # Se intenta extraer el enlace del resultado de búsqueda mediante la etiqueta <a> y se obtiene el atributo 'href'.
        # Si no se encuentra, se asigna 'No link'.

        try:
            description = result.find_element(By.CSS_SELECTOR, 'span.aCOpRe').text  # Extraer la descripción
        except:
            description = 'No description'
        # Se intenta extraer la descripción del resultado mediante el selector CSS 'span.aCOpRe', que corresponde a la descripción en los resultados de Google.
        # Si no se encuentra, se asigna 'No description'.

        # Imprime los resultados
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Description: {description}")
        print("-" * 80)
        # Se imprimen los datos obtenidos: título, enlace y descripción, y una línea de separación para mayor claridad.
        
        # Calcula el tiempo transcurrido y lo imprime al finalizar
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")

# Cerrar el navegador
driver.quit()
# Finalmente, se cierra el navegador una vez que todas las búsquedas han sido realizadas.
