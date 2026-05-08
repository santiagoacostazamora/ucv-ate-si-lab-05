# Ucv-ate-si-lab-05

## Descripción

Este proyecto desarrolla una aplicación web basada en FastAPI que permite analizar imágenes mediante el cálculo de métricas estadísticas fundamentales. Utilizando las bibliotecas OpenCV y NumPy, la API procesa archivos de imagen enviados por los usuarios y devuelve información cuantitativa sobre sus características visuales.

La API acepta un archivo de imagen y proporciona las siguientes métricas clave:
- `mean` (promedio de los valores de píxeles): Indica el brillo promedio de la imagen.
- `std` (desviación estándar): Mide la variabilidad en los valores de píxeles.
- `min` (valor mínimo): El píxel más oscuro presente.
- `max` (valor máximo): El píxel más brillante presente.

## Estructura del Proyecto

El código está organizado de manera modular para facilitar el mantenimiento y la escalabilidad:

- `src/lab5_metrics/api/main.py`: Contiene la aplicación FastAPI principal y define el endpoint `POST /analyze-metrics` para recibir archivos.
- `src/lab5_metrics/services/metrics_service.py`: Gestiona la lógica de procesamiento de imágenes y coordina el análisis.
- `src/lab5_metrics/analyzer.py`: Implementa la clase `ImageMetrics` responsable del cálculo de métricas estadísticas.
- `src/lab5_metrics/data/`: Directorio destinado al almacenamiento temporal de los archivos de imagen subidos.
- `src/lab5_metrics/tests/test_metrics.py`: Incluye pruebas unitarias para validar el funcionamiento de las métricas.
- `src/lab5_metrics/pyproject.toml`: Define las dependencias del proyecto y la configuración de construcción.

## Requisitos del Sistema

- Python 3.14 o superior
- Bibliotecas necesarias:
  - `numpy` (para operaciones numéricas)
  - `opencv-python` (para procesamiento de imágenes)
  - `fastapi` (framework web)
  - `uvicorn` (servidor ASGI)
  - `pytest` (para ejecutar pruebas, opcional para desarrollo)

## Instalación

Sigue estos pasos para configurar el entorno de desarrollo:

1. Navega al directorio raíz del proyecto en tu terminal:

```powershell
cd "ruta\a\tu\proyecto\Ucv-ate-si-lab-05\src\lab5_metrics"
```

2. Crea y activa un entorno virtual (recomendado para aislar dependencias):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Actualiza pip e instala las dependencias requeridas:

```powershell
python -m pip install --upgrade pip
python -m pip install numpy opencv-python fastapi uvicorn pytest
```

Alternativamente, si usas Poetry (basado en el `pyproject.toml`):

```powershell
poetry install
```

## Ejecución de la Aplicación

Asegúrate de ejecutar el servidor desde el directorio `src` para evitar errores de importación.

```powershell
cd "ruta\a\tu\proyecto\Ucv-ate-si-lab-05\src"
python -m uvicorn lab5_metrics.api.main:app --reload
```

Una vez iniciado, accede a la documentación interactiva de la API en:
- `http://127.0.0.1:8000/docs` (Swagger UI para explorar y probar los endpoints)

## Uso de la API

### Endpoint Principal: `POST /analyze-metrics`

- **Método**: POST
- **Tipo de contenido**: `multipart/form-data`
- **Campo requerido**: `file` (archivo de imagen, e.g., JPG, PNG)
- **Respuesta**: JSON con las métricas calculadas

#### Ejemplo de Solicitud

Usa herramientas como curl, Postman o la interfaz Swagger para enviar una imagen:

```bash
curl -X POST "http://127.0.0.1:8000/analyze-metrics" -F "file=@tu_imagen.jpg"
```

#### Ejemplo de Respuesta

```json
{
  "mean": 123.45,
  "std": 52.16,
  "min": 0,
  "max": 255
}
```

Estas métricas se calculan sobre la versión en escala de grises de la imagen para simplificar el análisis.

## Pruebas

Para ejecutar las pruebas unitarias y verificar que todo funciona correctamente:

```powershell
cd "ruta\a\tu\proyecto\Ucv-ate-si-lab-05\src\lab5_metrics"
python -m pytest tests/test_metrics.py
```

## Notas Adicionales

- Si encuentras un error `ModuleNotFoundError: No module named 'lab5_metrics'`, verifica que estés ejecutando desde el directorio `src`.
- Los archivos subidos se almacenan temporalmente en `src/lab5_metrics/data/`; considera implementar limpieza periódica en un entorno de producción.
- Este proyecto es parte de un laboratorio académico de Sistemas de Información en la UCV, enfocado en el procesamiento de imágenes y desarrollo de APIs.

## Contribución

Si deseas contribuir:
1. Haz un fork del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y agrega pruebas.
4. Envía un pull request.

## Licencia

Este proyecto es de uso académico y no tiene una licencia específica asignada.
