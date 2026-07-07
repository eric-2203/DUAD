from models import Car, User
from sqlalchemy import select

class CarRepository:
    def __init__(self, session):
        self.session = session

    def get_all_cars(self):
        result = self.session.execute(select(Car))
        return result.scalars().all()
    
    def add_car(self, brand, model, user_id: int | None = None):

        if user_id is not None:
            user = self.session.get(User, user_id)
            
            if not user:
                raise ValueError("This user does not exist in the database")
            
        
        new_car = Car(brand=brand, model=model, user_id=user_id)

        self.session.add(new_car)
        return new_car
    
    def get_car_by_id(self, car_id):
        result = self.session.get(Car, car_id)
        return result
    

    def update_car(self, car_id, brand, model):
        existing_car = self.get_car_by_id(car_id)
        if existing_car is  None:
            raise ValueError("The car you are trying to update does not exist in the database")
        
        existing_car.brand = brand
        existing_car.model = model

        return existing_car
    
    def delete_car(self, car_id):
        existing_car = self.get_car_by_id(car_id)
        if existing_car is None:
            raise ValueError("The car you are trying to delete does not exist in the database")
        
        self.session.delete(existing_car)

        return existing_car
    
    def associate_car_to_user(self, car_id, user_id):
        existing_car = self.get_car_by_id(car_id)
        if existing_car is None:
            raise ValueError("The car you are trying to update does not exist in the database")

        user = self.session.get(User, user_id)
        if user is None:
            raise ValueError("This user does not exist in the database")
        
        if existing_car.user_id is not None:
            raise  ValueError("This car is already associated to another user")
        
        existing_car.user_id = user_id

        return existing_car
        
