class vowels:
    valid_symbols = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"]
    def __init__(self, iterable):
        self.iterable = [x for x in iterable]
        self.current_index = 0
        self.max_index = (len(self.iterable) - 1)
        self.current_value = ...


    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= self.max_index:
            self.current_value = self.iterable[self.current_index]
            self.current_index += 1
            if self.current_value in self.valid_symbols:
                return self.current_value
            else:
                return self.__next__()
        else:
            raise StopIteration


# ##################################
# Test_Code_1:
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
# ---------------------------------
# Output_1:
# A
# e
# i
# u
# y
# o
# ##################################