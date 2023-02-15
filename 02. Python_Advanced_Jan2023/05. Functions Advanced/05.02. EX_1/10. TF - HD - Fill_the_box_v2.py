
def fill_the_box(height, length, width, *args):
    boxes_to_fit = list(args)[:list(args).index("Finish")]
    total_size_boxes_to_fit = sum(boxes_to_fit)
    box_size = height * length * width

    def filling_the_box(box_size, total_size_boxes_to_fit):
        box_size -= 1
        if total_size_boxes_to_fit == 0:
            if box_size < 0:
                return f"No more free space! You have {abs(box_size)} more cubes."
            else:
                return f"There is free space in the box. You could put {box_size} more cubes."
        else:
            return filling_the_box(box_size, total_size_boxes_to_fit-1)

    return filling_the_box(box_size, total_size_boxes_to_fit-1)


# ##############################################################
# Test_Code_1:
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# --------------------------------------------------------------
# Output_1:
# There is free space in the box. You could put 13 more cubes.
# ##############################################################
# Test_Code_2:
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# --------------------------------------------------------------
# Output_2:
# No more free space! You have 17 more cubes.
# ##############################################################
# Test_Code_3:
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
# --------------------------------------------------------------
# Output_3:
# There is free space in the box. You could put 960 more cubes.
# ##############################################################
