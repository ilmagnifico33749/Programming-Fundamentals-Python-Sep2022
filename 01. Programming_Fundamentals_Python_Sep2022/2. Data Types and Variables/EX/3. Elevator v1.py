number_of_people = int(input())
capacity = int(input())
if number_of_people <= capacity:
    print(f"1")
else:
    courses = number_of_people % capacity
    if courses == 0:
        print(f"{int(number_of_people / capacity)}")
    else:
        courses = int(number_of_people/ capacity)
        print(f"{courses + 1}")
