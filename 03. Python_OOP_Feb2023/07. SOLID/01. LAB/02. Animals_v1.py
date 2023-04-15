# ####################################################
# # Code_To_Correct_1:
# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'project':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('project'), Animal('dog')]
# animal_sound(animals)
#
# ## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
# ## при добавяне на нови животни
# # animals = [Animal('project'), Animal('dog'), Animal('chicken')]
# ####################################################
# Corrected_Code_1:

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def animal_sound():
        pass


class Cat(Animal):
    @staticmethod
    def animal_sound():
        return "Meow!"


class Dog(Animal):
    @staticmethod
    def animal_sound():
        return "Woof!"


class Duck(Animal):
    @staticmethod
    def animal_sound():
        return "Quack!"

####################################################
# Test_1:
animal = Animal
cat = Cat
dog = Dog
duck = Duck
print(animal.animal_sound())
print(cat.animal_sound())
print(dog.animal_sound())
print(duck.animal_sound())
####################################################
