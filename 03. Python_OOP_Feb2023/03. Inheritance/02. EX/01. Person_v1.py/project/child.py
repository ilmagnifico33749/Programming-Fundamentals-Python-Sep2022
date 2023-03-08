from project.person import Person
# from person import Person

class Child(Person):
    pass


# ############################################
# Test_Code_1:
person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)
# --------------------------------------------
# Output_1:
# Peter
# 25
# Person
# ############################################
