# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar el navegador Chrome
driver = webdriver.Chrome()

# Navegar a la página web
driver.get('https://www.facebook.com')

# Encuentra elementos y extrae datos
titles = driver.find_elements(By.TAG_NAME, 'h1')
for title in titles:
    print(title.text)

# Cerrar el navegador
driver.quit()



