from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from typing import List
from models.orderProduct import order_products





class Orders(Base):
    
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key= True)
    order_date: Mapped[date] = mapped_column(db.Date, nullable= False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))

    # create our many-one relationship to the customer table
    customers: Mapped['Customers'] = db.relationship(back_populates='orders')
    # create a many-many relationship to Products through our association table order_products
    products: Mapped[List['Products']] = db.relationship(secondary=order_products)