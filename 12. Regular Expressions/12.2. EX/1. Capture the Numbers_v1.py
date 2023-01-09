import re

sequence = input()
regex = "[]([0-9{+}])"
list_filtered = []

while sequence != "":
    filtered = re.findall(regex, sequence)
    print(filtered)
    list_filtered.append(''.join(filtered))
    sequence = input()

else:
    print(f"{list_filtered}")



# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45
