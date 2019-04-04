import json

from flask import request

from .models import User, Movie, RateStorage
from .wsgi import app, db

db.drop_all()
db.create_all()


@app.route('/api/users/', methods=['GET', 'POST'])
def handle_users_request():
    if request.method == 'POST':
        user = User.create_user(request.json)
        return user, 201
    if request.method == 'GET':
        users = User.get_users()
        return users, 200
    return 400


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
    return 400


@app.route('/api/movies/', methods=['GET', 'POST'])
def handle_movies_request():
    if request.method == 'POST':
        movie = Movie.create_movie(request.json)
        return movie, 201
    if request.method == 'GET':
        movies = Movie.get_movies()
        return movies, 200
    return 400


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
    return 400
