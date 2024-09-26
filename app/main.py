# uvicorn app.main:app --host 0.0.0.0 --reload
from app.model.model import __version__ as model_version
from app.model.model import predict_pipeline
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Literal

app = FastAPI()
app.title = "API - ML2"
app.version = "0.0.2"

class Data(BaseModel):
    LOAN: float = 30.77
    MORTDUE: float = 44.62
    VALUE: float = 15.519
    REASON: Literal['HomeImp', 'DebtCon'] = "HomeImp"
    JOB: Literal['Other', 'Office', 'Sales', 'Mgr', 'ProfExe', 'Self'] = "ProfExe"
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
                "REASON": "HomeImp",
                "JOB": "ProfExe",
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
    credit: str

@app.get("/", tags=["Settings"])
def home():
    return {"health_check": "OK", "model_version": "1.1"}

@app.post("/predict/", response_model=PredictionOut, tags=["ML2"])
def predict(payload: Data):
    prediction = predict_pipeline(payload.dict())
    return PredictionOut(BAD=prediction)

@app.get("/predict/", response_model=PredictionOut, tags=["ML2"])
def predict(payload: Data = Depends()):
    prediction = predict_pipeline(payload.dict())
    return PredictionOut(credit="Accepted" if prediction == 0 else "Rejected")