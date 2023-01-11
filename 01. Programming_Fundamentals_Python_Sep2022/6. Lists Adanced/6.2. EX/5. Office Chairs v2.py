#-------------------------------------------#
# input_1:                                  #
#           4                               #
#           XXXX 4                          #
#           XX 1                            #
#           XXXXXX 3                        #
#           XXX 3                           #
# output_1: Game On, 4 free chairs left     #
#-------------------------------------------#
# input_2:                                  #
#           3                               #
#           XXXXXXX 5                       #
#           XXXX 5                          #
#           XXXXXX 8                        #
# output_2:                                 #
#           1 more chairs needed in room 2  #
#           2 more chairs needed in room 3  #
#-------------------------------------------#

def conf_room_control(total_number_conf_rooms):
    count_free_chairs = 0
    count_chairs_needed = 0
    for room in range(1, total_number_conf_rooms + 1):
        chairs, attendants = input().split(" ")
        balance = len(chairs) - int(attendants)
        if balance >= 0:
            count_free_chairs += balance
        else:
            count_chairs_needed += abs(balance)
            print(f"{abs(balance)} more chairs needed in room {room}")
    return count_free_chairs, count_chairs_needed

number_of_conf_rooms = int(input())
available_free_chairs, necessary_chairs = conf_room_control(number_of_conf_rooms)
if available_free_chairs >= necessary_chairs:
    print(f"Game On, {available_free_chairs} free chairs left")

