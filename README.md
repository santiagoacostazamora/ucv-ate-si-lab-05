# Ucv-ate-si-lab-05

## Descripción

Este proyecto implementa una API con FastAPI para analizar imágenes y calcular métricas básicas usando OpenCV y NumPy.

La API recibe un archivo de imagen y devuelve las métricas:
- `mean` (promedio de píxeles)
- `std` (desviación estándar)
- `min` (valor mínimo)
- `max` (valor máximo)

## Estructura del proyecto

- `src/lab5_metrics/api/main.py`: App FastAPI y endpoint `POST /analyze-metrics`
- `src/lab5_metrics/services/metrics_service.py`: Lógica para leer la imagen y delegar el análisis
- `src/lab5_metrics/analyzer.py`: Cálculo de métricas sobre el array de imagen
- `src/lab5_metrics/data/`: Carpeta donde se guardan los archivos subidos
- `src/lab5_metrics/tests/test_metrics.py`: Prueba básica de las métricas
- `src/lab5_metrics/pyproject.toml`: Dependencias del proyecto

## Requisitos

- Python 3.14
- Paquetes:
  - `numpy`
  - `opencv-python`
  - `fastapi`
  - `uvicorn`
  - `pytest` (para pruebas)

## Instalación

1. Abre terminal en la carpeta del proyecto:

```powershell
cd "c:\Users\famil\Downloads\Ucv-ate-si-lab-05\src\lab5_metrics"
```

2. Crea y activa un entorno virtual (recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instala dependencias:

```powershell
python -m pip install --upgrade pip
python -m pip install numpy opencv-python fastapi uvicorn pytest
```

## Ejecución

Es importante ejecutar el servidor desde `src`, no desde `src\lab5_metrics`.

```powershell
cd "c:\Users\famil\Downloads\Ucv-ate-si-lab-05\src"
python -m uvicorn lab5_metrics.api.main:app --reload
```

Luego abre en el navegador:

- `http://127.0.0.1:8000/docs` para la documentación automática de Swagger

## Endpoint principal

### `POST /analyze-metrics`

- Tipo: `multipart/form-data`
- Campo: `file`
- Respuesta: JSON con las métricas calculadas

Ejemplo de respuesta:

```json
{
  "mean": 123.45,
  "std": 52.16,
  "min": 0,
  "max": 255
}
```

## Pruebas

Desde `src/lab5_metrics` ejecuta:

```powershell
python -m pytest tests/test_metrics.py
```

## Notas

- Si ves `ModuleNotFoundError: No module named 'lab5_metrics'`, asegúrate de ejecutar desde `src`.
- Los archivos de imagen subidos se guardan automáticamente en `src/lab5_metrics/data/`.
