word = str(input())
vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
consonants_only = "".join([letter for letter in word if letter not in vowels])
print(consonants_only)