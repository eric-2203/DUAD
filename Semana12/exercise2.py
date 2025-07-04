import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    

    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_perimeter(self):
        perimeter = 2 * self.radius * math.pi
        print(f"Circle perimeter is: {perimeter}")

    def calculate_area(self):
        area = (self.radius ** 2) * math.pi
        print(f"Circle are is: {area}")

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def calculate_perimeter(self):
        perimeter = self.side * 4
        print(f"Square perimeter is: {perimeter}")

    def calculate_area(self):
        area = self.side * self.side
        print(f"Square area is: {area}")


class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_perimeter(self):
        perimeter = 2* (self.base + self.height)
        print(f"Rectangle perimeter is: {perimeter}")

    def calculate_area(self):
        area = self.base * self.height
        print(f"Rectangle area is: {area}")

my_circle = Circle(5)
my_circle.calculate_perimeter()
my_circle.calculate_area()

my_square = Square(5)
my_square.calculate_perimeter()
my_square.calculate_area()

my_rectangle = Rectangle(5, 4)
my_rectangle.calculate_perimeter()
my_rectangle.calculate_area()