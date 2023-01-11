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

number_of_conf_rooms = int(input())
count_free_chairs = 0
for conf_room in range(1, number_of_conf_rooms + 1):
    conf_room_attendance = input().split()
    enough_chairs_everywhere = True
    if len(conf_room_attendance[0]) < int(conf_room_attendance[1]):
        enough_chairs_everywhere = False
        print(f"{int(conf_room_attendance[1]) - len(conf_room_attendance[0])} more chairs"
              f" needed in room {conf_room}")
    else:
        count_free_chairs += (abs(len(conf_room_attendance[0]) - int(conf_room_attendance[1])))
if enough_chairs_everywhere == True:
    print(f"Game On, {count_free_chairs} free chairs left")