import os
from flask import current_app, request, jsonify
from extensions import db
import logging
from rq import Queue
from rq.job import Job
from video_processor import process_video  
from redis import Redis
import uuid


def upload_video():
    # Vérification du fichier vidéo dans la requête
    if 'video' not in request.files:
        return jsonify({"error": "Aucun fichier vidéo fourni"}), 400

    video = request.files['video']
    
    if video.filename == '':
        return jsonify({"error": "Nom de fichier vide"}), 400

    # Chemin d'enregistrement de la vidéo
    video_path = os.path.join(current_app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)

    # Connexion Redis et file d'attente
    redis_conn = Redis(
        host=current_app.config.get('REDIS_HOST', 'localhost'),
        port=current_app.config.get('REDIS_PORT', 6379)
    )
    queue = Queue(connection=redis_conn)

    # Ajout de la tâche pour le traitement de la vidéo
    job = queue.enqueue(process_video, video_path)

    # Renvoie l'identifiant de tâche au client
    return jsonify({"message": "Vidéo en cours de traitement", "task_id": job.id}), 200
