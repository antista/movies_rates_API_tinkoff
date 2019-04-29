import json
from datetime import datetime
from uuid import uuid4

from api.wsgi import db


class User(db.Model):
    id = db.Column(db.String(80), primary_key=True, nullable=False)
    login = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    registration_date = db.Column(db.DateTime)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    @staticmethod
    def create_user(data):
        if 'login' not in data.keys() or 'email' not in data.keys():
            return None
        user_id = uuid4().hex
        db.session.add(User(id=user_id, login=data['login'], email=data['email'], registration_date=datetime.now()))
        db.session.commit()
        return json.dumps(User.query.get(user_id).as_dict())

    @staticmethod
    def get_user(user_id):
        if User.query.get(user_id) is None:
            return None
        return json.dumps(User.query.get(user_id).as_dict())

    @staticmethod
    def get_users():
        return json.dumps([user.as_dict() for user in User.query])

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)
        if user is None:
            return None
        user.login = user.login if 'login' not in data.keys() else data['login']
        user.email = user.email if 'email' not in data.keys() else data['email']
        db.session.commit()
        return json.dumps(user.as_dict())

    @staticmethod
    def delete_user(user_id):
        if User.query.get(user_id) is None:
            return None
        User.query.filter_by(user_id).delete()
        db.session.commit()
        return True


class Movie(db.Model):
    id = db.Column(db.String(80), primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer)
    country = db.Column(db.String(80), nullable=False)

    def as_dict(self):
        data = {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
        data['avr_rate'] = RatesStorage.get_average_rate(self.id)
        return data

    @staticmethod
    def create_movie(data):
        if 'name' not in data.keys() or 'year' not in data.keys() or \
                not data['year'].isdigit() or len(data['year']) > 4 or 'country' not in data.keys():
            return None
        movie_id = uuid4().hex
        db.session.add(Movie(id=movie_id, name=data['name'], year=int(data['year']), country=data['country']))
        db.session.commit()
        return json.dumps(Movie.query.get(movie_id).as_dict())

    @staticmethod
    def get_movie(movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            return None
        return json.dumps(movie.as_dict())

    @staticmethod
    def get_movies():
        return json.dumps([movie.as_dict() for movie in Movie.query])

    @staticmethod
    def update_movie(movie_id, data):
        movie = Movie.query.get(movie_id)
        if movie is None or ('year' in data.keys() and (not data['year'].isdigit() or len(data['year']) > 4)):
            return None
        movie.name = movie.name if 'name' not in data.keys() else data['name']
        movie.year = movie.year if 'year' not in data.keys() else data['year']
        movie.country = movie.country if 'country' not in data.keys() else data['country']
        db.session.commit()
        return json.dumps(movie.as_dict())

    @staticmethod
    def delete_movie(movie_id):
        if Movie.query.get(movie_id) is None:
            return None
        Movie.query.filter_by(id=movie_id).delete()
        db.session.commit()
        return True


class RatesStorage(db.Model):
    id = db.Column(db.String(80), primary_key=True, nullable=False)
    user_id = db.Column(db.String(80), nullable=False)
    movie_id = db.Column(db.String(80), nullable=False)
    rate = db.Column(db.Integer, default=0)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    @staticmethod
    def make_rate(user_id, data):
        if 'movie_id' not in data.keys() or 'rate' not in data.keys() or \
                not data['rate'].isdigit() or int(data['rate']) < 1 or int(data['rate']) > 10 or \
                RatesStorage.query.filter_by(movie_id=data['movie_id']).first() is not None:
            return None
        rate_id = uuid4().hex
        db.session.add(RatesStorage(id=rate_id, user_id=user_id, movie_id=data['movie_id'], rate=data['rate']))
        db.session.commit()
        print(RatesStorage.query.get(rate_id))
        print(RatesStorage.query.get(rate_id).as_dict())
        return json.dumps(RatesStorage.query.get(rate_id).as_dict())

    @staticmethod
    def get_rates(user_id):
        return json.dumps([rate.as_dict() for rate in RatesStorage.query.filter_by(user_id=user_id)])

    @staticmethod
    def update_rate(rate_id, data):
        rate = RatesStorage.query.get(rate_id)
        if rate is None or ('rate' in data.keys() and (
                not data['rate'].isdigit() or int(data['rate']) < 1 or int(data['rate']) > 10)):
            return None
        rate.rate = rate.rate if 'rate' not in data.keys() else data['rate']
        db.session.commit()
        return json.dumps(rate.as_dict())

    @staticmethod
    def get_rate(rate_id):
        rate = RatesStorage.query.get(rate_id)
        if not rate:
            return None
        return json.dumps(rate.as_dict())

    @staticmethod
    def delete_rate(rate_id):
        if RatesStorage.query.get(rate_id) is None:
            return None
        RatesStorage.query.filter_by(id=rate_id).delete()
        db.session.commit()
        return True

    @staticmethod
    def get_average_rate(movie_id):
        return sum([rate.rate for rate in RatesStorage.query.filter_by(movie_id=movie_id)])
