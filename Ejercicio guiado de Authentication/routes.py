from flask import jsonify, request, Response
from functools import wraps
from decimal import Decimal


def requires_authentication(jwt_manager):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if token is None:
                return jsonify(error="Authorization token is missing"), 401

            token = token.replace("Bearer ", "")
            decoded = jwt_manager.decode(token)
            if decoded is None:
                return jsonify(error="Invalid authorization token"), 401

            return function(*args, decoded=decoded, **kwargs)
        
        return wrapper
    
    return decorator


def requires_role(role, jwt_manager):
    def decorator(function):
        @wraps(function)
        @requires_authentication(jwt_manager)
        def wrapper(decoded, *args, **kwargs):

            user_role = decoded["role"]

            if user_role == role:
                return function(*args, **kwargs)

            
            return jsonify(error="User is not allowed to perform this action"), 403
        
        return wrapper
    
    return decorator


def authentication_routes(app, users_repo, jwt_manager):
    @app.route("/register", methods=['POST'])
    def register_user():
        try:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")

            if not username:
                return jsonify(error="Username is missing"), 400

            if not password:
                return jsonify(error="Password is missing"), 400
            result = users_repo.add_user(username, password)

            user_dict = result.to_dict()

        except ValueError as error:
            return jsonify(error=str(error)), 400
        return jsonify(user_dict), 201

    @app.route("/login", methods=['POST'])
    def login():
        try:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")

            if not username:
                return jsonify(error="Username is missing"), 400

            if not password:
                return jsonify(error="Password is missing"), 400

            result = users_repo.check_credentials(username, password)

            if result is None:
                return jsonify(error="Invalid credentials"), 401

            payload = {
                "id": result.id,
                "role": result.role
            }

            token = jwt_manager.encode(payload)

        except ValueError as error:
            return jsonify(error=str(error)), 400
        return jsonify(token=token), 200

    @app.route('/me', methods=['GET'])
    @requires_authentication(jwt_manager)
    def me(decoded):
        try:
            user_id = decoded["id"]

            user = users_repo.get_user_by_id(user_id)
            if user is None:
                return jsonify(error="User does not exist"), 404

            return jsonify(id=user_id, username=user.username, role=user.role)

        except Exception as e:
            return Response(status=500)

    @app.route("/test-admin")
    @requires_role("admin", jwt_manager)
    def test_admin():
        return jsonify(message="You are an admin")


def fruits_routes(app, fruits_repo, jwt_manager):
    @app.route("/fruits", methods=['POST'])
    @requires_role("admin", jwt_manager)
    def add_fruit():
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")
        stock_quantity = data.get("stock_quantity")

        if not name:
            return jsonify(error="Fruit name is missing"), 400

        name = name.strip().lower()

        if price is None:
            return jsonify(error="Price is missing"), 400

        if stock_quantity is None:
            return jsonify(error="Stock quantity is missing"), 400

        try:
            price = Decimal(price)
            stock_quantity = int(stock_quantity)

            if price <= 0:
                return jsonify(error="Price should be greater than zero"), 400

            if stock_quantity < 0:
                return jsonify(error="Stock quantity cannot be negative"), 400
            
            result = fruits_repo.add_fruit(name, price, stock_quantity)
        except ValueError as error:
            return jsonify(error=str(error)), 400

        return jsonify(result.to_dict()), 201

    @app.route("/fruits", methods=['GET'])
    @requires_role("admin", jwt_manager)
    def get_fruits():
        fruit_name = request.args.get("name")

        if fruit_name:
            fruit_name = fruit_name.strip().lower()
            try:
                fruit_result = fruits_repo.get_fruit_by_name(fruit_name)
                if fruit_result is None:
                    return jsonify(error="Fruit does not exist"), 404
                return jsonify(fruit_result.to_dict()), 200
            except ValueError as error:
                return jsonify(error=str(error)), 400

        fruits = fruits_repo.get_all_fruits()

        all_fruits = []
        for fruit in fruits:
            all_fruits.append(fruit.to_dict())
        return jsonify(all_fruits), 200

    @app.route("/fruits/<id>", methods=['GET'])
    @requires_role("admin", jwt_manager)
    def get_fruit_by_id(id):
        try: 
            fruit_id = int(id)

        except ValueError:
            return jsonify(error="Invalid fruit ID"), 400

        
        result = fruits_repo.get_fruit_by_id(fruit_id)

        if result is None:
            return jsonify(error="Fruit does not exist"), 404
            
        return jsonify(result.to_dict()), 200


    @app.route("/fruits/<id>", methods=['DELETE'])
    @requires_role("admin", jwt_manager)
    def delete_fruit(id):
        try: 
            fruit_id = int(id)

        except ValueError:
            return jsonify(error="Invalid fruit ID"), 400

        try:
            result = fruits_repo.delete_fruit(fruit_id)

        except ValueError as error:
            return jsonify(error=str(error)), 404
            
        return jsonify(result.to_dict()), 200

    @app.route("/fruits/<id>", methods=['PUT'])
    @requires_role("admin", jwt_manager)
    def update_fruit(id):
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")

        if not name:
            return jsonify(error="Fruit name is missing"), 400

        name = name.strip().lower()

        if price is None:
            return jsonify(error="Price is missing"), 400

        if price <= 0:
            return jsonify(error="Price should be greater than zero"), 400

        try: 
            fruit_id = int(id)

        except ValueError:
            return jsonify(error="Invalid fruit ID"), 400

        try:
            result = fruits_repo.update_fruit(fruit_id, name, price)

        except ValueError as error:
            return jsonify(error=str(error)), 404
        
        return jsonify(result.to_dict()), 200


    @app.route("/fruits/<id>/stock", methods=['POST'])
    @requires_role("admin", jwt_manager)
    def add_stock(id):
        data = request.get_json()
        quantity = data.get("quantity")

        if quantity is None:
            return jsonify(error="Quantity is missing"), 400
        
        try:
            quantity = int(quantity)

            if quantity <= 0:
                return jsonify(error="Quantity must be greater than zero"), 400

            fruit_id = int(id)
            result = fruits_repo.add_stock(fruit_id, quantity)

        except ValueError as error:
            return jsonify(error=str(error)), 400
        
        return jsonify(result.to_dict()), 200


