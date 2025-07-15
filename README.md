# Loan Eligibility Predictor – ML Inference Monitoring App

This app provides an API for predicting loan approval using a TensorFlow model. It logs predictions to MySQL and exposes Prometheus metrics for visualization in Grafana.

## Prerequisites

Ensure Docker and Docker&nbsp;Compose are installed and running. On Ubuntu you can use:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
sudo chmod 666 /var/run/docker.sock
```

Log out and back in after adding your user to the docker group.

## Setup

Create a `.env` file in the project root with the following variables:

```bash
FLASK_ENV=development
DB_HOST=db
DB_PORT=3306
DB_NAME=loan_predictor
DB_USER=root
DB_PASSWORD=rootpass
MODEL_PATH=model/loan_model_v1.h5
MODEL_VERSION=v1.0
```

Next generate the TensorFlow model required by the API:

```bash
docker run --rm -v "$(pwd):/app" -w /app python:3.10 \
  bash -c "pip install tensorflow && python model/generate_dummy_model.py 7"
```

This creates `model/loan_model_v1.h5`.

## Usage

Build and start all services:

```bash
docker-compose -f docker/docker-compose.yml up --build -d
```

The App will be available at `http://localhost:5000/`
