students = int(input())
my_dict_students = {}

for student in range(students):
    student, grade = tuple(input().split(" "))
    if student not in my_dict_students:
        my_dict_students[student] = [grade]
    else:
        my_dict_students[student].append(grade)

for key, value in my_dict_students.items():
    print(f"{key} -> {va}")


# #
# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
# ----
#
# #