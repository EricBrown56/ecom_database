from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from utils.util import user_validation, admin_required

@user_validation
def save(token_id): #name the controller the same as the service it recruits
    try:
        order_data = order_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    if token_id == order_data['customer_id']:
        new_order = orderService.save(order_data)
        return order_schema.jsonify(new_order), 201 # send the customer object with a success code
    else:
        return jsonify({"message":"You cant order things for other users."})

@admin_required
def find_all():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    page = 1 if not page else page
    per_page = 10 if not per_page else per_page
    all_orders = orderService.find_all(page, per_page)

    return orders_schema.jsonify(all_orders), 200

def find_by_id(order_id):
    order = orderService.find_by_id(order_id)

    return order_schema.jsonify(order), 200
@user_validation
def find_by_customer_id(customer_id, token_id):
    if customer_id == token_id:
        orders = orderService.find_by_customer_id(customer_id)
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({"message": "Cannot view other customers orders."})

def find_by_email():
    email = request.json['email']
    if email:
        orders = orderService.find_by_email(email)
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({"message":"Please insert an email"})