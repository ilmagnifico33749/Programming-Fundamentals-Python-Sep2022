### Initial_Code_with_Errors_To_Redact
# numbers_dictionary = {}
#
# line = input()
#
# while line != "Search":
#     number_as_string = line
#     number = int(input())
#     numbers_dictionary[number_as_string] = number
#
# line = input()
#
# while line != "Remove":
#     searched = line
#     print(numbers_dictionary[searched])
#
# line = input()
# while line != "End":
#     searched = line
#     del numbers_dictionary[searched]
#
# print(numbers_dictionary)
### ----------------------------------
### Redacted_Code:
numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()


line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()


line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()


print(numbers_dictionary)


# #######################################
# Input_1:
# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End
# ---------------------------------------
# Output_1:
# 1
# {'one': 1}
# #######################################
# Input_2:
# one
# two
# Search
# Remove
# End
# ---------------------------------------
# Output_2:
# The variable number must be an integer
# {}
# #######################################
# Input_3:
# one
# 1
# Search
# one
# Remove
# two
# End
# ---------------------------------------
# Output_3:
# 1
# Number does not exist in dictionary
# {'one': 1}
# #######################################
