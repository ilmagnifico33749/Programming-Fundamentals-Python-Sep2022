class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_index = 0
        self.current_value = ...
        self.iterable_object = [x * self.step for x in range(self.count)]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= (len(self.iterable_object) - 1):
            self.current_value = self.iterable_object[self.current_index]
            self.current_index += 1
            return self.current_value
        else:
            raise StopIteration


# ##################################
# Test_Code_1:
numbers = take_skip(2, 6)
for number in numbers:
    print(number)
# ---------------------------------
# Output_1:
# 0
# 2
# 4
# 6
# 8
# 10
# ##################################
# Test_Code_1:
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
# ---------------------------------
# Output_1:
# 0
# 10
# 20
# 30
# 40
# ##################################
