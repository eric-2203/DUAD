from flask import Flask, jsonify, request
from data_base import PgManager
from UsersRepository import UserRepository


app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Welcome to the Classics Car Rental API!</h1>"

def users_routes(app, users_repo):
    @app.route("/users", methods=['POST'])
    def register_user():
        data = request.get_json()
        result = users_repo.create_user(data["full_name"], data["email"], data["username"], data["birthdate"], data["account_status"], data["password"])
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result), 201
    
    @app.route("/users/<id>", methods=["DELETE"])
    def delete_user(id):
        result = users_repo.remove_user(id)
        if "error" in result:
            return jsonify(result), 404
        
        return jsonify(result), 200
    
    @app.route("/users", methods=['GET'])
    def get_users():
        user_id = request.args.get("id")
        user_email = request.args.get("email")
        user_username = request.args.get("username")
        user_birthdate = request.args.get("birthdate")
        user_account_status = request.args.get("account_status")
        user_password = request.args.get("password")
        if user_id:
            try:
                user_id = int(user_id)
                result = users_repo.get_user_by_id(user_id)
                if "error" in result:
                    return jsonify(result), 400
                return jsonify(result), 200
            except ValueError:
                return jsonify({"error": "ID must be an integer"}), 400
            
        if user_email:
            email_result = users_repo.get_user_by_email(user_email)
            return jsonify(email_result), 200
        
        if user_username:
            username_result = users_repo.get_user_by_username(user_username)
            return jsonify(username_result), 200
        
        if user_birthdate:
            birthdate_result = users_repo.get_user_by_birthdate(user_birthdate)
            return jsonify(birthdate_result), 200
        
        if user_account_status:
            account_status_result = users_repo.get_user_by_account_status(user_account_status)
            return jsonify(account_status_result), 200
        
        if user_password:
            password_result = users_repo.get_user_by_password(user_password)
            return jsonify(password_result), 200


        all_users = users_repo.get_all_users()
        return jsonify(all_users), 200
    
    @app.route("/users/<id>", methods=['PUT'])
    def update_user_status(id):
        data = request.get_json()
        result = users_repo.update_user(id, data["account_status"])
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result)
    
def cars_routes(app, cars_repo):
    @app.route("/cars", methods=['POST'])
    def register_car():
        data = request.get_json()
        result = cars_repo.create_car(data["brand"], data["model"], data["manufacture_year"], data["status"])
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result), 201
    
    @app.route("/cars", methods=['GET'])
    def get_cars():
        car_id = request.args.get("id")
        car_status = request.args.get("status")
        car_brand = request.args.get("brand")
        car_model = request.args.get("model")
        car_manufacture_year = request.args.get("manufacture_year")
        if car_id:
            try:
                car_id = int(car_id)
                result = cars_repo.get_car_by_id(car_id)
                if "error" in result:
                    return jsonify(result), 400
                return jsonify(result), 200
            except ValueError:
                return jsonify({"error": "ID must be an integer"}), 400
        
        if car_status:
            status_result = cars_repo.get_car_by_status(car_status)
            return jsonify(status_result), 200
        
        if car_brand:
            brand_result = cars_repo.get_car_by_brand(car_brand)
            return jsonify(brand_result), 200
        
        if car_model:
            model_result = cars_repo.get_car_by_model(car_model)
            return jsonify(model_result), 200
        
        if car_manufacture_year:
            manufacture_year_result = cars_repo.get_car_by_manufacture_year(car_manufacture_year)
            return jsonify(manufacture_year_result), 200


        cars = cars_repo.get_all_cars()
        return jsonify(cars), 200

    
    @app.route("/cars/<id>", methods=['GET'])
    def get_car_by_id(id):
        results = cars_repo.get_car_by_id(id)
        if "error" in results:
            return jsonify(results), 400
        return jsonify(results), 200
    
    @app.route("/cars/<id>", methods=['PUT'])
    def update_car_status(id):
        data = request.get_json()
        result = cars_repo.update_car(id, data["status"])
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result)

    
    
def rentals_routes(app, rentals_repo):
    @app.route("/rentals", methods=['GET'])
    def get_all_rentals():
        rental_id = request.args.get("id")
        user_id = request.args.get("user_id")
        car_id = request.args.get("car_id")
        rent_date = request.args.get("rent_date")
        rent_status = request.args.get("rent_status")
        if rental_id:
            try:
                rental_id = int(rental_id)
                result = rentals_repo.get_rental_by_id(rental_id)
                if "error" in result:
                    return jsonify(result), 400
                return jsonify(result), 200
            except ValueError:
                return jsonify({"error": "ID must be an integer"}), 400
            
        if user_id:
            try:
                user_id = int(user_id)
                result = rentals_repo.get_rental_by_user_id(user_id)
                if "error" in result:
                    return jsonify(result), 400
                return jsonify(result), 200
            except ValueError:
                return jsonify({"error": "User ID must be an integer"}), 400
            
        if car_id:
            try:
                car_id = int(car_id)
                result = rentals_repo.get_rental_by_car_id(car_id)
                if "error" in result:
                    return jsonify(result), 400
                return jsonify(result), 200
            except ValueError:
                return jsonify({"error": "Car ID must be an integer"}), 400
            
        if rent_date:
            rent_date_result = rentals_repo.get_rental_by_rent_date(rent_date)
            return jsonify(rent_date_result), 200
        
        if rent_status:
            rent_status_result = rentals_repo.get_rental_by_rent_status(rent_status)
            return jsonify(rent_status_result), 200


        all_rentals = rentals_repo.get_rentals()
        return jsonify(all_rentals), 200
    
    @app.route("/rentals", methods=['POST'])
    def register_rental():
        data = request.get_json()
        result = rentals_repo.create_rental(data["user_id"], data["car_id"])
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result), 201
    
    @app.route("/rentals/<car_id>", methods=['PUT'])
    def complete_rental(car_id):
        result = rentals_repo.car_return(car_id)
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result)
    
    @app.route("/rentals/<id>", methods=['PATCH'])
    def update_status(id):
        data = request.get_json()
        result = rentals_repo.update_rental_status(id, data["rent_status"])
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result)


if __name__ == '__main__':
    app.run(host="localhost", debug=True)