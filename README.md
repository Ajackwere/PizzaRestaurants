# PizzaRestaurants

## By Austine Jack Were

## Description

This is a Pizza Restaurant domain project. The backend is built using flask, database is postgresql hosted in render, and frontend side is built using react. The Models are described as follows:

### Models

- A `Restaurant` has many `Pizza`s through `RestaurantPizza`
- A `Pizza` has many `Restaurant`s through `RestaurantPizza`
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`

### Validations

The RestraurantPizza model has the following validation:

- must have a `price` between 1 and 30

## Project Setup

Follow these steps to setup the project in your local machine:

1. Clone the project repo into your local machine.
2. Run pipenv install & pipenv shell to install the pip dependencies and enter the virtual environment.
3. Run npm install inside the client directory to install the react dependencies.
4. Run flask run to start the backend server.
5. Run npm start to view the frontend side on your browser.

## License

This project is covered by MIT license.

## Support

For any help, reach out to me through my github page: @Ajackwere
