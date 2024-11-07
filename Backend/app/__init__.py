from flask import Flask
from extensions import db
from flask_migrate import Migrate
from flask_cors import CORS
import os

from app.routes.videos import videos_blueprint

# Initialisation des extensions
migrate = Migrate()

# Chemin de sauvegarde des fichiers uploadés
UPLOAD_FILES_FOLDER = 'Upload_Files'
os.makedirs(UPLOAD_FILES_FOLDER, exist_ok=True)

def create_app():
    app = Flask(__name__)
    
    # Activer CORS
    CORS(app)
    
    # Charger la configuration depuis config.py
    app.config.from_object('config.Config')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FILES_FOLDER  # Configurer le chemin d'upload

    # Route de test de l'application
    @app.route('/', methods=['GET'])
    def home():
        return {"message": "Hello, World!"}

    # Initialiser les extensions et enregistrer les blueprints
    register_extensions(app)
    register_resources(app)

    # Créer les tables dans la base de données si elles n'existent pas encore
    with app.app_context():
        db.create_all()

    return app

def register_extensions(app):
    """Initialise les extensions avec l'application Flask."""
    db.init_app(app)            # Initialiser la base de données avec l'application
    migrate.init_app(app, db)    # Associer Flask-Migrate avec l'app et db

def register_resources(app):
    """Enregistre les blueprints de l'application."""
    app.register_blueprint(videos_blueprint, url_prefix='/api/videos')
