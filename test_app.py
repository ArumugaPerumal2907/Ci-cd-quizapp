from flask import Flask
import pytest
from apquiz_app.app import app, get_db_connection

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Quiz App' in response.data

def test_register(client):
    response = client.post('/register', data={'email': 'test@example.com', 'password': 'password123'})
    assert response.status_code == 302  # Redirect after successful registration
    assert b'Registration successful! Please log in.' in response.data

def test_login(client):
    client.post('/register', data={'email': 'test@example.com', 'password': 'password123'})
    response = client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    assert response.status_code == 302  # Redirect after successful login
    assert b'Dashboard' in response.data

def test_logout(client):
    client.post('/register', data={'email': 'test@example.com', 'password': 'password123'})
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    response = client.get('/logout')
    assert response.status_code == 302  # Redirect after logout
    assert b'Welcome to the Quiz App' in response.data

def test_quiz(client):
    client.post('/register', data={'email': 'test@example.com', 'password': 'password123'})
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    response = client.get('/quiz')
    assert response.status_code == 200
    assert b'Quiz Questions' in response.data

def test_results(client):
    client.post('/register', data={'email': 'test@example.com', 'password': 'password123'})
    client.post('/login', data={'email': 'test@example.com', 'password': 'password123'})
    client.get('/quiz')  # Simulate taking the quiz
    response = client.get('/results')
    assert response.status_code == 200
    assert b'Results' in response.data

def test_db_connection():
    conn = get_db_connection()
    assert conn.is_connected()  # Ensure the database connection is successful
    conn.close()