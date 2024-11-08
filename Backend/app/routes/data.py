from flask import Blueprint
from  app.controllers.data import *

data_blueprint = Blueprint('data', __name__)


# --------------------CRUD-------------------------------
data_blueprint.route('/create', methods=['POST'])(create_data)
data_blueprint.route('/get_data', methods=['GET'])(read_data)



# --------------------SPE_DU_CHEF------------------------
data_blueprint.route('/deleteSpeDuChEF', methods=['DELETE'])(delete_all_data)
