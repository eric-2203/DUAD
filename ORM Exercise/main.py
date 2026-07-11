from database import Session, Base, engine
from usersrepository import UserRepository
from addressesrepository import AddressRepository
from carsrepository import CarRepository

Base.metadata.create_all(engine)

session = Session()

users_repo = UserRepository(session)
addresses_repo = AddressRepository(session)
cars_repo = CarRepository(session)

#new_user1 = users_repo.add_user("Eric Flores", "eric@gmail.com")
#new_user2 = users_repo.add_user("Daniela Campos", "dani@gmail.com")
#new_user3 = users_repo.add_user("Olga Cole", "olga@gmail.com")
#del_user = users_repo.delete_user(3)

#email_update = users_repo.update_user(1, "Eric Flores", "olga@gmail.com")

#new_address = addresses_repo.add_address("Limon, Guapiles, Quintas del Tropico, Casa B1", 2)

#new_car1 = cars_repo.add_car("Toyota", "Corolla")
#new_car2 = cars_repo.add_car("Nissan", "Kicks")
#new_car3 = cars_repo.add_car("Jeep", "Wrangler", 2)

#car_assignment = cars_repo.associate_car_to_user(2, 2)
#car_assignment_failure = cars_repo.associate_car_to_user(4, 1)

#del_user = users_repo.delete_user(2)


session.commit()
session.close()