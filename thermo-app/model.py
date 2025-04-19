import joblib
import numpy as np

# ✅ Load the best model once
model = joblib.load("models/best_model.pkl")

def predict_efficiency(length, width, flow_rate, alpha):
    """
    Predict system performance based on user inputs.
    Inputs are floats. Returns a float.
    """
    X = np.array([[length, width, flow_rate, alpha]])
    return model.predict(X)[0]