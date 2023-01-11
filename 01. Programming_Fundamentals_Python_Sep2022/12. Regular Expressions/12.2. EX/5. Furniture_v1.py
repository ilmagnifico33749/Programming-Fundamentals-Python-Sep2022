import re

command = input()

regex = "(>>[a-zA-Z]+<<[0-9]+[.|,]*[0-9]*![0-9]+)"

while command != "Purchase":
     matches = re.findall(regex, command)

    command = input()

else:
    print()


# valid_format = ">>{furniture_name}<<{price}!{quantity}



##############################
Input 1:
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase
##############################
Output 1:
Bought furniture:
Sofa
TV
Total money spend: 2436.69
##############################
