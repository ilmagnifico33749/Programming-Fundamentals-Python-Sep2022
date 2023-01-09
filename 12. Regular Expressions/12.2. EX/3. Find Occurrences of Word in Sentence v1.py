import re

sentence = input()
# sentence = "There was one. Therefore I bought it. I wouldn't buy it otherwise."
word = input()
# word = "there"

regex = fr"\b{word}\b"

match = re.findall(regex, sentence, re.I)

print(len(match))

#############################################################################
# Input 1:
# The waterfall was so high, that the child couldn't see its peak.
# the
#
# Output 1:
# 2
#############################################################################
# Input 2:
# How do you plan on achieving that? How? How can you even think of that?
# how
#
# Output 2:
# 3
#############################################################################
# Input 3:
# There was one. Therefore I bought it. I wouldn't buy it otherwise.
# there
#
# Output 3:
# 1
#############################################################################
