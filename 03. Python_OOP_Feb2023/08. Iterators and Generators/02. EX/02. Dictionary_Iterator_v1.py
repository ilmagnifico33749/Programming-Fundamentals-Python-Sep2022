class dictionary_iter:
    def __init__(self, dictionary):
        self.current_index = 0
        self.current_value = ...
        self.iterable = list(dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= len(self.iterable) - 1:
            self.current_value = self.iterable[self.current_index]
            self.current_index += 1
            return self.current_value
        else:
            raise StopIteration


# ##################################
# Test_Code_1:
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
# ---------------------------------
# Output_1:
# (1, '1')
# (2, '2')
# ##################################
# Test_Code_1:
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
# ---------------------------------
# Output_1:
# ("name", "Peter")
# ("age", 24)
# ##################################
