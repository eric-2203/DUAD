from models import User
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash

class UserRepository:

    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        result = self.session.execute(select(User))
        return result.scalars().all()
    
    def get_user_by_username(self, username):
        result = self.session.execute(select(User).where(User.username == username))
        return result.scalars().first()
    
    def add_user(self, username, password, role="user"):
        existing_user = self.get_user_by_username(username)
        if existing_user:
            raise ValueError("Username already exists")

        hashed_password = generate_password_hash(password)

        user = User(username=username, password=hashed_password, role=role)
        self.session.add(user)
        self.session.commit()
        return user
    
    def get_user_by_id(self, user_id):
        result = self.session.get(User, user_id)
        return result

    def check_credentials(self, username, password):
        user = self.get_user_by_username(username)

        if user:
            saved_password = user.password
            comparison = check_password_hash(saved_password, password)

            if comparison:
                return user

            else:
                return None

        else:
            return None



    def update_user(self, user_id, username, password):
        existing_user = self.get_user_by_username(username)
        if existing_user:
            raise ValueError("Username already exists")
        user = self.get_user_by_id(user_id)
        if user is  None:
            raise ValueError("User does not exist in the database")
        
        user.username = username
        user.password = password
        self.session.commit()

        return user
    
    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user is None:
            raise ValueError("The user you are trying to delete does not exist in the database")
        
        self.session.delete(user)
        self.session.commit()

        return user