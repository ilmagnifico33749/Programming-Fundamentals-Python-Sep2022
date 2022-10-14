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
    if card[0] == "A":
        for player in team_A:
            player_no = player.split("-")
            if player_no[1] == card[2]:
                team_A.remove(player)
                print(f"Removed {player}")
    if card[0] == "B":
        for player in team_B:
            player_no = player.split("-")
            if player_no[1] == card[2]:
                team_B.remove(player)
                print(f"Removed {player}")