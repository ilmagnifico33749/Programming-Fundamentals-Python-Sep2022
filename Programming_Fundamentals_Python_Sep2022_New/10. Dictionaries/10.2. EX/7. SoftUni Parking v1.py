register_my_dict = {}

number_of_commands = int(input())
for num_comms in range(number_of_commands):
    command = input()
    command_details = command.split(" ")
    command_order = command_details[0]
    username = command_details[1]

    if command_order == "register":
        licence_plate = command_details[2]
        if username not in register_my_dict.keys():
            register_my_dict[username] = {}
            register_my_dict[username]["licence_plate"] = licence_plate
            register_my_dict[username]["status"] = "registered"
            print(f"{username} registered {register_my_dict[username]['licence_plate']} successfully")
        else:
            print(f'ERROR: already registered with plate number {register_my_dict[username]["licence_plate"]}')
    elif command_order == "unregister":
        if username not in register_my_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            register_my_dict[username]["status"] = "unregistered"
            print(f"{username} unregistered successfully")

for user in register_my_dict.keys():
    if register_my_dict[user]["status"] == "registered":
        print(f"{user} => {register_my_dict[user]['licence_plate']}")

# -------------------------------#
# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy
# -------------------------------#
# 4
# register Jony AA4132BB
# register Jony AA4132BB
# register Linda AA9999BB
# unregister Jony
# -------------------------------#
# 6
# register Jacob MM1111XX
# register Anthony AB1111XX
# unregister Jacob
# register Joshua DD1111XX
# unregister Lily
# register Samantha AA9999BB
# -------------------------------#
