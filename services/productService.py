from database import db #services interact directly with the db
from models.product import Products
from sqlalchemy import select #so we can query our db


def save(product_data):
    new_product = Products(product_name=product_data['product_name'], price=product_data['price'])
    
    db.session.add(new_product)
    db.session.commit() 
    db.session.refresh(new_product)# makes sure the data doesnt decouple

    return new_product

def find_all(page=1, per_page=10):
    query = select(Products)
    all_products = db.paginate(query, page=int(page), per_page=int(per_page))
    return all_products

def search_product(search_term):
    query = select(Products).where(Products.product_name.like(f'%{search_term}%'))
    search_products = db.session.execute(query).scalars().all()
    return search_products