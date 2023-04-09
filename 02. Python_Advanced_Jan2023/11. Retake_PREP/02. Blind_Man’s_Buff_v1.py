def matrix_creator(matrix_size):
    rows_num, columns_num = [int(x) for x in (matrix_size.split(" "))]
    matrix_created = [input().split() for columns in range(rows_num)]
    return matrix_created

def ident_opponents_num(field):
    total_num_opponents = sum([row.count("P") for row in field])
    return total_num_opponents


def ident_player_position(matrix):
    player_position = ...
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            column_value = matrix[row][column]
            if column_value == "B":
                player_position = [row, column]
                return player_position


def new_position_validation(matrix, player_position):
    inside_field = ...
    position_validity = ...
    field_value = ...
    player_row = player_position[0]
    player_column = player_position[1]

    if 0 <= player_position[0] <= (len(matrix) - 1) and 0 <= player_position[1] <= (len(matrix[0]) - 1):
        inside_field = True
    else:
        inside_field = False

    if inside_field is True:
        field_value = matrix[player_position[0]][(player_position[1])]
        if field_value == "O":
            position_validity = False
        elif field_value == "-" or field_value == "P":
            position_validity = True
    else:
        position_validity = False

    return position_validity


def current_turn_outcome(matrix, movement_command):
    game_over = False
    field_turn_start = matrix
    field_turn_end = matrix
    dict_movement = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
    play_starting_position = ident_player_position(matrix)
    new_position = ...
    new_position_validity = False
    other_player_encountered = False

    if movement_command == "Finish":
        game_over = True
        return field_turn_end, new_position_validity, other_player_encountered, game_over

    for key, value in dict_movement.items():
        if key == movement_command:
            new_position = [(play_starting_position[0] + value[0]), (play_starting_position[1] + value[1])]
            break
    new_position_validity = new_position_validation(matrix, new_position)

    if new_position_validity is True:
        field_turn_end[play_starting_position[0]][play_starting_position[1]] = "-"
        if field_turn_end[new_position[0]][new_position[1]] == "P":
            other_player_encountered = True
        field_turn_end[new_position[0]][new_position[1]] = "B"

        return field_turn_end, new_position_validity, other_player_encountered, game_over

    else:
        return field_turn_start, new_position_validity, other_player_encountered, game_over


def game(field):
    initial_num_opponents = ident_opponents_num(field)
    moves_made = 0
    opponents_touched = 0
    opponents_remaining = initial_num_opponents
    game_over = False
    current_field = field
    new_field = ...


    while game_over is not True:
        new_field, new_position_validity, other_player_encountered, game_over = current_turn_outcome(current_field, str(input()))
        if new_position_validity is True:
            moves_made += 1
            current_field = new_field
            if other_player_encountered is True:
                opponents_touched += 1
                opponents_remaining -= 1


        current_num_opponents = ident_opponents_num(field)
        if current_num_opponents == 0:
            if current_num_opponents == opponents_remaining:
                game_over = True
        # result = f"{50 * '#'}\n"
        # result += '\n'.join([' '.join(row) for row in current_field])
        # result += f"\n{50 * '#'}"
        # print(result)
        # print(f"Moves made: {moves_made}\nOpponents touched:{opponents_touched}")
        # print(f"{50 * '#'} {['\n'.join(row) for row in current_field]} {50 * '#'}")
    else:
        return f"Game over!\nTouched opponents: {opponents_touched} Moves made: {moves_made}"


# print(matrix_creator(input()))

print(game(matrix_creator(input())))
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
# Finish
# Game over!
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
