# wow father mom wow shirt stats
# wow

list_words = input().split(" ")
user_palindrome = str(input())
count_palindromes = 0
final_list = ""
list_all_palindromes = []

for word in list_words:
    if word == "".join(reversed(word)):
        list_all_palindromes.append(word)
print(list_all_palindromes)
print(f"Found palindrome {list_all_palindromes.count(user_palindrome)} times")
