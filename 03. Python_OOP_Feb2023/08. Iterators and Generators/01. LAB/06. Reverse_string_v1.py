def reverse_text(text: str):
    for numbers in range(-1, -len(text)-1, -1):
        yield text[numbers]

# ##################################
# Test_Code_1:
for char in reverse_text("step"):
    print(char, end='')
# ---------------------------------
# Output_1:
# pets
# ##################################

