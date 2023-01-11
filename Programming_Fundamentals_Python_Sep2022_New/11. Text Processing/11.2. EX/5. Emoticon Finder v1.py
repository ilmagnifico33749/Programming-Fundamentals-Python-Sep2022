user_input = input()

for symbol in range(len(user_input)):
    if user_input[symbol] == ":":
        print(f"{user_input[symbol]}{user_input[symbol + 1]}")

# input: There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
# output:
#  :P
#  :O
#  :)

