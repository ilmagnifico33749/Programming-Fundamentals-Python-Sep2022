# from animal import Animal
# from reptile import Reptile
# from lizard import Lizard
# from snake import Snake
# from mammal import Mammal
# from gorilla import Gorilla
# from bear import Bear

from project.animal import Animal
from project.reptile import Reptile
from project.lizard import Lizard
from project.snake import Snake
from project.mammal import Mammal
from project.gorilla import Gorilla
from project.bear import Bear


# #############################################
# Test_Code_1:
mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
# ---------------------------------------------
# Output_1:
# Animal
# Stella
# Reptile
# John
# #############################################

