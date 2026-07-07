from database import Session, Base, engine
from usersrepository import UserRepository
from addressesrepository import AddressRepository
from carsrepository import CarRepository

Base.metadata.create_all(engine)

session = Session()

users_repo = UserRepository(session)
addresses_repo = AddressRepository(session)
cars_repo = CarRepository(session)

session.commit()
session.close()