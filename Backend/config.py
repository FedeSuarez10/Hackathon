import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    Debug = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','default_database_url')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_TOKEN_KEY = os.getenv('SECRET_TOKEN_KEY', 'default_secret_token')
if not Config.SQLALCHEMY_DATABASE_URI:
    raise ValueError("DATABASE_URL n'est pas définie. Veuillez l'ajouter au fichier .env.")