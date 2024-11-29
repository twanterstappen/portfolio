import pytest
import os
from dotenv import load_dotenv
from flaskr import create_app

load_dotenv('test.env')

@pytest.fixture()
def app():
    app = create_app()

    yield app
    
    
@pytest.fixture()
def client(app):
    return app.test_client()