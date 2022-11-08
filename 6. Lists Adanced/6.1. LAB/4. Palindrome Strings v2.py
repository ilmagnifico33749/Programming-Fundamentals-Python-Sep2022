list_words = input().split(" ")
palindrome = input()
print(f"{[word for word in list_words if word == ''.join(reversed(word))]}\nFound palindrome {list_words.count(palindrome)} times")