input_line_one = input().split(", ")
input_line_two = input().split(", ")
letters_current_word = []
words_encountered = []
for word in input_line_one:
    print([word for x in input_line_two if word in x])