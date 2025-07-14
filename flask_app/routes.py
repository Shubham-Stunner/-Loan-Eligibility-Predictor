from flask import Blueprint, request, jsonify, render_template
from time import time

from .model import load_model, predict
from .db import db
from .metrics import REQUEST_COUNT

# Define Blueprint
api_bp = Blueprint('api', __name__)

# Load ML model once at blueprint load time
model = load_model()

@api_bp.route('/')
def index():
    return render_template('index.html')

@api_bp.route('/predict', methods=['POST'])
def predict_route():
    start_time = time()
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid or missing JSON'}), 400

    try:
        numeric_data = {
            'age': float(data.get('age', 0)),
            'income': float(data.get('income', 0.0)),
            'credit_score': float(data.get('credit_score', 0.0)),
            'loan_amount': float(data.get('loan_amount', 0.0)),
            'loan_term': float(data.get('loan_term', 0)),
            'employment_years': float(data.get('employment_years', 0.0)),
            'existing_debt': float(data.get('existing_debt', 0.0))
        }
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input data types'}), 400

    try:
        prediction, confidence = predict(model, numeric_data)
    except Exception as e:
        return jsonify({'error': f'Model prediction failed: {str(e)}'}), 500

    inference_time = (time() - start_time) * 1000
    REQUEST_COUNT.inc()

    try:
        from .models import LoanPrediction
        record = LoanPrediction(
            age=int(numeric_data['age']),
            income=numeric_data['income'],
            credit_score=numeric_data['credit_score'],
            loan_amount=numeric_data['loan_amount'],
            loan_term=int(numeric_data['loan_term']),
            employment_years=numeric_data['employment_years'],
            existing_debt=numeric_data['existing_debt'],
            loan_approved=bool(prediction),
            confidence_score=float(confidence),
            inference_time_ms=inference_time
        )
        db.session.add(record)
        db.session.commit()
    except Exception as db_error:
        return jsonify({'error': f'Database logging failed: {str(db_error)}'}), 500

    return jsonify({
        'loan_approved': bool(prediction),
        'confidence_score': float(confidence),
        'model_version': 'v1.0',
        'inference_time_ms': inference_time
    })


@api_bp.route('/predict-ui', methods=['POST'])
def predict_ui():
    """Handle form submissions and display a friendly result page."""
    start_time = time()

    try:
        features = [
            float(request.form.get('age', 0)),
            float(request.form.get('income', 0.0)),
            float(request.form.get('credit_score', 0.0)),
            float(request.form.get('loan_amount', 0.0)),
            float(request.form.get('loan_term', 0)),
            float(request.form.get('employment_years', 0.0)),
            float(request.form.get('existing_debt', 0.0)),
        ]
    except (TypeError, ValueError):
        return render_template(
            'index.html',
            result='Invalid input data',
            result_class='danger'
        )

    # Run model prediction
    prediction_probs = model.predict([features], verbose=0)[0][0]
    eligible = prediction_probs >= 0.5

    inference_time = (time() - start_time) * 1000

    return render_template(
        'index.html',
        result='Loan Approved' if eligible else 'Loan Not Approved',
        result_class='success' if eligible else 'danger',
        confidence=float(prediction_probs),
        inference_time=inference_time
    )
