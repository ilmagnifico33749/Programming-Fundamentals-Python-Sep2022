submarine_health = 3

def matrix_creator(square_size):
    matrix_created = [[str(x) for x in input()] for rows in range(square_size)]
    return matrix_created

battlefield = matrix_creator(int(input()))


def current_position_action(primary_matrix, current_position, submarine_life_points):
    current_field = primary_matrix[current_position[0]][current_position[1]]
    if current_field == "-":
        primary_matrix[current_position[0]][current_position[1]] = "S"
    elif current_field == "*":
        submarine_life_points -= 1
        primary_matrix[current_position[0]][current_position[1]] = "S"
    elif current_field == "C":
        primary_matrix[current_position[0]][current_position[1]] = "S"

    return primary_matrix, submarine_life_points


def submarine_radar(primary_matrix):
    ships_existence = True
    number_of_ships = 0
    for row in primary_matrix:
        for column in row:
            if column == "C":
                number_of_ships += 1
    return number_of_ships


def submarine_position(primary_matrix):
    current_position_submarine = []
    position_validity = False
    for row in range(len(primary_matrix)):
        for column in range(len(primary_matrix[row])):
            if primary_matrix[row][column] == "S":
                current_position_submarine = [row, column]
    return current_position_submarine


initial_position_submarine = submarine_position(battlefield)
battlefield[initial_position_submarine[0]][initial_position_submarine[1]] = "-"


def submarine_movement(battlefield, command, submarine_position):
    position_validity = False
    starting_position_submarine = submarine_position
    new_position_submarine = []
    if command == "up":
        new_position_submarine = [(submarine_position[0] - 1), starting_position_submarine[1]]
    elif command == "down":
        new_position_submarine = [(submarine_position[0] + 1), starting_position_submarine[1]]
    elif command == "left":
        new_position_submarine = [submarine_position[0], (starting_position_submarine[1] - 1)]
    elif command == "right":
        new_position_submarine = [submarine_position[0], (starting_position_submarine[1] + 1)]

    def position_validity(position, battlefield):
        validity = False
        if 0 <= new_position_submarine[0] <= (len(battlefield)-1) and 0 <= new_position_submarine[1] <= (len(battlefield[0])-1):
            validity = True
        return validity

    position_validity = position_validity(new_position_submarine, battlefield)
    if position_validity is True:
        battlefield[starting_position_submarine[0]][starting_position_submarine[1]] = "-"
        return new_position_submarine
    elif position_validity is False:
        return initial_position_submarine


def battle_turn(battlefield, submarine_life_points, submarine_position):
    command = input()
    new_position_submarine = submarine_movement(battlefield, command, submarine_position)
    new_situation_battlefield, new_submarine_life_points = current_position_action(battlefield, new_position_submarine, submarine_life_points)
    current_number_ships = submarine_radar(battlefield)
    if new_submarine_life_points > 0 and current_number_ships > 0:
        return battle_turn(new_situation_battlefield, new_submarine_life_points, new_position_submarine)
    else:
        if new_submarine_life_points == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates {new_position_submarine}!")
            [print(''.join(row)) for row in new_situation_battlefield]
        elif current_number_ships == 0:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            [print(''.join(row)) for row in new_situation_battlefield]


battle_turn(battlefield, submarine_health, initial_position_submarine)


# ###########################################################################
# Input_1:
# 5
# *--*-
# -S-*C
# -*---
# -----
# -C-*C
# right
# down
# left
# up
# right
# right
# right
# down
# down
# down
# up
# left
# left
# left
# down
# ---------------------------------------------------------------------------
# Output_1:
# Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!
# *--*-
# -----
# -----
# -----
# -S-*-
# ###########################################################################
# Input_2:
# 5
# *--*-
# -S-*C
# -*---
# -----
# *C-*C
# right
# right
# up
# left
# left
# left
# ---------------------------------------------------------------------------
# Output_2:
# Mission failed, U-9 disappeared! Last known coordinates [0, 0]!
# S----
# ----C
# -*---
# -----
# *C-*C
# ###########################################################################
