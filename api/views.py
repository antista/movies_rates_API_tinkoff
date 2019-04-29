import json

from flask import request

from .models import User, Movie, RatesStorage
from .wsgi import app, db

db.create_all()


@app.route('/api/users/', methods=['GET', 'POST'])
def handle_users_request():
    if request.method == 'POST':
        user = User.create_user(request.json)
        if not user:
            return json.dumps({}), 406
        return user, 201
    if request.method == 'GET':
        users = User.get_users()
        return users, 200
    return 405


@app.route('/api/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user_request(user_id):
    if request.method == 'PUT':
        user = User.update_user(user_id, request.json)
        if not user:
            return json.dumps({}), 204
        return user, 200
    if request.method == 'GET':
        user = User.get_user(user_id)
        if not user:
            return json.dumps({}), 204
        return user, 200
    if request.method == 'DELETE':
        responce = User.delete_user(user_id)
        if not responce:
            return json.dumps({}), 204
        return json.dumps({}), 200
    return 405


@app.route('/api/movies/', methods=['GET', 'POST'])
def handle_movies_request():
    if request.method == 'POST':
        movie = Movie.create_movie(request.json)
        if not movie:
            return json.dumps({}), 406
        return movie, 201
    if request.method == 'GET':
        movies = Movie.get_movies()
        return movies, 200
    return 405


@app.route('/api/movies/<movie_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_movie_request(movie_id):
    if request.method == 'PUT':
        movie = Movie.update_movie(movie_id, request.json)
        if not movie:
            return json.dumps({}), 204
        return movie, 200
    if request.method == 'GET':
        movie = Movie.get_movie(movie_id)
        if not movie:
            return json.dumps({}), 204
        return movie, 200
    if request.method == 'DELETE':
        responce = Movie.delete_movie(movie_id)
        if not responce:
            return json.dumps({}), 204
        return json.dumps({}), 200
    return 405


@app.route('/api/users/<user_id>/rates', methods=['GET', 'POST'])
def handle_rates_request(user_id):
    if request.method == 'POST':
        rate = RatesStorage.make_rate(user_id, request.json)
        if not rate:
            return json.dumps({}), 406
        return rate, 201
    if request.method == 'GET':
        rates = RatesStorage.get_rates(user_id)
        return rates, 200
    return 405


@app.route('/api/users/<user_id>/rates/<rate_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_rate_request(user_id, rate_id):
    if request.method == 'PUT':
        rate = RatesStorage.update_rate(rate_id, request.json)
        if not rate:
            return json.dumps({}), 204
        return rate, 200
    if request.method == 'GET':
        rate = RatesStorage.get_rate(rate_id)
        if not rate:
            return json.dumps({}), 204
        return rate, 200
    if request.method == 'DELETE':
        responce = RatesStorage.delete_rate(rate_id)
        if not responce:
            return json.dumps({}), 204
        return json.dumps({}), 200
    return 405
