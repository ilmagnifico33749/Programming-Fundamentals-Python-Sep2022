import re

phone_nums = input()
regex_1 = "(\+359[-{1}][2]{1}[-{1}][0-9]{3}[-{1}][0-9]{4}|\+359[\s{1}][2]{1}[\s{1}][0-9]{3}[\s{1}][0-9]{4})\\b"
filtered_1 = re.findall(regex_1, phone_nums)
print(', '.join(filtered_1))