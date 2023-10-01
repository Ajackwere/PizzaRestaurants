from flask import Flask, make_response, request, jsonify, abort
from flask_migrate import Migrate
# from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://austine:0ypd6XocLkp7X2mEJc6LVZlde382o9QX@dpg-cka02mtdrqvc739q0u1g-a.ohio-postgres.render.com/bird_app_14hv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

# GET /restaurants
api = Api(app)


class RestaurantsResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        return jsonify([restaurant.serialize() for restaurant in restaurants])


# Get their restaurants id


class RestaurantByID(Resource):

    def get(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            return jsonify(restaurant.serialize())
        else:
            return jsonify({"error": "Restaurant not found"}), 404

    def delete(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        else:
            return jsonify({"error": "Restaurant not found"}), 404


class PizzzasResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        return jsonify([pizza.serialize() for pizza in pizzas])


class RestaurantPizzasResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('pizza_id', type=int, required=True)
        parser.add_argument('restaurant_id', type=int, required=True)
        args = parser.parse_args()

        price = args['price']
        pizza_id = args['pizza_id']
        restaurant_id = args['restaurant_id']

        # code to validate the data and create RestayrantPizza

        if price is not None and 1 <= price <= 30:
            restaurant_pizza = RestaurantPizza(
                price=price, pizza_id=pizza_id, restaurant_id=restaurant_id
            )
            db.session.add(restaurant_pizza)
            db.session.commit()
            return jsonify(restaurant_pizza.pizza.serialize()), 201
        else:
            return jsonify({"errors": ["Validation errors"]}), 400


api.add_resource(RestaurantsResource, '/restaurants')
api.add_resource(RestaurantByID, '/restaurants/<int:id>')
api.add_resource(PizzasResource, '/pizzas')
api.add_resource(RestaurantPizzasResource, '/restaurant_pizzas')


if __name__ == '__main__':
    app.run(debug=True)
