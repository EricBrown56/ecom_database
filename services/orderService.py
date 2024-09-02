from database import db #services interact directly with the db
from models.order import Orders
from sqlalchemy import select #so we can query our db


def save(order_data):
    new_order = Orders(order_date=order_data['order_date'], customer_id=order_data['customer_id'])
    
    db.session.add(new_order)
    db.session.commit() 
    db.session.refresh(new_order)# makes sure the data doesnt decouple

    return new_order

def find_all():
    query = select(Orders)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders
