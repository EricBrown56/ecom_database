from flask import Blueprint
from controllers.customerController import save, find_all, login, add_item_to_cart, remove_item_from_cart, view_cart, empty_cart, place_order

customer_blueprint = Blueprint('customer_bp', __name__)

#url_prefix for this blueprint is /customers
customer_blueprint.route('/', methods=['POST'])(save) #triggers the save function on POST request to /customers
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/login', methods=['POST'])(login)
customer_blueprint.route('/add-item', methods=['POST'])(add_item_to_cart)
customer_blueprint.route('/remove-item', methods=['POST'])(remove_item_from_cart)
customer_blueprint.route('/view-cart', methods=['POST'])(view_cart)
customer_blueprint.route('/empty-cart', methods=['POST'])(empty_cart)
customer_blueprint.route('/place-order', methods=['POST'])(place_order)
