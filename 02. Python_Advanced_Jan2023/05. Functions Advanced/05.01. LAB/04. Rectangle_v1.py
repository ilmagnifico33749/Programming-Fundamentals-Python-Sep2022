def rectangle(length, width):

    if isinstance(length, int) is False or isinstance(width, int) is False:
        return "Enter valid values!"

    def area():
        result = length * width
        return result

    def perimeter():
        result = 2 * (length + width)
        return result

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


# ##########################
# Test_Code_1:
# print(rectangle(2, 10))
# --------------------------
# Output_1:
# Rectangle area: 20
# Rectangle perimeter: 24
# ###
# Test_Code_2:
# print(rectangle('2', 10))
# rectangle('2', 10)
# --------------------------
# Output_2:
# "Enter valid values!"
# ##########################
