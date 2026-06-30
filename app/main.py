from fastapi import FastAPI
from app.predictor import predict
from app.schemas import Patient

app = FastAPI(
    title="Breast Cancer Prediction API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Breast Cancer Prediction API is running"
    }


@app.post("/predict")
def predict_patient(patient: Patient):

    prediction = predict(patient.model_dump())

    return {
        "prediction": prediction
    }