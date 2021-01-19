import os
import tempfile

import pytest

from digeiz_api.bootstrap import create_app
from digeiz_api.extensions import db
from digeiz_api.models import Account, Mall


@pytest.fixture
def app_client():
    """Client app factory"""
    app = create_app()
    db_fd, app.config["DATABASE"] = tempfile.mkstemp()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield app, client

    os.close(db_fd)
    os.unlink(app.config["DATABASE"])


@pytest.fixture
def client_init_data(app_client):
    app, client = app_client
    with app.app_context():
        mall = Mall(
            name="mall name",
            location="mall location",
            province="Saint Martin",
            city="Grenoble",
            country="France",
            country_code="FR",
            latitude=12.33,
            longitude=-22.32,
        )
        account = Account(
            username="username",
            email="email@mail.com",
            phone="0123456",
            name="account_name",
        )
        account.malls.append(mall)
        db.session.add(account)
        db.session.add(mall)
        db.session.commit()
    return client
