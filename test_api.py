import requests

# URL de la API
api_url = "https://jsonplaceholder.typicode.com/posts/1"

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
