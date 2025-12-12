# test_server.py
import pytest
from my_server import app  # make sure your flask file is named my_server.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    rv = client.get('/health')
    assert rv.json['ok'] == True
 
def test_login_generates_token(client):
    rv = client.post('/login', json={'id': 'alice@example.com'})
    json_data = rv.get_json()
    assert json_data['ok'] == True
    assert 'uuid_token' in json_data
    assert len(json_data['uuid_token']) == 36  # UUID format

def test_verify_valid_token(client):
    # First login to get a token
    login = client.post('/login', json={'id': 'bob@uconn.edu'})
    token = login.get_json()['uuid_token']

    # Now verify
    rv = client.post('/verify', json={'id': 'bob@uconn.edu', 'uuid-token': token})
    assert rv.get_json()['valid'] == True

def test_verify_invalid_token(client):
    rv = client.post('/verify', json={'id': 'bob@uconn.edu', 'uuid-token': 'fake-token'})
    assert rv.get_json()['valid'] == False