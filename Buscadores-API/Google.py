import requests

# Define la función google_search que toma tres parámetros: query, api_key, y cse_id
def google_search(query, api_key, cse_id):
    # URL base para la API de búsqueda personalizada de Google
    url = f"https://www.googleapis.com/customsearch/v1"
    
    # Parámetros que se envían con la solicitud GET a la API
    params = {
        'key': api_key,  # Clave de API para autenticarse en la API de Google
        'cx': cse_id,    # ID del motor de búsqueda personalizado
        'q': query       # La consulta de búsqueda proporcionada por el usuario
    }
    
    # Realiza una solicitud GET a la URL con los parámetros especificados
    response = requests.get(url, params=params)
    
    # Devuelve la respuesta de la API en formato JSON
    return response.json()

# Asigna tu clave de API a la variable api_key
api_key = ''

# Asigna tu ID de motor de búsqueda personalizado a la variable cse_id
cse_id = ''

# Define la consulta de búsqueda que quieres realizar
query = 'OpenAI'

# Llama a la función google_search con los parámetros especificados y guarda los resultados
results = google_search(query, api_key, cse_id)

# Imprime los resultados de la búsqueda en formato JSON
print(results)
