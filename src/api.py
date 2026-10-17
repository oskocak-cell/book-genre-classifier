from fastapi import FastAPI
import joblib
import csv
from pathlib import Path

app = FastAPI()

# Load model + vectorizer
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

@app.post("/predict")
def predict(data: dict):
    text = data["text"]
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    return {"prediction": str(pred)}

@app.get("/health")
def health():
    return {"status": "RMD-OK"}
@app.get("/metrics")
def metrics():
    metrics_file = Path("logs/metrics.csv")
    if not metrics_file.exists():
        return {"model_accuracy": None, "status": "Run training locally to generate metrics."}
    with metrics_file.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return {"model_accuracy": None, "status": "No training metrics recorded."}
    return {"model_accuracy": float(rows[-1]["accuracy"])}
