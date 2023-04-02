from project.animal import Animal
from project.cat import Cat
from project.kitten import Kitten
from project.tomcat import Tomcat
from project.dog import Dog


# ###################################################
# Test_Code_1:
dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)
# ---------------------------------------------------
# Output_1:
# Woof!
# This is Rocky. Rocky is a 3 year old Male Dog
# Hiss
# This is Tom. Tom is a 6 year old Male Tomcat
# ###################################################
# Test_Code_2:
kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)
# ---------------------------------------------------
# Output_2:
# Meow
# This is Kiki. Kiki is a 1 year old Female Kitten
# Meow meow!
# This is Johnny. Johnny is a 7 year old Male Cat
# ###################################################
