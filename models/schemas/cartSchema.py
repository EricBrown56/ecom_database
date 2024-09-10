from . import ma
from marshmallow import fields

class CartSchema(ma.Schema):
    id = fields.Integer(required= False)
    customer_id = fields.Integer(required= True)
    products = fields.Nested('ProductSchema', many=True)

    class Meta:
        fields = ('id', 'customer_id', 'items', 'products') 

cart_schema = CartSchema()
