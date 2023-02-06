def whatever_func(list_numbers):
    print(list_numbers)
    print(*list_numbers)

    def sum_negative(*args):
        sum_negative_numbers = sum([abs(int(x)) for x in list_numbers if int(x) < 0])
        return sum_negative_numbers

    def sum_positive(*args):
        sum_positive_numbers = sum([int(x) for x in list_numbers if int(x) > 0])
        return sum_positive_numbers

    def comparison_sums():
        if sum_positive() < sum_negative():
            return f"The negatives are stronger than the positives"
        else:
            return f"The positives are stronger than the negatives"

    print(f"{-sum_negative(list_numbers)}\n{sum_positive(list_numbers)}\n{comparison_sums()}")


whatever_func(input().split(" "))

# ##############################################
# Input_1:
# 1 2 -3 -4 65 -98 12 57 -84
# ----------------------------------------------
# Output_1:
# -189
# 137
# The negatives are stronger than the positives
# ##############################################
# Input_2:
# 1 2 3
# ----------------------------------------------
# Output_2:
# 0
# 6
# The positives are stronger than the negatives
# ##############################################
