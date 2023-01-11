# 1.2.3
# 1.3.9
# 3.9.9

list_version_details = input().split(".")
list_new_values = []

for value in range(len(list_version_details)-1, -1, -1):
    current_value = int(list_version_details.pop(value))
    new_value = 0
    if current_value < 9:
        new_value = current_value + 1
        list_version_details.insert(value, str(new_value))
        break
    else:
        new_value = 0
        list_version_details.insert(value, str(new_value))
print(".".join(list_version_details))

