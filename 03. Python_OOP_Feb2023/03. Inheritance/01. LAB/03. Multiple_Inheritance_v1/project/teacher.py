from project.person import Person
from project.employee import Employee

# from person import Person
# from employee import Employee

class Teacher(Person, Employee):
    def __init__(self):
        pass

    def teach(self):
        return f"teaching..."