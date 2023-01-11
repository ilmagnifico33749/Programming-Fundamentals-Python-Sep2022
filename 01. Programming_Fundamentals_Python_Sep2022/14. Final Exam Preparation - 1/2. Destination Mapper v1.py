places_string = input()
valid_destinations = []

init = False
validating = False
word_validity = True
start_index = int()
end_index = int()

for symbol in range(len(places_string)):

    current_symbol = places_string[symbol]
    if current_symbol == "=" or current_symbol == "/":
        if init is False:
            start_index = symbol
            init = True
        elif init is True:
            end_index = symbol
            validating = True
        if validating is True:
            current_word = places_string[start_index:end_index+1]
            if current_word[0] != current_word[len(current_word)-1]:
                word_validity = False
                break
            else:
                for letter in range(1, len(current_word)-1):
                    if current_word[letter].isalpha() == False:
                        word_validity = False
                        break

            if word_validity is True:
                valid_destinations.append(current_word[1:len(current_word)-1])
                validating = False
                init = False

print(f"Destinations: {', '.join(valid_destinations)}\nTravel Points: {sum([len(x) for x in valid_destinations])}")

# ---------------------------------------------------------#
# ---------------------------------------------------------#
# Input_1:
# =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=
# ---------------------------------------------------------#
# Output_1:
# Destinations: Hawai, Cyprus
# Travel Points: 11
# ---------------------------------------------------------#
# ---------------------------------------------------------#
# Input_2:
# ThisIs some InvalidInputTh
# ---------------------------------------------------------#
# Output_2:
# Destinations: Travel Points: 0
# ---------------------------------------------------------#
# ---------------------------------------------------------#
