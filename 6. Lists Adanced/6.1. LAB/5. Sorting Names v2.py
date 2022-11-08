orig_list_names = input().split(", ")

def sorting(list):
    sorted_list = sorted(list, key=lambda x: (-len(x), x))
    return sorted_list

print(sorting(orig_list_names))