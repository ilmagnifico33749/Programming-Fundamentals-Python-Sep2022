class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = [str(x) for x in sequence]
        self.number = number
        self.current_value = ...
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 0:
            self.current_value = self.sequence[self.current_index]
            if self.current_index >= len(self.sequence) - 1:
                self.current_index = 0
            else:
                self.current_index += 1
            self.number -= 1
            return self.current_value
        else:
            raise StopIteration



# ##################################
# Test_Code_1:
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
# ---------------------------------
# Output_1:
# abcab
# ##################################
# Test_Code_2:
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
# ---------------------------------
# Output_2:
# I L
# ##################################
