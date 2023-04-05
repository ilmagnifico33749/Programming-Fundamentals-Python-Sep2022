

class CustomRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current_value = ...

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            self.current_value = self.start
            self.start += self.step
            return self.current_value
        else:
            raise StopIteration()

    def __repr__(self): return str(self.current_value)




custom_iter = CustomRange(1, 11, 2)
print(iter(custom_iter))
# print(next(custom_iter))
# print(next(custom_iter))

# while True:
#     print(next(custom_iter))





