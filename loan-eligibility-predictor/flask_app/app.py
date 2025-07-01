from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

from .routes import api_bp
from .config import Config
from .db import db

metrics = PrometheusMetrics()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    metrics.init_app(app)
    app.register_blueprint(api_bp)
    return app

if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)
