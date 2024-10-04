import time  # Importa la biblioteca time, que se usa para controlar el tiempo, como las pausas.
import pandas as pd  # Importa la biblioteca pandas, que se usa para la manipulación de datos, especialmente para trabajar con DataFrames.
from googleapiclient.discovery import build  # Importa la función build para crear un cliente de la API de Google.
from googleapiclient.errors import HttpError  # Importa la clase HttpError para manejar errores de la API.

# Reemplaza con tu clave de API y tu ID del motor de búsqueda
API_KEY = ''  # Clave API para autenticarse en Google.
CX = ''  # ID del motor de búsqueda personalizada que se ha configurado en Google.

# Crear el servicio de búsqueda
service = build("customsearch", "v1", developerKey=API_KEY)  # Crea un cliente para el servicio de búsqueda.

# Función para leer el archivo Excel
def leer_excel(ruta_archivo):
    df = pd.read_excel(ruta_archivo)  # Carga el archivo Excel en un DataFrame usando pandas.
    if 'nom_estab' in df.columns and 'raz_social' in df.columns:  # Verifica si las columnas 'nom_estab' y 'raz_social' existen.
        return df[['nom_estab', 'raz_social']]  # Retorna solo esas dos columnas si existen.
    else:
        raise Exception("Las columnas 'nom_estab' y 'raz_social' no se encuentran en el archivo Excel.")  # Lanza una excepción si no se encuentran las columnas.

# Función para realizar la consulta a la API de Google
def google_search(query):
    try:
        result = service.cse().list(q=query, cx=CX).execute()  # Realiza la consulta a la API de Google con el query y el ID del motor de búsqueda.
        # NOTA: Marca error por pasarse los limites de peticiones. 
        return result  # Retorna el resultado de la búsqueda.
    except HttpError as e:  # Captura errores relacionados con la API.
        if e.resp.status == 429:  # Código de error 429: Too Many Requests.
            print("Se ha excedido el límite de consultas. Esperando antes de reintentar...")  # Informa que se ha alcanzado el límite de consultas.
            time.sleep(60)  # Espera 60 segundos.
            return google_search(query)  # Reintenta la búsqueda después de esperar.
        else:
            print(f"Error al realizar la búsqueda para '{query}': {str(e)}")  # Imprime el error que ocurrió.
            return None  # Retorna None si ocurrió un error distinto a 429.

# Función principal
def buscar_en_google_desde_excel(ruta_archivo):
    df = leer_excel(ruta_archivo)  # Llama a la función que lee el archivo Excel.
    for index, row in df.iterrows():  # Itera sobre cada fila del DataFrame.
        nom_estab = row['nom_estab']  # Extrae el nombre del establecimiento de la columna 'nom_estab'.
        raz_social = row['raz_social']  # Extrae la razón social de la columna 'raz_social'.
        query = f"{nom_estab} {raz_social}"  # Crea el query de búsqueda concatenando el nombre del establecimiento y la razón social.
        
        # Realizar la consulta en Google
        results = google_search(query)  # Llama a la función de búsqueda con el query creado.
        
        # Mostrar los resultados si existen
        if results and 'items' in results:  # Verifica si hay resultados y si la clave 'items' existe en el resultado.
            print(f"\nResultados para: {query}")  # Imprime el query de búsqueda actual.
            for item in results['items']:  # Itera sobre los resultados obtenidos.
                title = item.get('title')  # Extrae el título del resultado.
                link = item.get('link')  # Extrae el enlace del resultado.
                snippet = item.get('snippet')  # Extrae una breve descripción del resultado.
                # Imprime el título, enlace y descripción.
                print(f"Title: {title}\nLink: {link}\nDescription: {snippet}\n")  
        else:
            print(f"Sin resultados para: {query}")  # Imprime si no hay resultados para el query actual.

# Llamada al código principal
if __name__ == "__main__":  # Comprueba si el script se ejecuta como programa principal.
    ruta_excel = 'C:/Users//INEGI/APIs/denue.xlsx'  # Define la ruta del archivo Excel.
    buscar_en_google_desde_excel(ruta_excel)  # Llama a la función principal para iniciar el proceso.
