n = int(input())
word = str(input())
list_all_words = []
list_filtered_words = []
for strings in range(n):
    string = str(input())
    list_all_words.append(string)
    if word in string:
        list_filtered_words.append(string)
print(f"{list_all_words}\n{list_filtered_words}")
