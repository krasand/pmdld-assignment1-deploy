from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from typing import Dict
import os
import numpy as np
from sklearn.datasets import load_wine

MODEL_PATH = os.getenv("MODEL_PATH", "/app/models/model.joblib")
model = joblib.load(MODEL_PATH)

app = FastAPI(title="Wine Model API")

class Features(BaseModel):
    # словарь: имя_признака -> значение
    data: Dict[str, float]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: Features):
    names = load_wine().feature_names
    x = np.array([[payload.data.get(n, 0.0) for n in names]])
    y_pred = model.predict(x).tolist()[0]
    return {"prediction": int(y_pred)}