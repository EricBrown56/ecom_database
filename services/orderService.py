from database import db #services interact directly with the db
from models.order import Orders
from sqlalchemy import select #so we can query our db
from models.product import Products
from datetime import date

def save(order_data):
    new_order = Orders( customer_id=order_data['customer_id'], order_date=date.today())

    for item_id in order_data['items']:
        query = select(Products).where(Products.id==item_id)
        item = db.session.execute(query).scalar()
        new_order.products.append(item)
    
    db.session.add(new_order)
    db.session.commit() 
    db.session.refresh(new_order)# makes sure the data doesnt decouple

    return new_order

def find_all():
    query = select(Orders)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders
