command = ""
coffees_needed = 0
while command != "END":
    command = input()
    if command.lower() == "coding" or command.lower() == "dog" \
        or command.lower() == "cat" or command.lower() == "movie":
        event = str(command)
        if event.isupper() is True:
            coffees_needed += 2
            print(coffees_needed)
        elif event.islower() is True:
            coffees_needed += 1
            print(coffees_needed)
    else:
        pass

if coffees_needed <= 5:
    print(f"{coffees_needed}")
else:
    print(f"You need extra sleep")








