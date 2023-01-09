import re

sentence = input()
# sentence = "__invalidVariable _evenMoreInvalidVariable_ _validVariable"
regex = r"\b_([A-Za-z0-9]+)\b"

matches = re.findall(regex, sentence)

print(','.join(matches))
# print(matches)

################################################################
# Input 1:
# The _id and _age variables are both integers.
#
# Output 1:
# id,age
################################################################
# Input 2:
# Calculate the _area of the _perfectRectangle object.
#
# Output 2:
# area,perfectRectangle
################################################################
# Input 3:
# __invalidVariable _evenMoreInvalidVariable_ _validVariable
#
# Output 3:
# validVariable
################################################################
