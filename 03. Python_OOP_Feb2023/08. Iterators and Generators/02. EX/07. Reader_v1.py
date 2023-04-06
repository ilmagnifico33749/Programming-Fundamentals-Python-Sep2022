def read_next(*iterable):
    for item in iterable:
        for sub_item in item:
            yield sub_item


# ##################################
# Test_Code_1:
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
# ---------------------------------
# Output_1:
# string2dict
# ##################################
# Test_Code_2:
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
# ---------------------------------
# Output_2:
# N
# e
# e
# d
# 2
# 3
# words
# .
# ##################################
