import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

      # Teardown the database
        # with app.app_context():
            # db.drop_all()

def test_register(client):
    response = client.post('/register', json={
        'username': 'testuser4',
        'password': 'testpass'
    })
    assert response.status_code == 201
    assert b'User created' in response.data

def test_login(client):
    client.post('/register', json={'username': 'testuser5', 'password': 'testpass'})
    response = client.post('/login', json={
        'username': 'testuser5',
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert b'Logged in successfully' in response.data

def test_login_fail(client):
    response = client.post('/login', json={
        'username': 'testuser1',
        'password': 'wrongpass'
    })
    assert response.status_code == 401
    assert b'Login failed' in response.data
