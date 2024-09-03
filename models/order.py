from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from typing import List



order_products = db.Table(
    "order_products",
    Base.metadata, # allow this table to locate the foreign keys from the Base class
    db.Column('order_id', db.ForeignKey('orders.id'), primary_key= True),
    db.Column('product_id', db.ForeignKey('products.id'), primary_key= True)
)


class Orders(Base):
    
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key= True)
    order_date: Mapped[date] = mapped_column(db.Date, nullable= False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))

    # create our many-one relationship to the customer table
    customer: Mapped['Customers'] = db.relationship(back_populates='orders')
    # create a many-many relationship to Products through our association table order_products
    products: Mapped[List['Products']] = db.relationship(secondary=order_products)