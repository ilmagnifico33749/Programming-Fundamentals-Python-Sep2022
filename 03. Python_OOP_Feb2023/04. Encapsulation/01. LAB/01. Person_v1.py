class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# ##############################
# Test_Code_1:
person = Person("George", 32)
print(person.get_name())
print(person.get_age())
# ------------------------------
# Output_1:
# George
# 32
# ##############################
