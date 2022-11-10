number_of_conf_rooms = int(input())
count_free_chairs = 0
for conf_room in range(number_of_conf_rooms):
    conf_room_attendance = input().split()
    print(len(conf_room_attendance[0]))
    count_free_chairs += abs(len(conf_room_attendance[0]) - int(conf_room_attendance[1]))
    print(conf_room_attendance)
    print(count_free_chairs)