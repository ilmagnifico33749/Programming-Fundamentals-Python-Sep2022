from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        # raise NotImplementedError("Subclass must implement")
        pass

    @abstractmethod
    def calculate_perimeter(self):
        # raise NotImplementedError("Subclass must implement")
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        area = pi * (self.__radius ** 2)
        return area

    def calculate_perimeter(self):
        perimeter = 2 * pi * self.__radius
        return perimeter


class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_area(self):
        area = self.__length * self.__width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        return perimeter

# #######################################
# Test_Code_1:
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
# ---------------------------------------
# Output_1:
# 78.53981633974483
# 31.41592653589793
# #######################################
# Test_Code_2:
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
# ---------------------------------------
# Output_2:
# 200
# 60
# #######################################
