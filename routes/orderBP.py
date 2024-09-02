from flask import Blueprint
from controllers.orderController import save, find_all

order_blueprint = Blueprint('order_bp', __name__)

#url_prefix for this blueprint is /orders
order_blueprint.route('/', methods=['POST'])(save) #triggers the save function on POST request to /orders
order_blueprint.route('/', methods=['GET'])(find_all)