from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

model = joblib.load("Chronic Kidney Disease.pkl")
encoders = joblib.load("label_encoders.pkl")

app = FastAPI(title="Chronic Kidney Disease API")

class CKD(BaseModel):
    id: int
    sg: float
    al: int
    pc: str
    sod: float
    hemo: float
    pcv: int
    rc: float
    htn: str
    dm: str
    appet: str
    pe: str

@app.get("/")
def home():
    return {"message": "Welcome to Chronic Kidney Disease API"}
@app.post("/predict")
@app.post("/predict")
def predict(ckd: CKD):

    data = pd.DataFrame([ckd.model_dump()])

    cat_cols = [
        "pc",
        "htn",
        "dm",
        "appet",
        "pe"
    ]

    for col in cat_cols:
        data[col] = encoders[col].transform(data[col])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0]

    return {
        "Prediction": "CKD" if prediction == 1 else "Not CKD",
        "CKD Probability": round(float(probability[1]), 4),
        "Not CKD Probability": round(float(probability[0]), 4)
    }