user_input = list(input())
reversed_sentence = []

while user_input:
    reversed_sentence.append(user_input.pop())

print(''.join(reversed_sentence))