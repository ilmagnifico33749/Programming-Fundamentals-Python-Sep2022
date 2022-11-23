string_1 = str(input())
string_2 = str(input())
final_sum = 0

if len(string_1) > len(string_2):
    for symbol in range(len(string_2)):
        final_sum += ord(string_1[symbol]) * ord(string_2[symbol])
    for symbol in range((len(string_2)), len(string_1)):
        final_sum += ord(string_1[symbol])
elif len(string_2) > len(string_1):
    for symbol in range(len(string_1)):
        final_sum += ord(string_2[symbol]) * ord(string_1[symbol])
    for symbol in range((len(string_1)), len(string_2)):
        final_sum += ord(string_2[symbol])
else:
    for symbol in range(len(string_1)):
        final_sum += ord(string_1[symbol]) * ord(string_2[symbol])

print(final_sum)

# # input: George Peter -> output: 52114
# # input: 123 522 -> output: 7647
# # input: a aaaa -> output: 9700

# print(ord(symbol_1))
