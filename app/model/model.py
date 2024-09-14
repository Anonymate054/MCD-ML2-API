import pandas as pd
import pickle
import fs

__version__ = "0.1.0"

BASE_DIR = fs.open_fs("./app/model/")
MODEL_PATH = f"model-{__version__}.pkl"
MODEL_DIR = BASE_DIR.getsyspath(MODEL_PATH)

with open(MODEL_DIR, "rb") as f:
    model = pickle.load(f)

def predict_pipeline(json_request: dict) -> dict:
    input_data = pd.DataFrame([json_request])
    return model.predict(input_data)