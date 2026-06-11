from data_base import PgManager
from datetime import datetime, date


class CarRepository():
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_cars(self, car_record):
        return {
            "id": car_record["id"],
            "brand": car_record["brand"],
            "model": car_record["model"],
            "manufacture_year": car_record["manufacture_year"],
            "status": car_record["status"],
        }
    
    def get_all_cars(self):
        results = self.db_manager.execute_query(
            "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars;"
        )
        formatted_results = [self._format_cars(result) for result in results]
        return formatted_results
    
    def get_car_by_id(self, _id):
        try: 
            car = self.db_manager.execute_query(
                "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars WHERE id = %s;", (_id,)
                )
            
            formatted_result = self._format_cars(car[0])
            return formatted_result
        except Exception as error:
            return {"error": str(error)}
        
    def get_car_by_status(self, _status):
        try:
            cars = self.db_manager.execute_query(
                "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars WHERE LOWER(status) = LOWER(%s);", (_status,)
                )
            
            return [self._format_cars(car) for car in cars]
        except Exception as error:
            return {"error": str(error)}
        
    def get_car_by_brand(self, _brand):
        try:
            cars = self.db_manager.execute_query(
                "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars WHERE LOWER(brand) = LOWER(%s);", (_brand,)
                )
            
            return [self._format_cars(car) for car in cars]
        except Exception as error:
            return {"error": str(error)}

    def get_car_by_model(self, _model):
        try:
            cars = self.db_manager.execute_query(
                "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars WHERE LOWER(model) = LOWER(%s);", (_model,)
                )
            
            return [self._format_cars(car) for car in cars]
        except Exception as error:
            return {"error": str(error)}
        
    def get_car_by_manufacture_year(self, _manufacture_year):
        try:
            cars = self.db_manager.execute_query(
                "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars WHERE manufacture_year = %s;", (_manufacture_year,)
                )
            
            return [self._format_cars(car) for car in cars]
        except Exception as error:
            return {"error": str(error)}
    
    def _validate_date(self, data):
        try:
            datetime.strptime(data, "%Y")
            return True
        except ValueError:
            return False
    

    def create_car(self, brand, model, manufacture_year, status):
        valid_status = ["available", "rented", "unavailable"]
        status = status.strip().lower()
        try:
            if not brand or brand.strip() == "":
                return {"error": "Brand name is missing for this car"}
            if not model or model.strip() == "":
                return {"error": "Model name is missing for this car"}
            if not manufacture_year:
                return {"error": "Manufacture year is missing for this car or you are using an invalid format. Valid format: YYYY"}
            if manufacture_year < 0 or manufacture_year > 2026 or manufacture_year < 1980:
                return {"error": "The value entered is not valid. For a car to be registered it must have been manufactured between 1980 and 2026"}
            if not status or status.strip() == "":
                return {"error": "Status is missing for this car"}
            if status not in valid_status:
                return {"error": "The status you are using is not valid. Please use a valid status"}
            
            new_car = self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, status) VALUES (%s, %s, %s, %s) RETURNING id, brand, model, manufacture_year, status;",
                (brand, model, manufacture_year, status),
            )

            if new_car:
                return {
                    "id": new_car[0]["id"],
                    "brand": new_car[0]["brand"],
                    "model": new_car[0]["model"],
                    "manufacture_year": new_car[0]["manufacture_year"],
                    "status": new_car[0]["status"]
                }
            else:
                return {"error": "There was an error inserting car information"}
        except Exception as error:
            return {"error": str(error)}
        
    def update_car(self, _id, _status):
        valid_status = ["available", "unavailable", "rented", "reserved"]
        _status = _status.strip().lower()
        try:
            result = self.db_manager.execute_query(
            "SELECT id, status FROM lyfter_car_rental.cars WHERE id = %s;", (_id,)
            )

            if not _status or _status.strip() == "":
                return {"error": "Status is missing to update car information"}
            if _status.lower() not in valid_status:
                return {"error": "The status you entered is invalid. Enter a valid status"}
            if _status == "available":
                if result[0]["status"].lower() == "available":
                    return {"error": "Car status is already available"}
                available_status = self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'available' WHERE id = %s RETURNING id, status;",
                        (_id,)
                    )
                return available_status
            
            if _status == "unavailable":
                if result[0]["status"].lower() == "unavailable":
                    return {"error": "Car status is already unavailable"}
                unavailable_status = self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'unavailable' WHERE id = %s RETURNING id, status;",
                        (_id,)
                    )
                return unavailable_status
            
            if _status == "rented":
                if result[0]["status"].lower() == "rented":
                    return {"error": "Car status is already rented"}
                rented_status = self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'rented' WHERE id = %s RETURNING id, status;",
                        (_id,)
                    )
                return rented_status
            
            if _status == "reserved":
                if result[0]["status"].lower() == "reserved":
                    return {"error": "Car status is already reserved"}
                reserved_status = self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'reserved' WHERE id = %s RETURNING id, status;",
                        (_id,)
                    )
                return reserved_status
            
            else:
                return {"error": "There was an error updating this car"}

        except Exception as error:
            return {"error": str(error)}
        
    def get_all_rented_cars(self):
        rented_cars = []
        results = self.db_manager.execute_query(
            "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars;"
        )
        for car in results:
            if car["status"].lower() == "rented":
                rented_cars.append(car)
                
        rented = [self._format_cars(result) for result in rented_cars]
        return rented
    
    def get_all_available_cars(self):
        available_cars = []
        results = self.db_manager.execute_query(
            "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars;"
        )
        for car in results:
            if car["status"].lower() == "available":
                available_cars.append(car)
                
        available = [self._format_cars(result) for result in available_cars]
        return available
    
    def remove_from_rental(self,_id):
        try:
            result = self.db_manager.execute_query(
            "SELECT id, status FROM lyfter_car_rental.cars WHERE id = %s;", (_id,)
            )
            for car in result:
                if car["status"] == "available":
                    self.db_manager.execute_query(
                        "UPDATE lyfter_car_rental.cars SET status = 'unavailable' WHERE id = %s;",
                        (_id,)
                    )
                    print("Car removed from rental options")
                    return True
                else:
                    print("This car is no longer available or it does not exist.")
                    return False

        except Exception as error:
            print("Error updating car from the Database: ", error)
            return False