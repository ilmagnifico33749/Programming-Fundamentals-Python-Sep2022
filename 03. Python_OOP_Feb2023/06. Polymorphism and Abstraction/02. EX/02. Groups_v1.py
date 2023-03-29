class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: Person):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_group_name = self.name + " " + other.name
        new_group_people_list = self.people + other.people
        return Group(new_group_name, new_group_people_list)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([str(member) for member in self.people])}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"

# ########################################################
# Test_Code_1:
p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
# -------------------------------------------------------
# Output_1:
# 3
#
# Group Special with members Elon Musk, Warren Musk
#
# Person 0: Aliko Dangote
#
# Person 0: Aliko Dangote
# Person 1: Bill Gates
# Person 2: Warren Buffet
# Person 3: Elon Musk Person
# 4: Warren Musk
# ########################################################

