from flask import Flask, jsonify, request
from extensions import db
from flask_migrate import Migrate
from flask_cors import CORS  
from redis import Redis
from rq import Queue
from rq.job import Job
from video_processor import process_video  
import uuid
import os

migrate = Migrate()  

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    CORS(app, origins="*", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])

    # Configuration de Redis et RQ avec les variables d'environnement
    redis_conn = Redis(
        host=os.getenv('REDIS_HOST', 'redis_cache'),
        port=os.getenv('REDIS_PORT', 6379)
    )
    queue = Queue(connection=redis_conn)

    # Dictionnaire pour stocker le statut des tâches
    task_status = {}
    
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

        # Enregistrer la vidéo sur le disque
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
        video.save(video_path)

        # Ajouter la tâche à la file d'attente pour le traitement de la vidéo
        job = queue.enqueue(process_video, video_path)
        task_status[job.id] = "Processing"

        return jsonify({"message": "Vidéo en cours de traitement", "task_id": job.id}), 200

    @app.route('/status/<task_id>', methods=['GET'])
    def job_status(task_id):  
        job = Job.fetch(task_id, connection=redis_conn) 
        return jsonify({"status": job.get_status(), "result": job.result}), 200

    register_extensions(app)
    register_resources(app)

    with app.app_context():
        db.create_all()     
    return app

def register_extensions(app):
    """Initialize extensions with the Flask app."""
    db.init_app(app)
    migrate.init_app(app, db)

def register_resources(app):
    """Register application blueprints."""
    # App configuration, routes or blueprints
