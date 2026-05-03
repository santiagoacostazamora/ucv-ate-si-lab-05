import numpy as np

class ImageMetrics:

    def calcular_metricas(self, imagen):
        return {
            "mean": float(np.mean(imagen)),
            "std": float(np.std(imagen)),
            "min": int(np.min(imagen)),
            "max": int(np.max(imagen))
        }
