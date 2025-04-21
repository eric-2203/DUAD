class Circle:
    print("We will calculate the circle area.")
    radius = int(input("Input the circle radius: "))

    def get_area(self, radius):
        self.area = (radius ** 2) * 3.14
        print(f"The circle area is: {self.area}")

result = Circle()
result.get_area(Circle.radius)