# docker/Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Add this to ensure Python recognizes /app as a package root
ENV PYTHONPATH=/app

CMD ["python", "flask_app/app.py"]
