from models import User
from sqlalchemy import select

class UserRepository:

    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        result = self.session.execute(select(User))
        return result.scalars().all()
    
    def get_user_by_email(self, user_email):
        result = self.session.execute(select(User).where(User.email == user_email))
        return result.scalars().first()
    
    def add_user(self, name, email):
        existing_user = self.get_user_by_email(email)
        if existing_user:
            raise ValueError("The email you are trying to use already exists in the database")
        
        user = User(name=name, email=email)
        self.session.add(user)
        return user
    
    def get_user_by_id(self, user_id):
        result = self.session.get(User, user_id)
        return result
    

    def update_user(self, user_id, name, email):
        user = self.get_user_by_id(user_id)
        if user is  None:
            raise ValueError("The user you are trying to update does not exist in the database")
        
        user.name = name
        user.email = email

        return user
    
    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user is None:
            raise ValueError("The user you are trying to delete does not exist in the database")
        
        self.session.delete(user)

        return user