import os
import secrets
import datetime

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

INSTANCE_DIR = os.path.join(os.path.abspath(os.path.join(BASE_DIR, os.pardir, 'instance')))
print


class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(64))  # Replace with a secure key in production
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f"sqlite:///{os.path.join(INSTANCE_DIR, 'app.sqlite')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=30)
    SESSION_COOKIE_SAMESITE = 'Strict'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    USER_RELOAD = True
    

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    USER_RELOAD = False

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # In-memory database for testing
