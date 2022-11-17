# ------------------------#
# Adam-0888080808
# 2
# Mery
# Adam
# ------------------------#
# Adam-+359888001122
# Ralf-666
# George-5559393
# Silvester-02/987665544
# 4
# Silvester
# silvester
# Rolf
# Ralf
# ------------------------#

command = input()
my_dict = {}

while command.isnumeric() == False:
    list_phone_no = command.split("-")
    my_dict[list_phone_no[0]] = list_phone_no[1]
    command = input()
else:
    times_to_call = int(command)
    for times in range(times_to_call):
        person_to_call = input()
        if person_to_call in my_dict.keys():
            print(f"{person_to_call} -> {my_dict[person_to_call]}")
        else:
            print(f"Contact {person_to_call} does not exist.")
