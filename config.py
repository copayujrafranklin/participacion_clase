import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mi-clave-secreta-para-desarrollo-2026'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mi_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False