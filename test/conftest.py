import pytest

from api import wsgi
from api.models import User, Movie


@pytest.fixture
def app():
    return wsgi.app


@pytest.fixture
def user():
    return User(login='login', email='kek@mai.ru')


@pytest.fixture
def movie():
    return Movie(name='movie', year=1999, country='USA')


@pytest.fixture(scope='module')
def test_client():
    flask_app = wsgi.app
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
