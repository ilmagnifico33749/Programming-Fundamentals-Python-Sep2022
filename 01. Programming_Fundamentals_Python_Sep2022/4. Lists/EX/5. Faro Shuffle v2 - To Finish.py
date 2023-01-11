original_deck = input().split()
number_shuffles = int(input())
print(original_deck)
upper_card = ""
bottom_card = ""
deck_lenght = len(original_deck)
upper_card = original_deck[deck_lenght - 1]
bottom_card = original_deck[0]

deck_middle = deck_lenght / 2

for number_shuffles in range(number_shuffles):
    new_deck = []
    left_part = original_deck[0: deck_middle]
    right_part = original_deck[deck_middle::]
    for cards in range(0, len(original_deck)):
        new_deck.append(left_part[cards])
        new_deck.append(right_part[cards])

