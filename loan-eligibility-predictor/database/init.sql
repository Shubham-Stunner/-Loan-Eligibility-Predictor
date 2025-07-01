CREATE DATABASE IF NOT EXISTS loans;
USE loans;

CREATE TABLE IF NOT EXISTS loan_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    income FLOAT,
    credit_score FLOAT,
    loan_amount FLOAT,
    loan_term INT,
    employment_years FLOAT,
    existing_debt FLOAT,
    loan_approved BOOLEAN,
    confidence_score FLOAT,
    inference_time_ms FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
