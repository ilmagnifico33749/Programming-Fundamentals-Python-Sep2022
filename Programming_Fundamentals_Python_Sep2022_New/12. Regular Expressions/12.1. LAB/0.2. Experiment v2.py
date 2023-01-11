import re

command = ">>Sofa<< 312.23!3"

regex = "(>>[a-zA-Z]+<<[0-9]+[.|,]*[0-9]*![0-9]+)"

matches = re.findall(regex, command)

print(matches)

# valid_format = ">>{furniture_name}<<{price}!{quantity}


##############################
# Input
# 1:
# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase
# ##############################
# Output
# 1:
# Bought furniture:
# Sofa
# TV
# Total
# money
# spend: 2436.69
##############################
