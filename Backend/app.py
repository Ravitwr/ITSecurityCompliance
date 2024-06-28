from flask import Flask
from flask_cors import CORS

from config import SystemConfig, config
from controller import blueprint, health_check
from database import init_db, init_ma


def create_app(config: SystemConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(health_check.app)
    app.register_blueprint(blueprint.app, url_prefix="/api/v1")

    init_db(app)
    init_ma(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    return app


app = create_app(config)
