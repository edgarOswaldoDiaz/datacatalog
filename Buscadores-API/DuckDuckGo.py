import requests  # Se importa el módulo `requests` para hacer peticiones HTTP.

def duckduckgo_search(query):
    # Definicion de una función llamada `duckduckgo_search` que toma un parámetro `query`.
    
    url = f"https://duckduckgo.com/"  # URL base para la busquda en DuckDuckGo.
    
    params = {
        'q': query,  # El término de búsqueda, que se pasa como parámetro a la API.
        'format': 'json'  # Se especifica que la respuesta debe estar en formato JSON.
    }
    
    response = requests.get(url, params=params)  # Realiza una solicitud HTTP GET con los parámetros definidos.
    
    return response.json()  # Convierte la respuesta en formato JSON y la devuelve.

query = 'OpenAI'  # Define el término de búsqueda.

results = duckduckgo_search(query)  # Llama a la función `duckduckgo_search` y guarda el resultado en `results`.

print(results)  # Imprime el contenido de `results`, que es la respuesta de la búsqueda en formato JSON.
