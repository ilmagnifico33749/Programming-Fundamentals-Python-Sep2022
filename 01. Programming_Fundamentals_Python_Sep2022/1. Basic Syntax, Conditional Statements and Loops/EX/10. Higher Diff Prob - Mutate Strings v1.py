word_one = str(input())
word_two = str(input())
last_word = word_one


for i in range(len(word_one)):
    left_part = word_two[:i +1]
    right_part = word_one[i + 1:]
    current_word = left_part + right_part
    if current_word == last_word:
        continue
    print(current_word)
    last_word = current_word
