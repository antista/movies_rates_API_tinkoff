import json
from datetime import datetime
from uuid import uuid4

from api.wsgi import db
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase

Base = declarative_base(cls=(JsonSerializableBase,))


class User(db.Model):
    id = db.Column(db.String(80), primary_key=True, nullable=False)
    login = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    registration_date = db.Column(db.DateTime)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    @staticmethod
    def create_user(data):
        user_id = uuid4().hex
        db.session.add(User(id=user_id, login=data['login'], email=data['email'], registration_date=datetime.now()))
        db.session.commit()
        return json.dumps(User.query.get(user_id).as_dict())

    @staticmethod
    def get_user(user_id):
        if User.query.get(user_id) is None:
            return False
        return json.dumps(User.query.get(user_id).as_dict())

    @staticmethod
    def get_users():
        return json.dumps([user.as_dict() for user in User.query])

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)
        if user is None:
            return False
        user.login = user.login if 'login' not in data.keys() else data['login']
        user.email = user.email if 'email' not in data.keys() else data['email']
        db.session.commit()
        return json.dumps(user.as_dict())

    @staticmethod
    def delete_user(user_id):
        if User.query.get(user_id) is None:
            return False
        User.query.filter_by(user_id).delete()
        db.session.commit()
        return True


class Movie(db.Model, Base):
    id = db.Column(db.String(80), primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer)
    country = db.Column(db.String(80), nullable=False)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    @staticmethod
    def create_movie(data):
        movie_id = uuid4().hex
        db.session.add(Movie(id=movie_id, name=data['name'], year=int(data['year']), country=data['country']))
        db.session.commit()
        return json.dumps(Movie.query.get(movie_id).as_dict())

    @staticmethod
    def get_movie(movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            return False
        return json.dumps(movie.as_dict())

    @staticmethod
    def get_movies():
        return json.dumps([movie.as_dict() for movie in Movie.query])

    @staticmethod
    def update_movie(movie_id, data):
        movie = User.query.get(movie_id)
        if movie is None:
            return False
        movie.name = movie.name if 'name' not in data.keys() else data['name']
        movie.year = movie.year if 'year' not in data.keys() else data['year']
        movie.country = movie.country if 'country' not in data.keys() else data['country']
        db.session.commit()
        return json.dumps(movie.as_dict())

    @staticmethod
    def delete_movie(movie_id):
        if Movie.query.get(id=movie_id) is None:
            return False
        Movie.query.filter_by(id=movie_id).delete()
        db.session.commit()
        return True


class RateStorage(db.Model):
    id = db.Column(db.String(80), primary_key=True, nullable=False)
    user = db.Column(db.String(80), primary_key=True, nullable=False)
    rate = db.Column(db.Integer)
