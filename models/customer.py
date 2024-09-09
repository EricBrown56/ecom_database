from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List


class Customers(Base):
    
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(db.String(25), nullable=False)
    username: Mapped[str] = mapped_column(db.String(30), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    admin: Mapped[int] = mapped_column(db.Integer, nullable=False)

    # Create a one-many relationship to Orders table
    orders: Mapped[List["Orders"]] = db.relationship(back_populates='customers')
    #create a cart many to many relationship between customer and products
    #customer_products association table will be the CART should look just like order_products
    #cart: Mapped[List['Products]] = db.relationship(secondary=cart)

    #customer.cart.append(<product object>)
    #customer.cart.remove(<product object>)

    #will need db.session.add and db.session.commit after adding and removing items

    #view would be return cart

    #place order will utilize the customers cart do a for loop for item in customer.cart, order.append item and customer.cart.remove item
    #you will add both the customer and the order and commit them both