team_A = []
team_B = []
game_terminated = False
for index in range(1, 12):
    symbol_A = "A-" + str(index)
    team_A.append(symbol_A)
    symbol_B = "B-" + str(index)
    team_B.append(symbol_B)
sequence_of_cards = input().split()
for card in sequence_of_cards:
    card_details = card.split("-")
    card_for_player = int(card_details[1])
    if card[0] == "A":
        for player in team_A:
            player_details = player.split("-")
            player_no = int(player_details[1])
            if player_no == card_for_player:
                team_A.remove(player)
    if card[0] == "B":
        for player in team_B:
            player_details = player.split("-")
            player_no = int(player_details[1])
            if player_no == card_for_player:
                team_B.remove(player)
    if len(team_A) < 7 or len(team_B) < 7:
        game_terminated = True
        print(f"Team A - {len(team_A)}; Team B - {len(team_B)}\nGame was terminated")
        break

if game_terminated == False:
    print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
