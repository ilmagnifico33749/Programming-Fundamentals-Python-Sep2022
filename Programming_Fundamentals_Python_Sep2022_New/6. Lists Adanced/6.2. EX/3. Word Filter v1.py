# input_1: kiwi orange banana apple
# output_1: kiwi orange banana

# input_2: pizza cake pasta chips
# output_2: cake

user_input = input().split(" ")
word_even_len = [x for x in user_input if len(x)% 2 == 0]
print("\n".join(word_even_len))
