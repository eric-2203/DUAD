from datetime import date

class User:
    date_of_birth = date
        
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return(today.year - self.date_of_birth.year)
    
def check_age(func):
    def wrapper(user, *args):
        if user.age < 18:
            raise ValueError(
                "This user is under 18 and it is not allowed."
            )
        func(user, *args)
        
    return wrapper

eric = User(date(1994, 3, 22))


@check_age
def buy_alcohol(user, product):

    print(f"Product {product} was bought successfully.")

buy_alcohol(eric, "Vodka")