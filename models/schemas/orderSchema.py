from . import ma
from marshmallow import fields


class OrderSchema(ma.Schema):
    id = fields.Integer(required= False)
    order_date = fields.Date(required= False)
    customer_id = fields.Integer(required= True)

    class Meta:
        fields = ('id', 'order_date', 'customer_id', 'items') # items will be a list of product id's associated with an order

order_schema = OrderSchema()
orders_schema = OrderSchema(many= True)