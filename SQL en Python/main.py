import psycopg2.extras
from data_base import PgManager
from UsersRepository import UserRepository
from CarsRepostitory import CarRepository
from RentalsRepository import RentalRepository
from flask import Flask, jsonify, request
from API import app, users_routes, cars_routes, rentals_routes

app = Flask(__name__)

db_manager = PgManager(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

users_repo = UserRepository(db_manager)
cars_repo = CarRepository(db_manager)
rentals_repo = RentalRepository(db_manager)


users_routes(app, users_repo)
cars_routes(app, cars_repo)
rentals_routes(app, rentals_repo)

if __name__ == '__main__':
    app.run(host="localhost", debug=True)