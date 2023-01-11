list_commands = input().split(" ")
my_dictionary = {}
for command in list_commands:
    command_low_c = command.lower()
    if command_low_c not in my_dictionary:
        my_dictionary[command_low_c] = 1
    else:
        my_dictionary[command_low_c] += 1
for (key,value) in my_dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")

#-------------------------------------------#
# input_1: Java C# PHP PHP JAVA C java      #
# output_1: java c# c                       #
#-------------------------------------------#
# input_2: 3 5 5 hi pi HO Hi 5 ho 3 hi pi   #
# output_2: 5 hi                            #
#-------------------------------------------#
# input_3: a a A SQL xx a xx a A a XX c     #
# output_3: a sql xx c                      #
#-------------------------------------------#
