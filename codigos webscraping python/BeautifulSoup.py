# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'https://www.facebook.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Imprimir el HTML para verificar que el contenido fue cargado
    print(soup.prettify())
    
    titles = soup.find_all('h1')
    for title in titles:
        print(title.text)
else:
    print(f"Error en la solicitud: {response.status_code}")
