user_input = input()
path_details = user_input.split("\\")
file_details = ""
for word in range(len(path_details)):
    if word == (len(path_details) - 1):
        print(path_details[word])
        file_details = path_details[word].split(".")

print(f"File name: {file_details[0]}\nFile extension: {file_details[1]}")

# C:\Internal\training-internal\Template.pptx