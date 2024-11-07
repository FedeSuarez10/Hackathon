from flask import Blueprint
from  app.controllers.videos import *

videos_blueprint = Blueprint('videos', __name__)



videos_blueprint.route('/upload_video', methods=['POST'])(upload_video)
