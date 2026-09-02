from models import Fruit
from sqlalchemy import select

class FruitRepository():
    def __init__(self, session):
        self.session = session

    def get_all_fruits(self):
        result = self.session.execute(select(Fruit))
        return result.scalars().all()

    def get_fruit_by_name(self, fruit_name):
        result = self.session.execute(select(Fruit).where(Fruit.name == fruit_name))
        return result.scalars().first()

    def add_fruit(self, name, price, stock_quantity):
        existing_fruit = self.get_fruit_by_name(name)
        if existing_fruit:
            raise ValueError("This fruit already exists in the database. Instead, add the stock to it")

        fruit = Fruit(name=name, price=price, stock_quantity=stock_quantity)
        self.session.add(fruit)
        self.session.commit()
        return fruit

    def get_fruit_by_id(self, fruit_id):
        result = self.session.get(Fruit, fruit_id)
        return result

    def update_fruit(self, fruit_id, fruit_name, fruit_price):
        existing_fruit = self.get_fruit_by_id(fruit_id)
        if existing_fruit is None:
            raise ValueError("This fruit does not exist")
        
        fruit = self.get_fruit_by_name(fruit_name)
        if fruit is not None and fruit.id != fruit_id: 
            raise ValueError("This fruit already exists")
        
        existing_fruit.name = fruit_name
        existing_fruit.price = fruit_price
        self.session.commit()

        return existing_fruit

    def add_stock(self, fruit_id, quantity):
        existing_fruit = self.get_fruit_by_id(fruit_id)
        if existing_fruit is None:
            raise ValueError("This fruit does not exist")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        existing_fruit.stock_quantity = existing_fruit.stock_quantity + quantity
        self.session.commit()

        return existing_fruit

    def remove_stock(self, fruit_id, quantity):
        existing_fruit = self.get_fruit_by_id(fruit_id)
        if existing_fruit is None:
            raise ValueError("This fruit does not exist")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if existing_fruit.stock_quantity < quantity:
            raise ValueError("Current stock is less than the quantity you want to remove")

        existing_fruit.stock_quantity = existing_fruit.stock_quantity - quantity
        self.session.commit()

        return existing_fruit


    def delete_fruit(self, fruit_id):
        fruit = self.get_fruit_by_id(fruit_id)
        if fruit is None:
            raise ValueError("The fruit you are trying to delete does not exist in the database")
        
        self.session.delete(fruit)
        self.session.commit()

        return fruit