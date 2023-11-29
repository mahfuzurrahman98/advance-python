from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

# Creating instances of concrete classes
circle = Circle(5)
square = Square(4)

# Using the common interface (area and perimeter methods) for different shapes
print("Circle Area:", circle.area())  # Output: Circle Area: 78.5
print("Circle Perimeter:", circle.perimeter())  # Output: Circle Perimeter: 31.400000000000002
print("Square Area:", square.area())  # Output: Square Area: 16
print("Square Perimeter:", square.perimeter())  # Output: Square Perimeter: 16
