original_deck = input().split()
number_shuffles = int(input())

for number_shuffles in range(number_shuffles):
    new_deck = []
    deck_middle = len(original_deck) // 2
    left_part = original_deck[0: deck_middle]
    right_part = original_deck[deck_middle::]
    for cards in range(len(left_part)):
        new_deck.append(left_part[cards])
        new_deck.append(right_part[cards])
    original_deck = new_deck
print(original_deck)
