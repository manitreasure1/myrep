from app import  create_app
import pytest
import os
from app.core.extensions import sqlmodel
app = create_app()


@pytest.fixture()
def my_app():
    flask_app = app
    flask_app.config.update({
        "TESTING":True
    })
    yield app


@pytest.fixture(scope="module")
def client():
    os.environ['CONFIG_TYPE'] = "config.TestingConfig"
    flask_app = app
    with flask_app.test_client() as client:
        with flask_app.app_context():
            yield client
            sqlmodel.init_db()