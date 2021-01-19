from typing import Type, Optional, List

from flask import Flask
from flask.views import MethodView


def register_api(
        app: Flask,
        view: Type[MethodView],
        endpoint: str,
        url: str,
        pk: Optional[str] = None,
        pk_type: Optional[str] = None,
        methods: Optional[List[str]] = None,
):
    """Syntactic sugar for registering multiple API endpoints.
    Taken from: https://flask.palletsprojects.com/en/1.1.x/views/
    :param app:  Flask application object
    :param view: Method view
    :param endpoint: FQDN view name, i.e. account_view
    :param url: http endpoint, i.e. /api/accounts
    :param pk: Optional[str] object identifier
    :param pk_type: Optional[str], only specify when `pk` is specified. i.e. int
    :param methods: register methods, i.e. ["GET"]
    """
    if not methods:
        methods = ["GET", "PUT", "PATCH", "POST", "DELETE"]
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, view_func=view_func, methods=methods)