from flask import Flask
from database import db
from models.customer import Customers
from models.product import Products
from models.order import Orders
from models.schemas import ma
from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint
from limiter import limiter
from cache import cache
from models.orderProduct import order_products


def create_app(config_name):
    app = Flask(__name__) # instantiate the Flask app

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    blueprint_config(app)
    rate_limit_config(app)
    cache.init_app(app)

    return app


def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')


def rate_limit_config(app):
    limiter.init_app(app)
    limiter.limit('20 per hour')(customer_blueprint)
    limiter.limit('20 per hour')(product_blueprint)
    limiter.limit('20 per hour')(order_blueprint)

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    with app.app_context():
        db.create_all()

    app.run()