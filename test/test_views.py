import json

from api.wsgi import app


def test_handle_users_request_get(mocker, test_client):
    mocker.patch('api.models.User.get_users', return_value=json.dumps({}))
    with app.test_request_context():
        response = test_client.get('/api/users/')
        assert response.status_code == 200
        assert response.data.decode() == '{}'


def test_handle_users_request_post(mocker, test_client):
    mocker.patch('api.models.User.create_user', return_value=None)
    with app.test_request_context():
        response = test_client.post('/api/users/')
        assert response.status_code == 406
        assert response.data.decode() == '{}'
    mocker.patch('api.models.User.create_user', return_value=json.dumps({}))
    with app.test_request_context():
        response = test_client.post('/api/users/')
        assert response.status_code == 201


def test_handle_users_request_unknown(test_client):
    with app.test_request_context():
        response = test_client.put('/api/users/')
        assert response.status_code == 405


def test_handle_user_request_get(mocker, test_client):
    mocker.patch('api.models.User.get_user', return_value=None)
    with app.test_request_context():
        response = test_client.get('/api/users/123')
        assert response.status_code == 204
    mocker.patch('api.models.User.get_user', return_value=json.dumps({}))
    with app.test_request_context():
        response = test_client.get('/api/users/123')
        assert response.status_code == 200
        assert response.data.decode() == '{}'
