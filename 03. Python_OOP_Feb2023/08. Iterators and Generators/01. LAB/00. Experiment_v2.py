

# class MyGenerator:
#     def __init__(self, original_thing):
#         self.original_thing = original_thing
#
#     def __next__(self):
#         return self
#
#     def __iter__(self):
#         while True:
#             for char in self.original_thing:
#                 yield char

def my_gen(thing):
    for char in range(len(thing)):
        yield thing[char]


class MyIterator:
    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
        self.current_index = 0
        self.final_index = (len(iterable_object) - 1)
        self.iteration_step = 1
        self.current_value = ...

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= self.final_index:
            self.current_value = self.iterable_object[self.current_index]
            self.current_index += self.iteration_step
            return self.current_value
        else:
            raise StopIteration()


my_string = 'Abcedifuty0o'
# # iterable_object = MyIterator(my_string)
# # generated_object = MyGenerator(MyIterator(my_string))
generated_iterable_object = list(my_gen(my_string))
generated_object = MyIterator(generated_iterable_object)
while True:
    print(next(generated_object))

# for n in my_gen(my_string):
#     print(n)

# print(list(my_gen(my_string)))




