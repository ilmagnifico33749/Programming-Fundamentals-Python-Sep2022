
command = input()
while command != "end":
    word_reversed = ""
    for symbol in reversed(command):
        word_reversed += symbol
    print(command + " = " + word_reversed)
    command = input()