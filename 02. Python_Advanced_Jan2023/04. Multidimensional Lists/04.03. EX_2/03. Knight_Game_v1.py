rows_num = int(input())

def matrix_creator(rows_number):
    matrix_created = [[str(x) for x in input()] for rows in range(rows_number)]
    return matrix_created


matrix = matrix_creator(rows_num)


def knight_movements(matrix_size, knight_initial_row, knight_initial_column, dictionary_knights):
    matrix_size = matrix_size
    knight_initial_row = knight_initial_row
    knight_initial_column = knight_initial_column
    dictionary_knights = dictionary_knights
    dictionary_knights[f"Knight_{knight_initial_row}_{knight_initial_column}"] = {}

    current_row = knight_initial_row - 3
    for rows in range(1, 6):
        current_row += 1
        position_validity = False
        if rows != 3:
            if rows % 2 != 0:
                column_modifier = 1
            else:
                column_modifier = 2

            for columns in range(2):
                if columns == 0:
                    current_column = knight_initial_column - column_modifier
                    current_position = tuple([current_row, current_column])
                elif columns == 1:
                    current_column = knight_initial_column + column_modifier
                    current_position = tuple([current_row, current_column])

                for coordinates in current_position:
                    if 0 <= coordinates < matrix_size:
                        position_validity = True
                    else:
                        position_validity = False
                        break

                if position_validity == True:
                    dictionary_knights[f"Knight_{knight_initial_row}_{knight_initial_column}"][
                        f"Position_{current_row}_{columns}"] = current_position
        else:
            pass


def dictionary_knights(primary_matrix):
    primary_matrix = primary_matrix
    my_dict_knights = {}
    for row in range(len(primary_matrix)):
        for column in range(len(primary_matrix[row])):
            element = primary_matrix[row][column]
            if element == "K":
                knight_position_row = row
                knight_position_column = column
                knight_movements(len(primary_matrix), knight_position_row, knight_position_column, my_dict_knights)

    for keys, values in my_dict_knights.items():
        for key in my_dict_knights.keys():
            my_dict_knights[key]["Count Takes: "] = 0
            for value in my_dict_knights[key]:
                if value != "Count Takes: ":
                    coordinate_row, coordinate_column = my_dict_knights[key][value]
                    if primary_matrix[coordinate_row][coordinate_column] == "K":
                        my_dict_knights[key]["Count Takes: "] += 1

    return my_dict_knights


def count_knights_menace(dict_all_knights):
    dict_all_knights = dict_all_knights
    knights_to_be_removed = {}
    for key in dict_all_knights.keys():
        for value in dict_all_knights[key]:
            if value == "Count Takes: ":
                if 0 < dict_all_knights[key][value]:
                    knights_to_be_removed[key] = dict_all_knights[key][value]
    sorted_knights_to_be_removed = sorted(knights_to_be_removed.items(), key=lambda x: x[1], reverse=True)

    return sorted_knights_to_be_removed


def filtration_removing_knights(primary_matrix, dict_knights_to_be_removed):
    primary_matrix = primary_matrix
    dict_knights_to_remove = dict_knights_to_be_removed
    dictionary_knights(matrix)
    number_knights_menace = len(count_knights_menace(dictionary_knights(matrix)))
    count_removed_knights = 0
    while number_knights_menace > 0:
        current_knight = (dict_knights_to_remove.pop(0))[0]
        count_removed_knights += 1
        current_knight_details = current_knight.split("_")
        current_knight_row = int(current_knight_details[1])
        current_knight_column = int(current_knight_details[2])
        primary_matrix[current_knight_row][current_knight_column] = "0"
        dict_knights_to_remove = count_knights_menace(dictionary_knights(primary_matrix))
        number_knights_menace = len(dict_knights_to_remove)


    return count_removed_knights

print(filtration_removing_knights(matrix, count_knights_menace(dictionary_knights(matrix))))

# ########
# Input_1:
# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0
# --------
# Output_1:
# 1
# ########
# Input_2:
# 2
# KK
# KK
# --------
# Output_2
# 0
# ########
# Input_3:
# 8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK
# --------
# Output_3:
# 12
# ########