def purchase_routes(app, invoices_repo, jwt_manager):
    @app.route("/purchase", methods=['POST'])
    @requires_authentication(jwt_manager)
    def make_purchase(decoded):

        user_id = decoded["id"]

        data = request.get_json()
        items = data.get("items")

        if items is None:
            return jsonify(error="No items were provided"), 400

        if not isinstance(items, list):
            return jsonify(error="Items should be in list format"), 400

        if not items:
            return jsonify(error="List of items is empty"), 400

        for item in items:
            if not isinstance(item, dict):
                return jsonify(error="Each item should be a dictionary"), 400
            
            fruit_id = item.get("fruit_id")
            quantity = item.get("quantity")

            if fruit_id is None:
                return jsonify(error="Item is missing the ID"), 400

            if quantity is None:
                return jsonify(error="Quantity is missing for this fruit"), 400

            try:
                fruit_id = int(fruit_id)
                quantity = int(quantity)
                item["fruit_id"] = fruit_id
                item["quantity"] = quantity
                if fruit_id <= 0:
                    return jsonify(error="Fruit ID cannot be zero or a negative number"), 400
                
                if quantity <= 0:
                    return jsonify(error="Quantity must be greater than zero"), 400

            except ValueError as error:
                return jsonify(error=str(error)), 400

        try: 
            invoice = invoices_repo.create_invoice(user_id, items)
        except ValueError as error:
            return jsonify(error=str(error)), 400

        return jsonify(invoice.to_dict()), 201


def invoices_routes(app, invoices_repo, jwt_manager):
    @app.route("/invoices", methods=['GET'])
    @requires_authentication(jwt_manager)
    def get_invoices(decoded):

        user_id = decoded["id"]
        user_role = decoded["role"]

        if user_role == "admin":
            invoices = invoices_repo.get_all_invoices()
            all_invoices = []

            for invoice in invoices:
                invoice_data = invoice.to_dict()

                details = invoice.invoice_details

                invoice_data["details"] = []

                for detail in details:
                    invoice_data["details"].append(detail.to_dict())

                all_invoices.append(invoice_data)

            return jsonify(all_invoices), 200

        elif user_role == "user":
            user_invoices = invoices_repo.get_invoice_by_user(user_id)
            all_user_invoices =[]

            for invoice in user_invoices:
                invoice_data = invoice.to_dict()

                details = invoice.invoice_details

                invoice_data["details"] = []

                for detail in details:
                    invoice_data["details"].append(detail.to_dict())

                all_user_invoices.append(invoice_data)

            return jsonify(all_user_invoices), 200

        else:
            return jsonify(error="User role is not allowed"), 403

    @app.route("/invoices/user/<user_id>", methods=['GET'])
    @requires_role("admin", jwt_manager)
    def get_invoice_by_user_id(user_id):
        try: 
            user_id = int(user_id)

        except ValueError:
            return jsonify(error="Invalid user ID"), 400

        result = invoices_repo.get_invoice_by_user(user_id)

        all_invoices = []

        for invoice in result:
            invoice_data = invoice.to_dict()

            details = invoice.invoice_details

            invoice_data["details"] = []

            for detail in details:
                invoice_data["details"].append(detail.to_dict())

            all_invoices.append(invoice_data)

        return jsonify(all_invoices), 200