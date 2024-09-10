from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from utils.util import user_validation, admin_required

@user_validation
def place_order(cart): #name the controller the same as the service it recruits
    try:
        order_data = order_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    if token_id == order_data['customer_id']:
        new_order = orderService.save(order_data)
        return order_schema.jsonify(new_order), 201 # send the customer object with a success code
    else:
        return jsonify({"message":"You cant order things for other users."})