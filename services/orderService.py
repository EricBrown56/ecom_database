from database import db #services interact directly with the db
from models.order import Orders
from sqlalchemy import select #so we can query our db
from models.product import Products
from datetime import date
from models.customer import Customers

def save(order_data):
    new_order = Orders( customer_id=order_data['customer_id'], order_date=date.today())

    for item_id in order_data['items']: #for item in customer.cart
        query = select(Products).where(Products.id==item_id)
        item = db.session.execute(query).scalar()
        new_order.products.append(item)
        #customer.cart.remove(item)
    
    db.session.add(new_order)
    db.session.commit() 
    db.session.refresh(new_order)# makes sure the data doesnt decouple

    return new_order

def find_all(page=1, per_page=10):
    query = select(Orders)
    all_orders = db.paginate(query, page=int(page), per_page=int(per_page))
    
    return all_orders


def find_by_id(order_id):
    query = select(Orders).where(Orders.id==order_id)
    order = db.session.execute(query).scalar()

    return order

def find_by_customer_id(customer_id):
    query = select(Orders).where(Orders.customer_id == customer_id)
    orders = db.session.execute(query).scalars().all()
    
    return orders

def find_by_email(email):
    query = select(Orders).join(Customers).where(Customers.id==Orders.customer_id).where(Customers.email == email)
    orders = db.session.execute(query).scalars().all()

    return orders

