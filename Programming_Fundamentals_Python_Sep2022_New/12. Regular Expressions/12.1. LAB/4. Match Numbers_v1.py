import re

sequence = input()
# sequence = "1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5 00.5"

regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

filtered = re.finditer(regex, sequence)

for match in filtered:
    print(match.group(), end=" ")
