

class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current_index = (len(self.iterable) - 1)
        self.current_value = ...

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= 0:
            self.current_value = self.iterable[self.current_index]
            self.current_index -= 1
            return self.current_value
        else:
            raise StopIteration()


# ##################################
# Test_Code_1:
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
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

