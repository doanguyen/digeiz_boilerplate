from flask import Flask

from digeiz_api.config import DB_URI, DEBUG
from digeiz_api.extensions import db, migrate, ma
from digeiz_api.utils import register_api
from digeiz_api.views import AccountAPI, SingleAccountAPI, account_malls_api


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = DEBUG

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    register_api(app, AccountAPI, "accounts", "/api/accounts", methods=["GET", "POST"])
    register_api(
        app,
        SingleAccountAPI,
        "single_account",
        "/api/accounts/",
        pk="pk",
        pk_type="int",
        methods=["GET", "PUT", "PATCH", "DELETE"],
    )
    app.add_url_rule(
        "/api/accounts/<int:pk>/malls",
        view_func=account_malls_api,
        methods=["GET", "POST"],
    )
    return app
