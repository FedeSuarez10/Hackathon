from flask import Flask
from extensions import db
from flask_migrate import Migrate
from flask_cors import CORS  
import os


from app.routes.videos import videos_blueprint




migrate = Migrate()  

UPLOAD_FILES_FOLDER = 'Upload_Files'
os.makedirs(UPLOAD_FILES_FOLDER, exist_ok=True)  
def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')


    
    @app.route('/', methods=['GET'])
    def home():
        return {"message": "Hello, World!"}

    register_extensions(app)
    register_resources(app)

    with app.app_context():
        db.create_all() 
    return app

def register_extensions(app):
    """Initialize extensions with the Flask app."""
    db.init_app(app)
    migrate.init_app(app, db)  # Associate Migrate with the app and db

def register_resources(app):
    """Register application blueprints."""

    #use BDD 
    app.register_blueprint(videos_blueprint, url_prefix='/api/videos')