from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

# Cargar configuración desde el archivo JSON
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Obtener la URL desde el archivo de configuración
web_url = config["web_url"]

# Configura el WebDriver (usando Chrome en este ejemplo)
driver = webdriver.Chrome()

try:
    # Navegar a la página
    driver.get(web_url)
    
    # Esperar unos segundos para asegurarse de que la página haya cargado
    time.sleep(2)
    
    # Extraer el texto del encabezado
    header = driver.find_element(By.TAG_NAME, "h1").text.strip()
    
    # Validar el encabezado esperado
    expected_header = "JSONPlaceholder"
    assert header == expected_header, f"Error: Se esperaba '{expected_header}', pero se obtuvo '{header}'"
    
    print("Prueba exitosa: El encabezado es correcto.")

finally:
    # Cerrar el navegador
    driver.quit()
