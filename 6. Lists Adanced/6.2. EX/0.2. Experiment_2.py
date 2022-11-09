list_one = ["arp", "live", "strong"]
list_two = ["lively", "alive", "harp", "sharp", "armstrong"]
letters_current_word = []
words_encountered = list(map(lambda x: x == word , list_two))
for word in list_one:
    print([word for x in list_two if word in x])

print(words_encountered)
