from data_base import PgManager
from datetime import datetime, date

class UserRepository():
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record["id"],
            "full_name": user_record["full_name"],
            "email": user_record["email"],
            "username": user_record["username"],
            "birthdate": user_record["birthdate"],
            "account_status": user_record["account_status"],
            "password": user_record["password"],
        }
    
    def get_all_users(self):
        results = self.db_manager.execute_query(
            "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users;"
        )
        formatted_results = [self._format_user(result) for result in results]
        return formatted_results
    
    def get_user_by_id(self, _id):
        try: 
            user = self.db_manager.execute_query(
                "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users WHERE id = %s;", (_id,)
                )
            
            formatted_result = self._format_user(user[0])
            return formatted_result
        except Exception as error:
            return {"error": str(error)}
        
    def get_user_by_email(self, _email):
        try: 
            if "@" not in _email:
                return {"error": "Format in email is incorrect. It must contain "@""}
            users = self.db_manager.execute_query(
                "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users WHERE LOWER(email) = LOWER(%s);", (_email,)
                )
            
            return [self._format_user(user) for user in users]
        except Exception as error:
            return {"error": str(error)}
        
    def get_user_by_username(self, _username):
        try: 
            users = self.db_manager.execute_query(
                "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users WHERE LOWER(username) = LOWER(%s);", (_username,)
                )
            
            return [self._format_user(user) for user in users]
        except Exception as error:
            return {"error": str(error)}
        
    def get_user_by_birthdate(self, _birthdate):
        try: 
            users = self.db_manager.execute_query(
                "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users WHERE birthdate = %s;", (_birthdate,)
                )
            
            return [self._format_user(user) for user in users]
        except Exception as error:
            return {"error": str(error)}
        
    def get_user_by_account_status(self, _account_status):
        try: 
            users = self.db_manager.execute_query(
                "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users WHERE LOWER(account_status) = LOWER(%s);", (_account_status,)
                )
            
            return [self._format_user(user) for user in users]
        except Exception as error:
            return {"error": str(error)}
        
    def get_user_by_password(self, _password):
        try: 
            users = self.db_manager.execute_query(
                "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users WHERE password = %s;", (_password,)
                )
            
            return [self._format_user(user) for user in users]
        except Exception as error:
            return {"error": str(error)}
    
    def _validate_birthdate(self, data):
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return True
        except ValueError:
            return False
        
    def _check_age(self, birth_str):
        birth = datetime.strptime(birth_str, "%d/%m/%Y").date()
        today = date.today()

        age = today.year - birth.year
        
        if age < 18:
            return True
        else:
            return False

    
    def create_user(self, full_name, email, username, birthdate, account_status, password):
        valid_status = ["active", "inactive", "debtor"]
        account_status = account_status.strip().lower()
        try:
            if not full_name or full_name.strip() == "":
                return {"error": "Full name is missing for this user"}
            if not email or email.strip() == "" or "@" not in email:
                return {"error": "The email is missing or the value provided is invalid"}
            if not username or username.strip() == "" or len(username) < 3:
                return {"error": "The username entered is invalid or it is missing. Username must have more than 3 characters"}
            if not birthdate or birthdate.strip() == "" or not self._validate_birthdate(birthdate):
                return {"error": "Birthdate is missing or it has an invalid format. Valid format: DD/MM/YYYY"}
            if self._check_age(birthdate):
                return {"error": "This user is under 18 years old and cannot be entered in the database yet to rent a car"}
            if not account_status or account_status.strip() == "":
                return {"error": "Account status is missing for this user"}
            if account_status.lower() not in valid_status:
                return {"error": "The account status you entered is invalid. Enter a valid account status"}
            if not password or password.strip() == "":
                return {"error": "Password is missing for this user"}
            if len(password) < 8:
                return {"error": "Password must contain at least 8 characters"}
            
            check_email = self.db_manager.execute_query(
            "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users WHERE email = %s;", (email,)
            )
            for user in check_email:
                if user["email"] == email:
                    return {"error": "The email you are trying to use already exists in the database. Please use a new email address"}

            check_username = self.db_manager.execute_query(
            "SELECT id, full_name, email, username, birthdate, account_status, password FROM lyfter_car_rental.users WHERE username = %s;", (username,)
            )
            for name in check_username:
                    if name["username"] == username:
                        return {"error": "The username you are trying to use already exists in the database. Please create a new username"}
            
            new_user = self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (full_name, email, username, birthdate, account_status, password) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id, full_name, email, username, birthdate, account_status, password;",
                (full_name, email, username, birthdate, account_status, password),
            )

            if new_user:
                return {
                    "id": new_user[0]["id"],
                    "full_name": new_user[0]["full_name"],
                    "email": new_user[0]["email"],
                    "username": new_user[0]["username"],
                    "birthdate": new_user[0]["birthdate"],
                    "account_status": new_user[0]["account_status"],
                    "password": new_user[0]["password"]
                }
            else:
                return {"error": "There was an error inserting the user information"}
        except Exception as error:
            return {"error": str(error)}
        
    def update_user(self, _id, account_status):
        valid_status = ["active", "inactive", "debtor"]
        account_status = account_status.strip().lower()
        try:
            if not account_status or account_status.strip() == "":
                return {"error": "Account status is missing to update user information"}
            if account_status.lower() not in valid_status:
                return {"error": "The account status you entered is invalid. Enter a valid account status"}
            
            result = self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s RETURNING id, account_status;",
                (account_status, _id)
            )

            if result:
                return {
                    "id": result[0]["id"],
                    "account_status": result[0]["account_status"],
                    "message": "User updated successfully"
                }
            else:
                return {"error": "There was an error updating user"}

        except Exception as error:
            return {"error": str(error)}
        
    def remove_user(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.users WHERE id = %s RETURNING id", (_id,)
            )
            print("User deleted successfully")
            return {"message": "User eliminated successfully"}
        except Exception as error:
            return {"error": str(error)}