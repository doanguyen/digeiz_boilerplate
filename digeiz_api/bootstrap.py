from flask import Flask

from digeiz_api.extensions import db, migrate


def create_app() -> Flask:
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app)
    return app
