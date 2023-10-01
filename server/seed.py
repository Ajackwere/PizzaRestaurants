from app import app, db
from models import Restaurant, Pizza, RestaurantPizza
from faker import Faker

# Create a Flask app context
app.app_context().push()

# Clear existing data (optional)
db.drop_all()
db.create_all()

# Create a Faker instance
fake = Faker()

# Generate and add 10 restaurants
restaurants = []
for _ in range(10):
    restaurant = Restaurant(
        name=fake.company(),
        address=fake.address()
    )
    restaurants.append(restaurant)
    db.session.add(restaurant)

# Generate and add 10 pizzas
pizzas = []
for _ in range(10):
    pizza = Pizza(
        name=fake.word(),
        ingredients=fake.sentence()
    )
    pizzas.append(pizza)
    db.session.add(pizza)

# Generate and add 20 restaurant_pizzas (randomly pairing restaurants and pizzas)
restaurant_pizzas = []
for _ in range(20):
    restaurant = fake.random_element(restaurants)
    pizza = fake.random_element(pizzas)
    price = fake.random_int(min=1, max=30)
    restaurant_pizza = RestaurantPizza(
        restaurant=restaurant,
        pizza=pizza,
        price=price
    )
    restaurant_pizzas.append(restaurant_pizza)
    db.session.add(restaurant_pizza)

# Commit the data to the database
db.session.commit()

# Close the app context
app.app_context().pop()

print("Data seeded successfully!")
