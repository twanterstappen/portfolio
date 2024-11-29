import pytest


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Ethical Hacker" in response.data
    
def test_any(client):
    response = client.get('/does-not-exist')
    assert response.status_code == 302  
    assert b"Redirecting" in response.data  
    assert response.headers["Location"]
    assert response.headers["Location"] == "/coming-soon" 
    
def test_coming_soon(client):
    response = client.get('/coming-soon')
    assert response.status_code == 200
    assert b"Coming Soon" in response.data