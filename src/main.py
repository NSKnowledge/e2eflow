from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Water

app= FastAPI(
    title="Water Potability Prediction",
    description="Predicting water potability"
)

with open(r"C:\Users\u350272\OneDrive - WNS\Documents\StudyProj\mlops\e2eflow\model.pkl",'rb') as f:
    model = pickle.load(f)


@app.get("/")
def index():
    return "Welcome to water potability Prediction Fastapi"

@app.post("/predict")
def model_predict(water:Water):
    sample =pd.DataFrame({
        "ph": [water.ph],
        "Hardness": [water.Hardness],
        "Solids": [water.Solids],
        "Chloramines": [water.Chloramines],
        "Sulfate": [water.Sulfate],
        "Conductivity": [water.Conductivity],
        "Organic_carbon": [water.Organic_carbon],
        "Trihalomethanes": [water.Trihalomethanes],
        "Turbidity": [water.Turbidity]
    })

    predicted_value = model.predict(sample)

    if predicted_value==1:
        return "Water is Consummable"
    else:
        return "Water is not Consummable"




