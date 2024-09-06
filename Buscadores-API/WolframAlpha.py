import requests  # Importa el módulo `requests` para hacer peticiones HTTP.

def wolframalpha_search(query, app_id):
    # Se define una función llamada `wolframalpha_search` que toma dos parámetros: `query` y `app_id`.
    
    url = f"https://api.wolframalpha.com/v1/result"  # URL base para la API de WolframAlpha.
    
    params = {
        'i': query,  # El término de búsqueda, que se pasa como parámetro a la API.
        'appid': app_id  # La clave de aplicación (`app_id`) necesaria para autenticar la solicitud.
    }
    
    response = requests.get(url, params=params)  # Realiza una solicitud HTTP GET con los parámetros definidos.
    
    return response.text  # Devuelve el contenido de la respuesta como texto.

app_id = ''  # Definicion la clave de aplicación para acceder a la API de WolframAlpha.

query = 'Next solar eclipse date'  # Define el término de búsqueda como "Fecha del proximo eclipse solar".

result = wolframalpha_search(query, app_id)  # Llama a la función `wolframalpha_search` con el término de búsqueda y la clave de aplicación, y guarda el resultado en `result`.

print(result)  # Imprime el contenido de `result`, que es la respuesta en formato de texto de la búsqueda realizada.
