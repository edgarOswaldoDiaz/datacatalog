import pandas as pd
import requests

# Reemplaza con tu clave de API y tu ID de Wolfram Alpha
APP_ID = ''  # Clave API para autenticarse en Wolfram Alpha

# Función para leer el archivo Excel
def leer_excel(ruta_archivo):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_archivo)  # Carga el archivo Excel en un DataFrame usando pandas
    
    # Verificar que las columnas existan
    if 'nom_estab' in df.columns and 'raz_social' in df.columns:  # Verifica si las columnas 'nom_estab' y 'raz_social' están presentes
        return df[['nom_estab', 'raz_social']]  # Retorna solo esas dos columnas si existen
    else:
        raise Exception("Las columnas 'nom_estab' y 'raz_social' no se encuentran en el archivo Excel.")  # Lanza un error si las columnas faltan

# Función para realizar la consulta a la API de Wolfram Alpha
def wolfram_alpha_search(query):
    # Crear la URL de la solicitud
    url = f"http://api.wolframalpha.com/v2/query?input={query}&format=plaintext&output=JSON&appid={APP_ID}"  # Configura la URL para la API de Wolfram Alpha
    
    # Realizar la solicitud a la API
    response = requests.get(url)  # Llama a la API
    if response.status_code == 200:  # Verifica que la respuesta sea exitosa
        return response.json(), url  # Devuelve los resultados en formato JSON y la URL de la consulta
    else:
        print(f"Error en la solicitud: {response.status_code}")  # Imprime el código de error si ocurre uno
        return None, None  # Devuelve None si hay un error

# Función principal
def buscar_en_wolfram_alpha_desde_excel(ruta_archivo):
    # Leer el archivo Excel
    df = leer_excel(ruta_archivo)  # Llama a la función que lee el archivo Excel
    
    # Recorrer cada fila del DataFrame y hacer la búsqueda en Wolfram Alpha
    for index, row in df.iterrows():  # Itera sobre cada fila del DataFrame
        nom_estab = row['nom_estab']  # Extrae el nombre del establecimiento
        raz_social = row['raz_social']  # Extrae la razón social
        
        # Crear el query de búsqueda
        query = f"{nom_estab} {raz_social}"  # Combina ambas columnas para crear el query de búsqueda
        
        # Realizar la consulta en Wolfram Alpha
        results, url = wolfram_alpha_search(query)  # Llama a la función de búsqueda con el query creado

        # Mostrar los resultados si existen
        if results and 'queryresult' in results:  # Verifica que haya resultados
            print(f"\nResultados para: {query}")  # Imprime el query de búsqueda actual
            print(f"URL de la consulta: {url}")  # Imprime la URL para verificar la información
            pods = results['queryresult'].get('pods', [])  # Obtiene los pods de resultados
            for pod in pods:  # Itera sobre cada pod de resultados
                title = pod.get('title')  # Extrae el título del pod
                subpods = pod.get('subpods', [])  # Obtiene los subpods
                for subpod in subpods:  # Itera sobre cada subpod
                    plaintext = subpod.get('plaintext')  # Extrae el texto en plano del subpod
                    print(f"Title: {title}\nDescription: {plaintext}\n")  # Imprime el título y la descripción
        else:
            print(f"Sin resultados para: {query}")  # Imprime si no hay resultados para el query actual

# Llamada al código principal
if __name__ == "__main__":  # Comprueba si el script se ejecuta como programa principal
    ruta_excel = 'C:/Users/Ivan/Desktop/INEGI/APIs/denue.xlsx'  # Define la ruta del archivo Excel
    buscar_en_wolfram_alpha_desde_excel(ruta_excel)  # Llama a la función principal para iniciar el proceso
