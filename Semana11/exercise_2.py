import random

class Bus:
    passengers = []

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers


    def get_people(self, passenger):
        if len(self.passengers) < self.max_passengers: 
            self.passengers.append(passenger)
        else:
            print(f"{passenger} the bus is full")

    def remove_people(self, passenger):
        number = random.randint(0, self.max_passengers)
        self.passengers.pop(number)
        

my_bus = Bus(6)
my_bus.get_people("Raul")
my_bus.get_people("Claudia")
my_bus.get_people("Luis")
my_bus.get_people("Dani")
my_bus.get_people("Eric")
my_bus.get_people("Juan")
my_bus.remove_people("passenger")
my_bus.get_people("Fernando")
my_bus.get_people("Pedro")

print(f"People on the bus: {my_bus.passengers}")