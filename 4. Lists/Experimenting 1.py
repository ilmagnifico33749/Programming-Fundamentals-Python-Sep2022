team_A = []
team_B = []
for index in range(1, 12):
    symbol_A = "A-" + str(index)
    team_A.append(symbol_A)
    symbol_B = "B-" + str(index)
    team_B.append(symbol_B)
sequence_of_cards = input().split()
for card in sequence_of_cards:
    card_for_player = card.split("-")
    print(card_for_player)