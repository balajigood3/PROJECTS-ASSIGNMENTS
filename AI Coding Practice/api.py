from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# To this:
with open(r"C:\Balaji - AI Course\AI\AI Coding Practice\salary_model.pk1", "rb") as f:

    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Salary Prediction API"}

@app.get("/predict")
def predict(exp: float):
    
    data = pd.DataFrame({"YearsExperience": [exp]})
    prediction = model.predict(data)
    return {"prediction": float(prediction[0])}
