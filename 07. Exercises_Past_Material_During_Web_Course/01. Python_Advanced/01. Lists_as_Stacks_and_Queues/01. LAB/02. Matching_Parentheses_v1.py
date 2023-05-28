expression = input()
# expression = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
# expression = "(2 + 3) - (2 + 3)"

all_sets = list()

opening_parenthesis_index = int()
closing_parenthesis_index = int()
parenthesis_to_skip = 0


for element_index in range(len(expression)):
    current_symbol = expression[element_index]
    if current_symbol == "(":
        opening_parenthesis_index = element_index

        for subelement_index in range(opening_parenthesis_index+1, len(expression)):
            current_subsymbol = expression[subelement_index]
            if current_subsymbol == "(":
                parenthesis_to_skip += 1
            elif current_subsymbol == ")":
                if parenthesis_to_skip > 0:
                    parenthesis_to_skip -= 1
                else:
                    closing_parenthesis_index = subelement_index
                    all_sets.append(expression[opening_parenthesis_index:closing_parenthesis_index+1])
                    break

[print(all_sets.pop()) for times in range(len(all_sets))]

