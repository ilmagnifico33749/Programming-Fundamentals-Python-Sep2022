
class Parent:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return f"Hi! I am {self.name}"

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

parent = Parent("Michael")
child = Child
print()

