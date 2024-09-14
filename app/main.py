from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class Data(BaseModel):
    LOAN: float
    MORTDUE: float
    VALUE: float
    REASON: float
    JOB: float
    YOJ: float
    DEROG: float
    DELINQ: float
    CLAGE: float
    NINQ: float
    CLNO: float
    DEBTINC: float

    class Config:
        json_schema_extra = {
            "example": {
                "LOAN": 30.77,
                "MORTDUE": 44.62,
                "VALUE": 15.519,
                "REASON": 0.0,
                "JOB": 5.0,
                "YOJ": 10.0,
                "DEROG": 28.0,
                "DELINQ": 34.0,
                "CLAGE": 22.757,
                "NINQ": 10.0,
                "CLNO": 64.5,
                "DEBTINC": 26.638
            }
        }

class PredictionOut(BaseModel):
    BAD: int

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": "1.0"}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: Data):
    prediction = predict_pipeline(payload.dict())
    return PredictionOut(BAD=prediction)