# from app import app, db
# from models import Restaurant, Pizza, RestaurantPizza
# from faker import Faker
# import random

# fake = Faker()


# def create_random_data():
#     # Create sample data
#     restaurants = []
#     pizzas = []

#     for _ in range(10):  # Create 10 random restaurants
#         restaurant = Restaurant(
#             name=fake.company(), address=fake.address())
#         restaurants.append(restaurant)

#     for _ in range(10):  # Create 10 random pizzas
#         pizza = Pizza(
#             name=fake.word(), ingredients=fake.sentence())
#         pizzas.append(pizza)

#     db.session.add_all(restaurants)
#     db.session.add_all(pizzas)
#     db.session.commit()


# def create_random_relations():
#     # Create random RestaurantPizza associations
#     for _ in range(20):  # Create 20 random associations
#         restaurant = random.choice(Restaurant.query.all())
#         pizza = random.choice(Pizza.query.all())
#         price = round(random.uniform(1, 30), 2)
#         restaurant_pizza = RestaurantPizza(
#             restaurant=restaurant, pizza=pizza, price=price)
#         db.session.add(restaurant_pizza)

#     db.session.commit()


# if __name__ == '__main__':
#     # Create random data and relations
#     create_random_data()
#     create_random_relations()

#     print('Database seeded successfully with Faker data.')
