# 4 6 2 8

initial_list = input().split()

def list_str_to_int(list):
    list_int = []
    for string in list:
        list_int.append(int(string))
    return list_int


def sorting(list):
    list_int = list
    list_sorted = []
    for numbers in range(len(list_int)):
        list_sorted.append(min(list_int))
        list_int.remove(min(list_int))
    return list_sorted

print(sorting(sorting(list_str_to_int(initial_list))))

