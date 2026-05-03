from fastapi import FastAPI, UploadFile, HTTPException
import shutil
from pathlib import Path
from lab5_metrics.services.metrics_service import analizar

app = FastAPI()

data_dir = Path(__file__).resolve().parents[1] / "data"
data_dir.mkdir(parents=True, exist_ok=True)

@app.post("/analyze-metrics")
async def analyze(file: UploadFile):
    path = data_dir / file.filename

    try:
        with path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except OSError as exc:
        raise HTTPException(status_code=500, detail=f"No se pudo guardar el archivo: {exc}")

    result = analizar(str(path))
    return result
