#-------------#
# 3           #
# cute        #
# adorable    #
# cute        #
# charming    #
# smart       #
# clever      #
#-------------#
# 2           #
# task        #
# problem     #
# task        #
# assignment  #
#-------------#

number_of_words = int(input())
dict_synon = {}
list_all_words = []

for times in range(number_of_words * 2):
    word = str(input())
    list_all_words.append(word)

for word in range(0, len(list_all_words), 2):
    key = str(list_all_words[word])
    value = str(list_all_words[word + 1])
    if key in dict_synon.keys():
        dict_synon[key] += ", "
        dict_synon[key] += value
    else:
        dict_synon[key] = value

for keys in dict_synon.keys():
    print(f"{keys} - {dict_synon[keys]}")
