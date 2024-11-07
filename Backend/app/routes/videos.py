from flask import Blueprint
from app.controllers.videos import upload

videos_blueprint = Blueprint('videos', __name__)

videos_blueprint.route('/upload', methods=['POST'])(upload)

