from data_base import PgManager

class RentalRepository():
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rentals(self, rental_record):
        return {
            "id": rental_record["id"],
            "user_id": rental_record["user_id"],
            "car_id": rental_record["car_id"],
            "rent_date": rental_record["rent_date"],
            "rent_status": rental_record["rent_status"],
        }
    
    def get_rentals(self):
        results = self.db_manager.execute_query(
            "SELECT id, user_id, car_id, rent_date, rent_status FROM lyfter_car_rental.rentals;"
        )
        formatted_results = [self._format_rentals(result) for result in results]
        return formatted_results
    
    def get_rental_by_id(self, _id):
        try: 
            rental = self.db_manager.execute_query(
                "SELECT id, user_id, car_id, rent_date, rent_status FROM lyfter_car_rental.rentals WHERE id = %s;", (_id,)
                )
            
            formatted_result = self._format_rentals(rental[0])
            return formatted_result
        except Exception as error:
            return {"error": str(error)}
        
    def get_rental_by_user_id(self, _user_id):
        try:
            rentals = self.db_manager.execute_query(
                "SELECT id, user_id, car_id, rent_date, rent_status FROM lyfter_car_rental.rentals WHERE user_id = %s;", (_user_id,)
                )
            
            return [self._format_rentals(rental) for rental in rentals]
        except Exception as error:
            return {"error": str(error)}
        
    def get_rental_by_car_id(self, _car_id):
        try:
            rentals = self.db_manager.execute_query(
                "SELECT id, user_id, car_id, rent_date, rent_status FROM lyfter_car_rental.rentals WHERE car_id = %s;", (_car_id,)
                )
            
            return [self._format_rentals(rental) for rental in rentals]
        except Exception as error:
            return {"error": str(error)}
        
    def get_rental_by_rent_date(self, _rent_date):
        try:
            rentals = self.db_manager.execute_query(
                "SELECT id, user_id, car_id, rent_date, rent_status FROM lyfter_car_rental.rentals WHERE rent_date = %s;", (_rent_date,)
                )
            
            return [self._format_rentals(rental) for rental in rentals]
        except Exception as error:
            return {"error": str(error)}
        
    def get_rental_by_rent_status(self, _rent_status):
        try:
            rentals = self.db_manager.execute_query(
                "SELECT id, user_id, car_id, rent_date, rent_status FROM lyfter_car_rental.rentals WHERE LOWER(rent_status) = LOWER(%s);", (_rent_status,)
                )
            
            return [self._format_rentals(rental) for rental in rentals]
        except Exception as error:
            return {"error": str(error)}

    
    def create_rental(self, user_id, car_id):
        try:
            if not user_id:
                return {"error": "User ID is missing for this rental"}
            if not car_id:
                return {"error": "Car ID is missing for this rental"}
            
            results = self.db_manager.execute_query(
            "SELECT id, user_id, car_id, rent_date, rent_status FROM lyfter_car_rental.rentals WHERE car_id = %s;", (car_id,)

            )
            for rental in results:
                if rental["rent_status"].lower() == "active" or rental["rent_status"].lower() == "reserved":
                    return {"error": "This car has an active rental"}
                
            car_results = self.db_manager.execute_query(
                "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars WHERE id = %s;", (car_id,)
            )
            for car in car_results:
                if car["status"].lower() != "available":
                    return {"error": "The car you are trying to rent is already rented or it is not available for rental"}
                    
                
            user_results = self.db_manager.execute_query(
                "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users WHERE id = %s;", (user_id,)
            )
            for user in user_results:
                if user["account_status"].lower() == "inactive":
                    return {"error": "This user is not able to rent a car as their account is currently inactive"}
                
            new_rental = self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.rentals (user_id, car_id) VALUES (%s, %s) RETURNING id, user_id, car_id, rent_date, rent_status;",
                (user_id, car_id),
            )
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = 'reserved' WHERE id = %s;",
                (car_id,)
            )

            if new_rental:
                return {
                    "id": new_rental[0]["id"],
                    "user_id": new_rental[0]["user_id"],
                    "car_id": new_rental[0]["car_id"],
                    "rent_date": new_rental[0]["rent_date"],
                    "rent_status": new_rental[0]["rent_status"]
                }
            else:
                return{"error": "There was an error inserting rental information to the database"}
            
        except Exception as error:
            return {"error": str(error)}
        
    def car_return(self, car_id):
        try:
            results = self.db_manager.execute_query(
            "SELECT id, car_id, rent_status FROM lyfter_car_rental.rentals WHERE car_id = %s;", (car_id,)

            )
            for rental in results:
                if rental["rent_status"].lower() == "active" or rental["rent_status"].lower() == "pending":
                    self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.rentals SET rent_status = 'ended' WHERE id = %s RETURNING id;",
                        (rental["id"],)
                    )

                    rent_update = self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'available' WHERE id = %s RETURNING id, status;",
                        (car_id,)
                    )
                    if rent_update:
                        return {"message": "Rental completed successfully"}
                    else:
                        return {"error": "There was an error updating the rental"}
                
            return {"error": "Car does not have an active rental or it does not exist"}
        except Exception as error:
            return {"error": str(error)}
        
    def update_rental_status(self, id, _rent_status):
        valid_status = ["pending", "active", "ended", "cancelled"]
        _rent_status = _rent_status.strip().lower()
        try:
            result = self.db_manager.execute_query(
            "SELECT id, car_id, rent_status FROM lyfter_car_rental.rentals WHERE id = %s;", (id,)
            )
            print(result)
            
    
            if result: 
                car_id = result[0]["car_id"]
                print(car_id)
                if not _rent_status or _rent_status.strip() == "":
                    return {"error": "Rent Status information is missing to update the rental."}
                if _rent_status not in valid_status:
                    return {"error": "The rent status you entered is invalid. Enter a valid rent status"}
                if _rent_status == "pending":
                    if result[0]["rent_status"].lower() == "pending":
                        return {"error": "Rental status is already pending"}
                    if result[0]["rent_status"].lower() == "active":
                        return {"error": "Rental status cannot be changed from active to pending"}
                    if result[0]["rent_status"].lower() == "cancelled":
                        return {"error": "Rental status cannot be changed from cancelled to pending"}
                    if result[0]["rent_status"].lower() == "ended":
                        return {"error": "Rental status cannot be changed from ended to pending"}
                    pending_status = self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.rentals SET rent_status = 'pending' WHERE id = %s RETURNING id, rent_status;",
                        (id,)
                    )
                    self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'reserved' WHERE id = %s RETURNING id, status;",
                        (car_id,)
                    )
                    return pending_status
                if _rent_status == "active":
                    if result[0]["rent_status"].lower() == "active":
                        return {"error": "Rental status is already active"}
                    if result[0]["rent_status"].lower() == "ended":
                        return {"error": "Rental status cannot be changed from ended to active"}
                    if result[0]["rent_status"].lower() == "cancelled":
                        return {"error": "Rental status cannot be changed from cancelled to active"}
                    active_status = self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.rentals SET rent_status = 'active' WHERE id = %s RETURNING id, rent_status;",
                        (id,)
                    )
                    self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'rented' WHERE id = %s RETURNING id, status;",
                        (car_id,)
                    )
                    return active_status
                
                if _rent_status == "cancelled":
                    if result[0]["rent_status"].lower() == "cancelled":
                        return {"error": "Rental status is already cancelled"}
                    if result[0]["rent_status"].lower() == "ended":
                        return {"error": "Rental status cannot be changed from ended to cancelled"}
                    if result[0]["rent_status"].lower() == "pending":
                        return {"error": "Rental status cannot be changed from pending to cancelled"}
                    if result[0]["rent_status"].lower() == "active":
                        return {"error": "Rental status cannot be changed from active to cancelled"}
                    cancelled_status = self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.rentals SET rent_status = 'cancelled' WHERE id = %s RETURNING id, rent_status;",
                        (id,)
                    )
                    self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'available' WHERE id = %s RETURNING id, status;",
                        (car_id,)
                    )
                    return cancelled_status
                
                if _rent_status == "ended":
                    if result[0]["rent_status"].lower() == "ended":
                        return {"error": "Rental status is already ended"}
                    if result[0]["rent_status"].lower() == "cancelled":
                        return {"error": "Rental status cannot be changed from cancelled to ended"}
                    ended_status = self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.rentals SET rent_status = 'ended' WHERE id = %s RETURNING id, rent_status;",
                        (id,)
                    )
                    self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'available' WHERE id = %s RETURNING id, status;",
                        (car_id,)
                    )
                    return ended_status

            else:
                return {"error": "A rental was not found with the information provided"}
        except Exception as error:
            return {"error": str(error)}


