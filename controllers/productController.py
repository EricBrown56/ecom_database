from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError



def save(): #name the controller the same as the service it recruits
    try:
        product_data = product_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400 #return error message with a 400 failed response
    
    new_product = productService.save(product_data)
    return jsonify({"status": "success", "message": "product added"}), 201 # send the customer object with a success code


def find_all():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    page = 1 if not page else page
    per_page = 10 if not per_page else per_page
    all_products = productService.find_all(page, per_page)

    return products_schema.jsonify(all_products), 200

