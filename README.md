# Proyecto de Pruebas Automatizadas con Selenium y Python

Este proyecto contiene dos casos de prueba automatizados utilizando **Selenium** y **Python**. Los casos son:

1. **`test_navigation.py`**: Navega a una página web y verifica el encabezado.
2. **`test_api.py`**: Realiza una solicitud a una API y valida un valor específico del JSON de respuesta.

---

## **Requisitos previos**

Antes de comenzar, asegúrate de tener los siguientes componentes instalados en tu sistema:

1. **Python** (versión 3.7 o superior)
   - Descárgalo desde [https://www.python.org/](https://www.python.org/).

2. **Google Chrome** (u otro navegador) y su WebDriver:
   - Descarga el **ChromeDriver** compatible con tu versión de Chrome desde: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/).

3. **Git**
   - Descárgalo desde [https://git-scm.com/](https://git-scm.com/).

4. **Crea el entorno virtual**
   - python -m venv venv

5. **Activa el entorno virtual**
   - venv\Scripts\activate
6. **Instala las dependencias necesarias con**
   - pip install -r requirements.txt

7. **Ejecución de los casos de pruebas**
   - python test_navigation.py o python test_api.py

8. **Notas adicionales**
   - Asegúrate de que el ChromeDriver esté disponible en tu PATH o en el mismo directorio que el proyecto.
   - Si estás usando otro navegador (Firefox, Edge, etc.), instala el WebDriver correspondiente y modifica el script para usarlo.

---

## **Pasos para clonar el proyecto**

1. Abre tu terminal y navega al directorio donde deseas clonar el repositorio.
2. Ejecuta el siguiente comando:
   ```bash
   git clone https://github.com/jenisqatester/ExampleSelenium.git
