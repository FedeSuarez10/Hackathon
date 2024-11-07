from flask import Flask, jsonify, request
from extensions import db
from flask_migrate import Migrate
from flask_cors import CORS  
from redis import Redis
from rq import Queue
from rq.job import Job
import os

migrate = Migrate()  
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Import des routes de l'application
from app.routes.videos import videos_blueprint

def create_app():
    app = Flask(__name__)
    
    # Configuration de l'application
    app.config.from_object('config.Config')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    # Configuration de CORS
    CORS(app, origins="*", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])

    # Configuration de Redis et RQ avec les variables d'environnement
    redis_conn = Redis(
        host=os.getenv('REDIS_HOST', 'localhost'),
        port=os.getenv('REDIS_PORT', 6379)
    )
    queue = Queue(connection=redis_conn)

    @app.route('/', methods=['GET'])
    def home():
        return {"message": "Hello, World!"}
    
    # Route pour vérifier le statut d'une tâche
    @app.route('/status/<task_id>', methods=['GET'])
    def job_status(task_id):  
        try:
            job = Job.fetch(task_id, connection=redis_conn)
            return jsonify({"status": job.get_status(), "result": job.result}), 200
        except Exception:
            return jsonify({"error": "Tâche non trouvée"}), 404

    # Enregistrement des extensions et des ressources
    register_extensions(app)
    register_resources(app)

    with app.app_context():
        db.create_all()     

    return app

def register_extensions(app):
    """Initialisation des extensions avec l'application Flask."""
    db.init_app(app)
    migrate.init_app(app, db)

def register_resources(app):
    """Enregistrement des blueprints de l'application."""
    app.register_blueprint(videos_blueprint, url_prefix='/api/videos')
