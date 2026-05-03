import cv2
from pathlib import Path
from fastapi import HTTPException
from lab5_metrics.analyzer import ImageMetrics

def analizar(path: str):
    archivo = Path(path)
    if not archivo.exists():
        raise HTTPException(status_code=400, detail=f"Archivo no encontrado: {archivo}")

    imagen = cv2.imread(str(archivo), 0)
    if imagen is None:
        raise HTTPException(
            status_code=400,
            detail="No se pudo leer la imagen. Asegúrese de enviar un archivo de imagen válido."
        )

    analyzer = ImageMetrics()
    return analyzer.calcular_metricas(imagen)
