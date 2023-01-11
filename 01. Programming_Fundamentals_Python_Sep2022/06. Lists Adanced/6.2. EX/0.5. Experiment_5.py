# list_words = ["abc", "defg", "hikjl", "mno", "p", "q"]
#
# word_one = [word for word in list_words if len(word) <= 3 and len(word) > 1]
# print(word_one)
#
# upp_range = 4
# low_range = 2
# word_two = [list_words[word] for word in range(len(list_words)) if word in range(low_range, upp_range + 1)]
# print(word_two)
# ------------------------------------------------------------------------
# list_words = ["abc", "defg", "hikjl", "mno", "p", "q"]
# words = [list_words.pop(x) for x in range(len(list_words)) if x == 0]
# print(words)
# word = str(''.join(words))
# print(f"Word: {word}")
# letters_one = [letter for letter in word]
# print(letters_one)
# letters_two = [word[letters] for letters in range(len(word))]
# print(letters_two)
#
# for letter in range(len(str(word))):
#     print(word[letter])
# ----------------------------------------------------------------------------

list_letters = ['a', 'b', 'c', 'd']
print(list_letters)
print(len(list_letters))
times_to_divide = 2
# list_letters_two = [list_letters.pop(letter) for letter in range(len(list_letters))
#                     if (len(list_letters)) > ((len(list_letters)) - times_to_divide)]
list_letters_two = [list_letters.pop(0) for letter in range(len(list_letters)) if letter < times_to_divide]
print(list_letters_two)
list_three = [''.join(list_letters_two)]
print(list_three)