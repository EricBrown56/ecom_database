from database import db, Base

cart = db.Table(
    "cart",
    Base.metadata, # allow this table to locate the foreign keys from the Base class
    db.Column('customer_id', db.ForeignKey('customers.id'), primary_key= True),
    db.Column('product_id', db.ForeignKey('products.id'), primary_key= True)
)
