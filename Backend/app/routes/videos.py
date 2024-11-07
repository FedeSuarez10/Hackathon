from flask import Blueprint
from  app.controllers.videos import *

videos_blueprint = Blueprint('videos', __name__)