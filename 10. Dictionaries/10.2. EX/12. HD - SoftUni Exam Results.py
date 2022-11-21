my_dict_exam = {'Languages': []}

command = input()
while command != "exam finished":
    if "banned" not in command:
        command_details = command.split("-")
        current_username = command_details[0]
        current_language = command_details[1]
        current_points = int(command_details[2])
        banned = False
        found = False
        for key in my_dict_exam['Languages']:
            if current_language in key:
                found = True
                key[current_language] += 1
                break
        if found is not True:
            my_dict_exam['Languages'].append({current_language: 1})
        if current_username not in my_dict_exam.keys():
            my_dict_exam[current_username] = [{current_language: current_points}, {'Banned': banned}]
        elif current_username in my_dict_exam.keys():
            lang_present = False
            for data in my_dict_exam[current_username]:
                if current_language in data:
                    lang_present = True
                    if data[current_language] < current_points:
                        data[current_language] = current_points
                    break
            if lang_present is not True:
                my_dict_exam[current_username].append({current_language: current_points})
    else:
        command_details = command.split("-")
        current_username = command_details[0]
        for data in my_dict_exam[current_username]:
            if 'Banned' in data:
                data['Banned'] = True
    command = input()

else:
    print(f"Results: ")
    for person in my_dict_exam:
        if person != 'Languages':
            banned_status = False
            for item in (my_dict_exam[person]):
                item_dict = item
                for key, value in item.items():
                    if key == 'Banned':
                        banned_status = value
            if banned_status is False:
                for item in (my_dict_exam[person]):
                    for key, value in item.items():
                        if key != 'Banned':
                            print(f"{person} | {value}")
    print(f"Submissions:")
    for language in my_dict_exam['Languages']:
        for key, value in language.items():
            print(f"{key} - {value}")

# -----------------#
# Peter-Java-84
# George-C#-84
# George-C#-70
# Katy-C#-94
# exam finished
# -----------------#
# Peter-Java-91
# George-C#-84
# Katy-Java-90
# Katy-C#-50
# Katy-banned
# exam finished
# -----------------#

