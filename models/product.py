from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from models.orderProduct import order_products
from typing import List
from models.cart import cart

class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    product_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[float] = mapped_column(db.Float(255), nullable=False)

    orders: Mapped[List['Orders']] = db.relationship(secondary=order_products)
    cart: Mapped[List['Products']] = db.relationship(secondary=cart)
    