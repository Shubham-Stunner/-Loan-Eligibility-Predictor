from .db import db


class LoanPrediction(db.Model):
    __tablename__ = 'loan_predictions'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    income = db.Column(db.Float)
    credit_score = db.Column(db.Float)
    loan_amount = db.Column(db.Float)
    loan_term = db.Column(db.Integer)
    employment_years = db.Column(db.Float)
    existing_debt = db.Column(db.Float)
    loan_approved = db.Column(db.Boolean)
    confidence_score = db.Column(db.Float)
    inference_time_ms = db.Column(db.Float)
