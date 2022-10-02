word_one = str(input())
word_two = str(input())
new_word = ""

if word_one != word_two:
    for i in range(len(word_one)):
        symbol_one = word_one[i]
        symbol_two = word_two[i]
        if symbol_one != symbol_two:
            symbol_one = symbol_two

        else:
            pass
    print(word_one)
