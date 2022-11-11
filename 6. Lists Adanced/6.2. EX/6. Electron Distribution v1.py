#---------------------------#
# input_1: 10               #
# output_1: [2, 8]          #
#---------------------------#
# input_2: 44               #
# output_2: [2, 8, 18, 16]  #
#---------------------------#

def list_shells(electrons):
    list_shells = []
    count_electrons = electrons
    index = 1

    while count_electrons > 0:
        shell_capacity = 2 * (index ** 2)
        if shell_capacity < count_electrons:
            list_shells.append(shell_capacity)
        else:
            list_shells.append(count_electrons)
        count_electrons -= shell_capacity
        index += 1
    else:
        return list_shells

print(list_shells(int(input())))
