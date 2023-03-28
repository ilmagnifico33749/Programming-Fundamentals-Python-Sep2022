class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.height * self.width
        return area

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()


# ######################
# Test_Code_1:
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 == a2)
# print(a1 != a3)
# ----------------------
# Output_1:
# True
# True
# ######################
# Test_Code_2:
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 != a2)
# print(a1 >= a3)
# ----------------------
# Output_2:
# False
# False
# ######################
# Test_Code_3:
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 <= a2)
# print(a1 < a3)
# ----------------------
# Output_3:
# True
# True
# ######################

