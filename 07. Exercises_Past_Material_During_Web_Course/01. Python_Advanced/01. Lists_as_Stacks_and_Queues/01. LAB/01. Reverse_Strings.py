a = [x for x in input()]
b = list()

for times in range(len(a)):
    b.append(a.pop())

print(''.join(b))

