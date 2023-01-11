courses_dict = {}

user_input = input()

while ":" in user_input:
    user_input_details = user_input.split(":")
    student_name = user_input_details[0]
    student_id = int(user_input_details[1])
    course = user_input_details[2]

    if course not in courses_dict:
        courses_dict[course] = {}
        courses_dict[course][student_name] = student_id
    else:
        courses_dict[course][student_name] = student_id
    user_input = input()
else:
    for key, value in courses_dict.items():
        if key == " ".join(user_input.split("_")):
            for student_name, student_id in value.items():
                print(f"{student_name} - {student_id}")

# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals

# Alex:6:programming basics
# Maria:7:programming basics
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics
