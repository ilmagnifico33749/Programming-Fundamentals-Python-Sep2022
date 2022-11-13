
class Person:

    def __init__(self,name):
        self.name = name

    def say_hello(self):
        print(f"Hello {self.name}")
    def say_goodbye(self):
        print(f"Goodbye {self.name}")
    def say_welcome(self):
        print(f"Welcome {self.name}")

ivan = Person("Ivan")
ivan.say_hello()

print(ivan.say_welcome())


