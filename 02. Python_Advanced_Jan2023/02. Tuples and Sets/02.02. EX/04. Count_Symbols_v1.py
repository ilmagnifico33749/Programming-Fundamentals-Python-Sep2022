sentence_tuple = (sorted([x for x in input()]))
sentence_set = set()
[sentence_set.add(x) for x in sentence_tuple]
[print(f"{x}: {sentence_tuple.count(x)} time/s") for x in sorted(sentence_set)]

# ########################
# Input_1:
# SoftUni rocks
# ------------------------
# Output_1:
# : 1 time/s
# S: 1 time/s
# U: 1 time/s
# c: 1 time/s
# f: 1 time/s
# i: 1 time/s
# k: 1 time/s
# n: 1 time/s
# o: 2 time/s
# r: 1 time/s
# s: 1 time/s
# t: 1 time/s
# ########################
# Input_2:
# Why do you like Python?
# ------------------------
# Output_2:
#  : 4 time/s
# ?: 1 time/s
# P: 1 time/s
# W: 1 time/s
# d: 1 time/s
# e: 1 time/s
# h: 2 time/s
# i: 1 time/s
# k: 1 time/s
# l: 1 time/s
# n: 1 time/s
# o: 3 time/s
# t: 1 time/s
# u: 1 time/s
# y: 3 time/s
# ########################


