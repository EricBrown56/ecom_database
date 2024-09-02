from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from cache import cache


def save(): #name the controller the same as the service it recruits
    try:
        customer_data = customer_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    customer = customerService.save(customer_data)
    return customer_schema.jsonify(customer), 201 # send the customer object with a success code

@cache.cached(timeout=60)
def find_all():
    all_customers = customerService.find_all()

    return customers_schema.jsonify(all_customers), 200