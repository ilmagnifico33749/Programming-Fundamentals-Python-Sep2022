bakery = {}
user_input = input().split(" ")

for thing in range(0, len(user_input), 2):
    bakery[user_input[thing]] = int(user_input[thing + 1])
print(bakery)

# bread 10 butter 4 sugar 9 jam 12
# eggs 3 sugar 7 salt 1 butter 3