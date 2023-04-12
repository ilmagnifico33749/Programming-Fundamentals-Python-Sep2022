field_size = int(input())
all_movement_commands = input(). split(", ")

def matrix_creator(matrix_size):
    created_matrix = [[str(x) for x in input()] for times in range(matrix_size)]
    return created_matrix

def current_position_identifier(current_field):
    current_position = ...
    position_found = False
    for row_num in range(len(current_field)):
        for column_num in range(len(current_field[row_num])):
            current_field_value = current_field[row_num][column_num]
            if current_field_value == "s":
                current_position = [row_num, column_num]
                position_found = True
                break
        if position_found is True:
            break
    return current_position

def new_position_identifier(current_position_squirrel, movement_command):
    starting_position = current_position_squirrel
    new_position = ...
    if movement_command == "up":
        new_position = [(starting_position[0]-1), starting_position[1]]
    if movement_command == "down":
        new_position = [(starting_position[0]+1), starting_position[1]]
    if movement_command == "left":
        new_position = [starting_position[0], (starting_position[1]-1)]
    if movement_command == "right":
        new_position = [starting_position[0], (starting_position[1]+1)]
    return new_position

def new_position_validation(current_field, new_position):
    hazelnut_found = False
    trap_found = False
    position_validity = ...
    out_of_field = False
    game_over = ...
    new_current_position = new_position
    new_position_field_value = ...
    if 0 <= new_current_position[0] <= (len(current_field)-1):
        if 0 <= new_current_position[1] <= (len(current_field[new_current_position[0]])-1):
            new_position_field_value = current_field[new_position[0]][new_position[1]]
            if new_position_field_value == "h":
                hazelnut_found = True
                position_validity = True
            elif new_position_field_value == "t":
                trap_found = True
            elif new_position_field_value == "*":
                position_validity = True
        else:
            out_of_field = True
    else:
        out_of_field = True

    if out_of_field is False and position_validity is True and trap_found is False:
        game_over = False
    else:
        game_over = True

    return game_over, hazelnut_found, trap_found, out_of_field, position_validity

def game(play_field, list_commands):
    current_field = play_field
    list_all_commands = list_commands
    hazelnuts_on_field = 3
    hazelnuts_collected = 0
    trap_found = ...
    out_of_field = ...
    game_over = ...
    new_position_validity = ...

    for moves in range(len(list_all_commands)):
        current_movement_command = list_all_commands[moves]
        current_position_squirrel = current_position_identifier(current_field)
        new_position_squirrel = new_position_identifier(current_position_squirrel, current_movement_command)
        game_over, hazelnut_found, trap_found, out_of_field, new_position_validity = new_position_validation(current_field, new_position_squirrel)
        if game_over is True:
            break
        if hazelnut_found is True:
            hazelnuts_on_field -= 1
            hazelnuts_collected +=1
            if hazelnuts_on_field == 0:
                game_over = True
        if new_position_validity is True:
            current_field[current_position_squirrel[0]][current_position_squirrel[1]] = "*"
            current_field[new_position_squirrel[0]][new_position_squirrel[1]] = "s"

    if game_over is True:
        if hazelnuts_on_field == 0:
            return f"Good job! You have collected all hazelnuts!\nHazelnuts collected: {hazelnuts_collected}"
        elif trap_found is True:
            return f"Unfortunately, the squirrel stepped on a trap...\nHazelnuts collected: {hazelnuts_collected}"
        elif out_of_field is True:
            return f"The squirrel is out of the field.\nHazelnuts collected: {hazelnuts_collected}"
    else:
        return f"There are more hazelnuts to collect.\nHazelnuts collected: {hazelnuts_collected}"


field = matrix_creator(field_size)
print(game(field, all_movement_commands))


# ###################################################
# Test_Code_1:
# 5
# left, left, up, right, up, up
# **h**
# t****
# *h***
# *h*s*
# *****
# ---------------------------------------------------
# Output_1:
# Good job! You have collected all hazelnuts!
# Hazelnuts collected: 3
# ###################################################
# Test_Code_2:
# 4
# down, down, right, right
# *s*h
# ***h
# ***t
# h***
# ---------------------------------------------------
# Output_2:
# Unfortunately, the squirrel stepped on a trap...
# Hazelnuts collected: 0
# ###################################################
# Test_Code_3:
# 4
# down, down, right, right
# h***
# ***h
# *s*t
# **h*
# ---------------------------------------------------
# Output_3:
# The squirrel is out of the field.
# Hazelnuts collected: 0
# ###################################################