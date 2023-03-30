# class Shape:
#     # def calculate_area(self):
#     #     return None
#     pass

class Square:
    def __init__(self, side_length: int):
        self.side_length = side_length
    def calculate_area(self):
        return self.side_length * 2


class Triangle:
    def __init__(self, base_length, height):
        self.base_length = base_length
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base_length * self.height


shapes = [Square(5), Triangle(10, 2)]
for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.calculate_area()}")

