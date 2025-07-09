# docker/Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Add this to ensure Python recognizes /app as a package root
ENV PYTHONPATH=/app

CMD ["python3", "flask_app/app.py"]
