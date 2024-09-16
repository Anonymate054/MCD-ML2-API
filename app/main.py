# uvicorn app.main:app --host 0.0.0.0 --reload

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()
app.title = "API - ML2"
app.version = "0.0.1"

class Data(BaseModel):
    LOAN: float = 30.77
    MORTDUE: float = 44.62
    VALUE: float = 15.519
    REASON: float = 0.0
    JOB: float = 5.0
    YOJ: float = 10.0
    DEROG: float = 28.0
    DELINQ: float = 34.0
    CLAGE: float = 22.757
    NINQ: float = 10.0
    CLNO: float = 64.5
    DEBTINC: float = 26.638

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

@app.get("/", tags=["Settings"])
def home():
    return {"health_check": "OK", "model_version": "1.0"}

@app.post("/predict/", response_model=PredictionOut, tags=["ML2"])
def predict(payload: Data):
    prediction = predict_pipeline(payload.dict())
    return PredictionOut(BAD=prediction)

@app.get("/predict/", response_model=PredictionOut, tags=["ML2"])
def predict(payload: Data = Depends()):
    prediction = predict_pipeline(payload.dict())
    return PredictionOut(BAD=prediction)