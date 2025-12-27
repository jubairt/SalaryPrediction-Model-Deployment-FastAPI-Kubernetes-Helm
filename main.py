from fastapi import FastAPI
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI(title="Salary Prediction API")

# Load trained model
model = joblib.load("model.pkl")


@app.get("/")
def home():
    return {"message": "Salary Prediction API is running 🚀"}


@app.post("/predict")
def predict_salary(years_experience: float):
    """
    Input: Years of Experience
    Output: Predicted Salary
    """
    # Convert input to 2D array
    input_data = np.array([[years_experience]])

    # Predict
    prediction = model.predict(input_data)

    return {
        "years_experience": years_experience,
        "predicted_salary": float(prediction[0])
    }
