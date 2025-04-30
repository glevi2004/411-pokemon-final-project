import pytest

from pokemon.app import create_app
from config import Config
from pokemon.db import db

@pytest.fixture
def app():
    app = create_app(Config)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def session(app):
    with app.app_context():
        yield db.session