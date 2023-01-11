input_line_one = input().split(", ")
input_line_two = input().split(", ")
print([word_one for word_one in input_line_one if any([word_one in word_two for word_two in input_line_two])])


