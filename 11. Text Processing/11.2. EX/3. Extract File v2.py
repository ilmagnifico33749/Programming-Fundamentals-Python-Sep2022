def file_name_ext(file_path):
    file_path_details = file_path.split("\\")
    file_details = file_path_details[(len(file_path_details)) - 1].split(".")
    return f"File name: {file_details[0]}\nFile extension: {file_details[1]}"

print(file_name_ext(input()))

# C:\Internal\training-internal\Template.pptx