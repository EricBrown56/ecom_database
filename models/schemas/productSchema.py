from . import ma
from marshmallow import fields


class ProductSchema(ma.Schema): #inheriting our instance of Marshmallow
    id = fields.Integer(required=False)
    product_name = fields.String(required=True)
    price = fields.Float(required=True)

    class Meta:
        fields = ('id', 'product_name', 'price')# all fields that could be coming in when validating data

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
     