bakery = {}
user_input = input().split(" ")

for thing in range(0, len(user_input), 2):
    key, value = user_input[thing], user_input[thing + 1]
    bakery[key] = int(value)
print(bakery)

# bread 10 butter 4 sugar 9 jam 12
# eggs 3 sugar 7 salt 1 butter 3