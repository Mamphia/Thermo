import joblib
import numpy as np
import os

# 🔒 Use absolute path to avoid file not found issues on Render
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "best_model.pkl")

# ✅ Load model once at module level (fast + efficient)
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print("⚠️ Model failed to load:", e)

def predict_efficiency(length, width, flow_rate, alpha):
    """
    Predict thermal system efficiency using a trained ML model.
    """
    if model is None:
        raise ValueError("Model not loaded properly.")

    X = np.array([[length, width, flow_rate, alpha]])
    return model.predict(X)[0]
