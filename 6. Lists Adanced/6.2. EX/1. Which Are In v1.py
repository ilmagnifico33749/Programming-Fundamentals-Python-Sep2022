list_one = input().split(", ")
list_two = input().split(", ")
list_three = []

for word_one in list_one:
    for word_two in list_two:
        if word_one in word_two and word_one not in list_three:
            list_three.append(word_one)
print(list_three)