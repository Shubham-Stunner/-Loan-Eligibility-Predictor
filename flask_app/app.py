from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

from flask_app.routes import api_bp
from flask_app.config import Config
from flask_app.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Updated line – pass app to PrometheusMetrics
    PrometheusMetrics(app)

    app.register_blueprint(api_bp)
    return app

if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)
