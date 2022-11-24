original_word = input()
new_word = ""
strength = 0
for index in range(len(original_word)):
    if strength > 0 and original_word[index] != ">":
        strength -= 1
    elif original_word[index] == ">":
        new_word += original_word[index]
        strength += int(original_word[index + 1])
    else:
        new_word += original_word[index]
print(new_word)

# input: abv>1>1>2>2asdasd
# output: abv>>>>dasd

#Write a program that reads a string from the console that contains:
# · Explosions marked with '>'
# · Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# · Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
# When all characters are processed, print the final string.





