km_passed = 0

matrix_square_size = int(input())
number_racing_car = str(input())

def matrix_creator(square_size):
    created_matrix = [[x for x in input().split()] for row in range(square_size)]
    return created_matrix

matrix = matrix_creator(matrix_square_size)


def car_movement(command, car_current_position, matrix_size):
    car_initial_position = [int(x) for x in car_current_position]
    car_new_position = []
    if command == "left":
        car_new_position = [car_initial_position[0], (car_initial_position[1] - 1)]
    elif command == "right":
        car_new_position = [car_initial_position[0], (car_initial_position[1] + 1)]
    elif command == "up":
        car_new_position = [(car_initial_position[0] - 1), car_initial_position[1]]
    elif command == "down":
        car_new_position = [(car_initial_position[0] + 1), car_initial_position[1]]


    def position_validity(new_position, matrix_size):
        validity = False
        if 0 <= car_new_position[0] <= (matrix_size-1) and 0 <= car_new_position[1] <= (matrix_size - 1):
            validity = True
        return validity

    if position_validity(car_new_position, matrix_size) is True:
        return car_new_position
    elif position_validity(car_current_position, matrix_size) is not True:
        return car_initial_position


def tunnel(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            current_symbol = matrix[row][column]
            if current_symbol == "T":
                tunnel_exit_coordinates = ([row, column])
    return tunnel_exit_coordinates


def car_position_significance(current_matrix, car_current_position, current_km_passed):
    race_finished = False
    car_new_initial_position = car_current_position
    car_new_final_position = []
    current_position = current_matrix[car_current_position[0]][car_current_position[1]]
    if current_position == ".":
        current_km_passed += 10
        car_new_final_position = car_new_initial_position
    elif current_position == "T":
        current_km_passed += 30
        car_new_final_position = tunnel(current_matrix)
        current_matrix[car_current_position[0]][car_current_position[1]] = "."
        current_matrix[car_new_final_position[0]][car_new_final_position[1]] = "."
    elif current_position == "F":
        current_km_passed += 10
        race_finished = True
        car_new_final_position = car_new_initial_position
    return current_matrix, race_finished, car_new_final_position, current_km_passed


def race(race_track, car_current_position, current_km_passed, race_finished):
    command = input()
    if race_finished is False and command != "End":
        car_new_position = car_movement(command, car_current_position, matrix_size=matrix_square_size)
        race_track, race_finished, car_new_position, current_km_passed = car_position_significance(race_track, car_new_position, current_km_passed)
        return race(race_track, car_new_position, current_km_passed, race_finished)
    elif race_finished is True:
        print(f"Racing car {number_racing_car} finished the stage!")
        print(f"Distance covered {current_km_passed} km.")
        race_track[car_current_position[0]][car_current_position[1]] = "C"
        [print(''.join(row)) for row in race_track]
    elif command == "End":
        print(f"Racing car {number_racing_car} DNF.")
        print(f"Distance covered {current_km_passed} km.")
        race_track[car_current_position[0]][car_current_position[1]] = "C"
        [print(''.join(row)) for row in race_track]


race(matrix, [0, 0], km_passed, race_finished=False)


# ##################################
# Input_1:
# 5
# 01
# . . . . .
# . . . T .
# . . . . .
# . T . . .
# . . F . .
# down
# right
# right
# right
# down
# right
# up
# down
# right
# up
# End
# ----------------------------------
# Output_1:
# Racing car 01 finished the stage!
# Distance covered 80 km.
# .....
# .....
# .....
# .....
# ..C..
# ##################################
# Input_2:
# 10
# 45
# . . . . . . . . . .
# . . T . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . F . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . T . .
# right
# down
# down
# right
# up
# left
# up
# up
# End
# ----------------------------------
# Output_2:
# Racing car 45 DNF.
# Distance covered 100 km.
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ......F...
# ......C...
# ..........
# ..........
# ##################################
