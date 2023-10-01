from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules = ('-restaurant_pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(250), nullable=False)

    pizzas = db.relationship(
        'Pizza', secondary='restaurant_pizzas', backref='restaurants')

    def __repr__(self):
        return f'<Restaurant {self.name}>'


class Pizza(db.Model):
    __tablename__ = 'pizzas'
    serialize_rules = ('-restaurant_pizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)

    restaurants = db.relationship(
        'Restaurant', secondary='restaurant_pizzas', backref='pizzas')

    def __repr__(self):
        return f'<Pizza {self.name}>'


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    serialize_rules = ('-restaurant.pizzas', '-pizza.restaurants',)

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey(restaurants.id), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey(
        'pizzas.id'), nullable=False)
    price = db.Column(db.Float, nullable=False,
                      check_constraint='price >= 1 AND price <= 30')

    restaurant = db.relationship('Restaurant', backref=db.backref(
        'restaurant_pizzas', cascade='all, delete-orphan'))
    pizza = db.relationship('Pizza', backref=db.backref(
        'restaurant_pizzas', cascade='all, delete-orphan'))
    
    def __repr__(self):
        return f'<RestaurantPizza {self.id}>'
    