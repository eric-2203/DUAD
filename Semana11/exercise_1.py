import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
        


    def get_area(self):
        area = (self.radius ** 2) * math.pi
        return area

my_circle = Circle(21)
my_circle.get_area()
