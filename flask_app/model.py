import tensorflow as tf
import numpy as np

MODEL_PATH = 'model/loan_model_v1.h5'


def load_model(path: str = MODEL_PATH):
    return tf.keras.models.load_model(path)


def predict(model, data: dict):
    """Convert incoming dictionary to a numeric numpy array for the model."""
    features = np.array([
        [
            float(data.get('age', 0)),
            float(data.get('income', 0.0)),
            float(data.get('credit_score', 0.0)),
            float(data.get('loan_amount', 0.0)),
            float(data.get('loan_term', 0)),
            float(data.get('employment_years', 0.0)),
            float(data.get('existing_debt', 0.0))
        ]
    ], dtype=np.float32)
    probs = model.predict(features, verbose=0)[0]
    prediction = int(probs[0] > 0.5)
    confidence = float(probs[0])
    return prediction, confidence
