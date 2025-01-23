import requests
import json

# Cargar configuración desde el archivo JSON
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Obtener la URL desde el archivo de configuración
api_url = config["api_url"]

# Realizar la petición GET
response = requests.get(api_url)

# Verificar que el estado sea 200
assert response.status_code == 200, f"Error: Status code {response.status_code}"

# Parsear el JSON
data = response.json()

# Extraer y validar el título esperado
expected_title = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
assert data["title"] == expected_title, f"Error: Se esperaba '{expected_title}', pero se obtuvo '{data['title']}'"

print("Prueba exitosa: El título del JSON es correcto.")

