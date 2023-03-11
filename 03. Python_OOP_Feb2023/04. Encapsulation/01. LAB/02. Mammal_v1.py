class Mammal:
    __kingdom = "animals"

    def __init__(self, name, animal_type, sound):
        self.name = name
        self.type = animal_type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


# ##########################################
# Test_Code_1:
mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
# ------------------------------------------
# Output_1:
# Dog makes Bark
# animals
# Dog is of type Domestic
# ##########################################
