class Person:
    specie = "human"

    def __init__(self, name = "Template", person_id="000000000"):
        self.name = name
        self.__person_id = person_id

    def get_info(self):
        return f"Personal Info: name: {self.name}, id: {self.__person_id}"


class Child(Person):
    def __init__(self, name, child_id):
        self.child_name = name
        self.__child_id = child_id
        super().__init__(self.child_name, self.__child_id)


parent = Person()
print(f"parent.specie: {parent.specie}")
print(f"parent.name: {parent.name}")
print(f"parent.id: {parent._Person__person_id}")
print(f"parent.get_info(): {parent.get_info()}")

print(f"{50*'-'}")

child = Child("Michael Jr.", 133456789)
print(f"child.specie: {child.specie}")
print(f"child.child_name: {child.child_name}")
# print(f"child.child_id: {child._Child__child_id}")
# print(f"child.id: {child._Person__person_id}")
print(f"child.get_info(): {child.get_info()}")
print(child._Person__person_id)



