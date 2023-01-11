name = str(input())
while name != "Welcome!":
    if name != "Voldemort":
        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        elif len(name) > 6:
            print(f"{name} goes to Hufflepuff.")
        name = str(input())
    else:
        print("You must not speak of that name!")
        break
else:
    print("Welcome to Hogwarts.")