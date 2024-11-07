from flask import Flask, jsonify, request
from extensions import db
from flask_migrate import Migrate
from flask_cors import CORS  
import os

migrate = Migrate()  

UPLOAD_FILES_FOLDER = 'Upload_Files'
os.makedirs(UPLOAD_FILES_FOLDER, exist_ok=True)  
def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    CORS(app, origins="*", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])
    # CORS(app, origins="https://monappfrontend.com", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])


    
    @app.route('/', methods=['GET'])
    def home():
        return {"message": "Hello, World!"}
    
    @app.route('/upload_video', methods=['POST'])
    def upload_video():
        if 'video' not in request.files:
            return jsonify({"error": "Aucun fichier vidéo fourni"}), 400

        video = request.files['video']
        
        if video.filename == '':
            return jsonify({"error": "Nom de fichier vide"}), 400

        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
        video.save(video_path)
        
        return jsonify({"message": "Vidéo sauvegardée avec succès", "path": video_path}), 200

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

    # app.register_blueprint(exploits_blueprint, url_prefix='/api/exploits')

    #not use BDD