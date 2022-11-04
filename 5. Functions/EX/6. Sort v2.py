# 4 6 2 8

initial_list = input().split()

def list_str_to_int(list):
    list_int = []
    for string in list:
        list_int.append(int(string))
    return list_int


def sorting(list):

    sorted_list = sorted(list)
    return sorted(list)

print(sorting(sorting(list_str_to_int(initial_list))))