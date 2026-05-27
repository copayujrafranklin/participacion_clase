import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///mi_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False