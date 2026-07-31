from models import Address, User
from sqlalchemy import select

class AddressRepository:
    def __init__(self, session):
        self.session = session

    def get_all_addresses(self):
        result = self.session.execute(select(Address))
        return result.scalars().all()
    

    def add_address(self, address, user_id):
        user = self.session.get(User, user_id)

        if user is None:
            raise ValueError("This user does not exist in the database")
        for data in user.addresses:
            if data.address == address:
                raise ValueError("You are trying to add a duplicated address for this user")

        new_address = Address(address=address, user_id=user_id)
        self.session.add(new_address)
        return new_address
    
    def get_address_by_id(self, address_id):
        result = self.session.get(Address, address_id)
        return result
    
    def update_address(self, address_id, address_txt):
        existing_address = self.get_address_by_id(address_id)
        if existing_address is  None:
            raise ValueError("The address you are trying to update does not exist in the database")
        
        existing_address.address = address_txt

        return existing_address
    
    def delete_address(self, address_id):
        existing_address = self.get_address_by_id(address_id)
        if existing_address is None:
            raise ValueError("The address you are trying to delete does not exist in the database")
        
        self.session.delete(existing_address)

        return existing_address