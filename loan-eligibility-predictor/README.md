# Loan Eligibility Predictor – ML Inference Monitoring App

This app provides an API for predicting loan approval using a TensorFlow model. It logs predictions to MySQL and exposes Prometheus metrics for visualization in Grafana.

## Usage

Build and run all services:

```bash
docker-compose -f docker/docker-compose.yml up --build
```

The API will be available at `http://localhost:5000/predict`.
