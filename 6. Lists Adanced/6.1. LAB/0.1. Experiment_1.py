original_list = [6, 2, 1, 4, 3, 5]
a = [-x for x in original_list]
print(a)

def b(list):
    for names in original_list:
        c = lambda names: (-len(names), names)
        return c
print(b)



