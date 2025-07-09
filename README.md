# Loan Eligibility Predictor – ML Inference Monitoring App

This app provides an API for predicting loan approval using a TensorFlow model. It logs predictions to MySQL and exposes Prometheus metrics for visualization in Grafana.

## Usage

Build and run all services:

```bash
docker-compose -f docker/docker-compose.yml up --build
```

The API will be available at `http://localhost:5000/predict`. A simple HTML
front‑end form is served at `http://localhost:5000/`.

To generate a dummy model with the required **seven** input features run:

```bash
python3 model/generate_dummy_model.py
```

This will create `model/loan_model_v1.h5`. Ensure it exists before starting the API so the prediction endpoint can load it correctly.

Example payload:

```json
{
  "age": 30,
  "income": 600000,
  "credit_score": 750,
  "loan_amount": 250000,
  "loan_term": 10,
  "employment_years": 4,
  "existing_debt": 10000
}
```
