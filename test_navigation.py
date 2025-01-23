from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura el WebDriver (usando Chrome en este ejemplo)
driver = webdriver.Chrome()

try:
    # Navegar a la página
    driver.get("https://jsonplaceholder.typicode.com/")
    
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
