# 123, 323, 421, 121

def comparison(norm_num, rev_num):
    nums_identicality = False
    if norm_num == rev_num:
        nums_identicality = True
        return "True"
    else:
        return "False"

print(comparison(123, 123))