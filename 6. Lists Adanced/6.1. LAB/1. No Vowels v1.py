vowels = ["a", "o", "u", "e", "i"]
word = str(input())
consonants_only = [letter for letter in word if letter not in vowels]
print("".join(consonants_only))