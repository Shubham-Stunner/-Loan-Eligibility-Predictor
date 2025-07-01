from flask import Blueprint, request, jsonify
from time import time

from .model import load_model, predict
from .db import db
from .metrics import REQUEST_COUNT

api_bp = Blueprint('api', __name__)
model = load_model()


@api_bp.route('/predict', methods=['POST'])
def predict_route():
    start_time = time()
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    prediction, confidence = predict(model, data)

    inference_time = (time() - start_time) * 1000
    REQUEST_COUNT.inc()

    # Log into DB
    from .models import LoanPrediction
    record = LoanPrediction(
        age=data.get('age'),
        income=data.get('income'),
        credit_score=data.get('credit_score'),
        loan_amount=data.get('loan_amount'),
        loan_term=data.get('loan_term'),
        employment_years=data.get('employment_years'),
        existing_debt=data.get('existing_debt'),
        loan_approved=bool(prediction),
        confidence_score=float(confidence),
        inference_time_ms=inference_time
    )
    db.session.add(record)
    db.session.commit()

    return jsonify({
        'loan_approved': bool(prediction),
        'confidence_score': float(confidence),
        'model_version': 'v1.0',
        'inference_time_ms': inference_time
    })
