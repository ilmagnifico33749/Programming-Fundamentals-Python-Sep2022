students = int(input())
my_dict_students = {}

for student in range(students):
    student, grade = tuple(input().split(" "))
    if student not in my_dict_students:
        my_dict_students[student] = [f"{float(grade):.2f}"]
    else:
        my_dict_students[student].append(f"{float(grade):.2f}")

for key, value in my_dict_students.items():
    average_grades = sum([float(x) for x in my_dict_students[key]])/len(list(my_dict_students[key]))
    print(f"{key} -> {' '.join(value)} (avg: {average_grades:.2f})")

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



