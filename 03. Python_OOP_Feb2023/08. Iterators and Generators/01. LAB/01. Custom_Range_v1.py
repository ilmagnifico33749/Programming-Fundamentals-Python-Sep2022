class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_value = ...

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            self.current_value = self.start
            self.start += 1
            return self.current_value
        else:
            raise StopIteration()


# ##################################
# Test_Code_1:
one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
# ---------------------------------
# Output_1:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ##################################

