import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Flask application configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-for-testing')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///pokemon.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 