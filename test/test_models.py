import json

from api.models import User


def test_user_as_dict(user):
    d = user.as_dict()
    assert type(d) == dict
    assert len(d.keys()) == 4
    assert {'id', 'login', 'email', 'registration_date'} == d.keys()


def test_get_users():
    assert User.get_users() == json.dumps([])
    assert not User.get_user('kek')


def test_update_user():
    assert not User.update_user('kek', [])


def test_movie_as_dict(movie):
    d = movie.as_dict()
    assert len(d.keys()) == 5
    assert 'avr_rate' in d.keys()
    assert d['avr_rate'] == 0
