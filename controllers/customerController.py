from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema, customer_login
from services import customerService
from marshmallow import ValidationError
from cache import cache
from utils.util import token_required, user_validation, admin_required


def save(): #name the controller the same as the service it recruits
    try:
        customer_data = customer_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    customer = customerService.save(customer_data)
    return customer_schema.jsonify(customer), 201 # send the customer object with a success code

#@cache.cached(timeout=60)
@token_required
def find_all():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    page = 1 if not page else page
    per_page = 10 if not per_page else per_page
    all_customers = customerService.find_all(page, per_page)

    return customers_schema.jsonify(all_customers), 200

def login():
    try:
        credentials = customer_login.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400 #invalid credential payload
    
    token = customerService.login(credentials)

    if token:
        response = {
            "status": "success",
            "message": "successfully logging in",
            "token": token
        }
        return jsonify(response), 200
    else:
        return jsonify({"status": "error", "message": "invalid username or password"}), 404
    
    
def add_item_to_cart():
    try:
        item_data = customer_login.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400 #invalid credential payload

    customer = customerService.add_item_to_cart(item_data)
    return customer_schema.jsonify(customer), 200

def remove_item_from_cart():
    try:
        item_data = customer_login.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400 #invalid credential payload

    customer = customerService.remove_item_from_cart(item_data)
    return customer_schema.jsonify(customer), 200

def view_cart():
    try:
        item_data = customer_login.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400 #invalid credential payload

    customer = customerService.view_cart(item_data)
    return customer_schema.jsonify(customer), 200


def empty_cart():
    try:
        item_data = customer_login.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400 #invalid credential payload

    customer = customerService.empty_cart(item_data)
    return customer_schema.jsonify(customer), 200


def place_order():
    try:
        item_data = customer_login.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400 #invalid credential payload

    customer = customerService.place_order(item_data)
    return customer_schema.jsonify(customer), 200




