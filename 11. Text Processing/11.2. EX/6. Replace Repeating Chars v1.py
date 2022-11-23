original_word = input()
new_word = ""
for symbol in range(len(original_word)):
    current_letter = original_word[symbol]
    previous_letter = ""
    if symbol > 0:
        previous_letter = original_word[symbol - 1]
    else:
        pass
    if current_letter != previous_letter:
        new_word += current_letter
    else:
        pass

print(new_word)

# aaaaabbbbbcdddeeeedssaa
# qqqwerqwecccwd

