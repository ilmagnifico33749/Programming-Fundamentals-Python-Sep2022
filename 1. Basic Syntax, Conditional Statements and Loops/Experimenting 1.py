#a = input()
#print(ord(a))
#print(chr(97))
#new_command = ""



word_one = str(input())
word_two = str(input())
new_word = ""

if new_word != word_two:
    for i in range(len(word_one)):
        symbol_one = word_one[i]
        for j in range(len(word_two)):
            symbol_two = word_two[j]
            if symbol_two != symbol_one:
                new_word += str(symbol_two)
else:
    pass
print(new_word)

