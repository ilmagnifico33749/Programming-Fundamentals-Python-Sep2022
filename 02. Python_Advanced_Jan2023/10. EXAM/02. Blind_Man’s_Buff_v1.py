#85/100 - 1 of 7 failed
rows, columns = [int(x) for x in input().split()]


def matrix_creator(rows_number):
    created_matrix = [[str(x) for x in input().split()] for rows in range(rows_number)]
    return created_matrix
starting_playground = matrix_creator(rows)


def player_starting_position_identifier(playground):
    position = []
    for row in range(len(playground)):
        for column in range(len(playground[row])):
            if playground[row][column] == "B":
                position = [row, column]
    return position
player_starting_position = player_starting_position_identifier(starting_playground)

def player_movement(command, starting_position, current_playground):
    valid_new_position = False
    starting_position = starting_position
    current_playground = current_playground
    new_position = []
    if command == "up":
        new_position = [(starting_position[0]-1), starting_position[1]]
    elif command == "down":
        new_position = [(starting_position[0]+1), starting_position[1]]
    elif command == "left":
        new_position = [starting_position[0], (starting_position[1]-1)]
    elif command == "right":
        new_position = [starting_position[0], (starting_position[1]+1)]

    if 0 <= new_position[0] <= len(current_playground) and 0 <= new_position[1] <= len(current_playground[0]):
        valid_new_position = True
    if current_playground[new_position[0]][new_position[1]] == "O":
        valid_new_position = False

    if valid_new_position is True:
        return new_position
    else:
        return starting_position


def game(playground, player_position, touched_opponents, turn):
    initial_position_player = player_position
    current_playground = playground
    touched_opponents = touched_opponents
    current_turn = turn
    command = input()
    while command != "Finish" and touched_opponents < 3:
        new_position_player = player_movement(command, initial_position_player, current_playground)
        if new_position_player != initial_position_player:
            current_turn += 1
            if current_playground[new_position_player[0]][new_position_player[1]] == "P":
                touched_opponents += 1
                current_playground[new_position_player[0]][new_position_player[1]] = "-"

        return game(current_playground, new_position_player, touched_opponents, current_turn)
    else:
        return f"Game over!\nTouched opponents: {touched_opponents} Moves made: {current_turn}"


print(game(starting_playground, player_starting_position, touched_opponents=0, turn=0))

#
# #############################################
# Input_1:
# 5 8
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -
# up
# up
# left
# Finish
# ---------------------------------------------
# Output_1:
# 5 8
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -
# up
# up
# left
# Finish	Game over!
# Touched opponents: 1 Moves made: 3
# #############################################
# Input_2:
# 4 4
# O B O -
# - P O P
# - - P -
# - - - -
# left
# right
# down
# right
# down
# right
# up
# right
# up
# down
# Finish
# ---------------------------------------------
# Output_2:
# Game over!
# Touched opponents: 3 Moves made: 5
# #############################################
