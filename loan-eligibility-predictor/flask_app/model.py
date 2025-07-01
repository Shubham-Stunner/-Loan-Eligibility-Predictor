import tensorflow as tf
import numpy as np

MODEL_PATH = 'model/loan_model_v1.h5'


def load_model(path: str = MODEL_PATH):
    return tf.keras.models.load_model(path)


def predict(model, data: dict):
    features = np.array([
        [
            data.get('age', 0),
            data.get('income', 0.0),
            data.get('credit_score', 0.0),
            data.get('loan_amount', 0.0),
            data.get('loan_term', 0),
            data.get('employment_years', 0.0),
            data.get('existing_debt', 0.0)
        ]
    ])
    probs = model.predict(features, verbose=0)[0]
    prediction = int(probs[0] > 0.5)
    confidence = float(probs[0])
    return prediction, confidence
