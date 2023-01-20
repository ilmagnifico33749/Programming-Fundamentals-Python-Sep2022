intersections_num = int(input())

longest_intersections_len = 0
longest_intersections_tuple = ()

for intersections in range(intersections_num):
    intersections = input().split("-")
    intersection_1 = intersections[0].split(",")
    set_intersection_1 = set([x for x in range(int(intersection_1[0]), ((int(intersection_1[1])+1)))])
    intersection_2 = intersections[1].split(",")
    set_intersection_2 = {x for x in range(int(intersection_2[0]), ((int(intersection_2[1])+1)))}
    sets_intersection = set_intersection_1.intersection(set_intersection_2)
    if len(sets_intersection) > longest_intersections_len:
        longest_intersections_len = len(sets_intersection)
        longest_intersections_tuple = sets_intersection

print(f"Longest intersection is [{', '.join(map(str, longest_intersections_tuple))}] with length {longest_intersections_len}")

# ###################################################################
# Input_1:
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
# -------------------------------------------------------------------
# Output_1:
# Longest intersection is [6, 7, 8, 9, 10] with length 5
# ###################################################################
# Input_2:
# 5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11
# -------------------------------------------------------------------
# Output_2:
# Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9
# ###################################################################
