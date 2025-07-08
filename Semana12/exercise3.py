class Flyer():
    def __init__(self, animal):
        self.animal = animal
        pass

    def fly(self):
        print(f"This {self.animal} can fly.")

class Swimmer():
    def __init__(self, animal):
        self.animal = animal
        
    def swim(self):
        print(f"This {self.animal} can swim.")

class Walker():
    def __init__(self, animal):
        self.animal = animal
    def walk(self): 
        print(f"This {self.animal} can walk.")

class Penguin(Walker):
    pass

class Eagle(Flyer, Walker):
    pass

class Dolphin(Swimmer):
    pass

class Frog(Walker, Swimmer, Flyer):
    pass

my_penguin = Penguin("Penguin")
my_penguin.walk()

my_eagle = Eagle("Eagle")
my_eagle.fly()
my_eagle.walk()

my_flying_frog = Frog("Frog")
my_flying_frog.walk()
my_flying_frog.fly()
my_flying_frog.swim()

