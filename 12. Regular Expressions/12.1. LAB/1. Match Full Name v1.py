import re

names = input()

regex = "(\\b[A-Z]{1}[a-z]{2}[a-z]*\s{1}[A-Z]{1}[a-z]{2}[a-z]+\\b)"
matches = re.findall(regex, names)
print(matches)
print(" ".join(matches))

# --------------------------------------------------------------------------------------------------#
# Input_1: Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett
# Output_1: Peter Smith Lily Everet
# --------------------------------------------------------------------------------------------------#
