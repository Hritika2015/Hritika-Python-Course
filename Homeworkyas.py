import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

radius_input = float(input("Enter the radius of the circle: "))
print("I am angry joking!!")

my_circle = Circle(radius_input)

print("Area of circle: ", my_circle.area())
print("Perimeter of the circle: ", my_circle.perimeter())
        