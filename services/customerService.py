from database import db #services interact directly with the db
from models.customer import Customers #need this to create customer objects
from sqlalchemy import select #so we can query our db


def save(customer_data):
    new_customer = Customers(name=customer_data['name'], email=customer_data['email'], 
                    phone=customer_data['phone'], username=customer_data['username'], 
                    password=customer_data['password'])
    
    db.session.add(new_customer)
    db.session.commit() # adding our new customer to our db

    db.session.refresh(new_customer)# makes sure the data doesnt decouple

    return new_customer

def find_all():
    query = select(Customers)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers
