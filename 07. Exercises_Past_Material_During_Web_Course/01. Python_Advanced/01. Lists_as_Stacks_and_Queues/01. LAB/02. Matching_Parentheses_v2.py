expression = input()
# expression = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
# expression = "(2 + 3) - (2 + 3)"

all_sets = list()

opening_parenthesis_index = []
closing_parenthesis_index = []

for element in range(len(expression)):
    current_symbol = expression[element]
    if current_symbol == "(":
        opening_parenthesis_index.append(element)
    elif current_symbol == ")":
        closing_parenthesis_index.append(element+1)
        all_sets.append(expression[opening_parenthesis_index.pop():closing_parenthesis_index.pop()])

print('\n'.join(all_sets))



