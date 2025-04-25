import random


class Person:
    def __init__(self, name):
        self.name = name
    
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []


    def get_people(self, passenger):
        if len(self.passengers) < self.max_passengers: 
            self.passengers.append(passenger)
        else:
            print("The bus is full, please wait for the next one.")

    def remove_people(self, passenger):
        number = random.randint(0, self.max_passengers)
        self.passengers.pop(number)
        

person1 = Person("Eric")
person2 = Person("Dani")
person3 = Person("Alice")

my_bus = Bus(4)
my_bus.get_people(person1)
my_bus.get_people(person2)
my_bus.get_people(person3)


print(my_bus.passengers)