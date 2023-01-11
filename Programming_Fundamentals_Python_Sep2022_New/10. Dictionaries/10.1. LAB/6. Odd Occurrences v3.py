list_commands = input().lower().split(" ")
my_dictionary = {}
for command in list_commands:
    if list_commands.count(command) % 2 != 0:
        my_dictionary[command] = list_commands.count(command)
print(" ".join(my_dictionary.keys()))

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
