a = ["8", 5, 6]

def simp_func(list_nums):
    result = 0
    for i in list_nums:
        if i.isdigit() is True:
            result += i
        else:
            raise AssertionError("The symbol is not an Integer")
    return result

try:
    simp_func(a)

except AssertionError as error:
    print(error)
