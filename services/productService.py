from database import db #services interact directly with the db
from models.product import Products
from sqlalchemy import select #so we can query our db


def save(product_data):
    new_product = Products(product_name=product_data['product_name'], price=product_data['price'])
    
    db.session.add(new_product)
    db.session.commit() 
    db.session.refresh(new_product)# makes sure the data doesnt decouple

    return new_product

def find_all():
    query = select(Products)
    all_products = db.session.execute(query).scalars().all()
    return all_products
