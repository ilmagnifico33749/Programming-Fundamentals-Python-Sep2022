import re

names = input()

# regex = "(\\b[A-Z]{1}[a-z]{2}[a-z]* [A-Z]{1}[a-z]{2}[a-z]+\\b)"
# ^50/100 points in Judge but perfect output
regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
# ^100/100 points in Judge
matches = re.findall(regex, names)
print(" ".join(matches))


# --------------------------------------------------------------------------------------------------#
# Input_1: Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett
# Output_1: Peter Smith Lily Everet
# --------------------------------------------------------------------------------------------------#
# Input_1: Ivan Ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Test Testov, Ivan	Ivanov
# Output_1:Ivan Ivanov Test Testov
# --------------------------------------------------------------------------------------------------#
