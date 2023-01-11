word = input()
numbers = ""
letters = ""
other_symbols = ""
for symbol in word:
    if symbol.isdigit():
        numbers += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        other_symbols += symbol

print(f"{numbers}\n{letters}\n{other_symbols}")

# Agd#53Dfg^&4F53
