class countdown_iterator:
    def __init__(self, count):
        self.countdown_start_num = count
        self.current_value = ...
        self.iterable = [x for x in range(self.countdown_start_num + 1)]
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= -len(self.iterable):
            self.current_value = self.iterable[self.current_index]
            self.current_index -= 1
            return self.current_value
        else:
            raise StopIteration


# ##################################
# Test_Code_1:
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
# ---------------------------------
# Output_1:
# 10 9 8 7 6 5 4 3 2 1 0
# ##################################
# Test_Code_2:
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
# ---------------------------------
# Output_2:
# 0
# ##################################
