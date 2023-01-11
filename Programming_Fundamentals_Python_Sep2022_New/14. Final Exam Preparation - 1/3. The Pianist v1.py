number_of_pieces = int(input())
collection = {}

for piece in range(number_of_pieces):
    piece_info = input()
    piece_info_details = piece_info.split("|")
    piece_name = piece_info_details[0]
    piece_composer = piece_info_details[1]
    piece_key = piece_info_details[2]

    collection[piece_name] = {piece_composer: piece_key}

command = input()

while command != "Stop":
    command_details = command.split("|")
    action = command_details[0]
    piece_name = command_details[1]

    if action == "Add":
        composer = command_details[2]
        piece_key = command_details[3]
        if piece_name in collection.keys():
            print(f"{piece_name} is already in the collection!")
        else:
            collection[piece_name] ={composer: piece_key}
            print(f"{piece_name} by {composer} in {piece_key} added to the collection!")

    elif action == "Remove":
        if piece_name not in collection.keys():
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
        else:
            del collection[piece_name]
            print(f"Successfully removed {piece_name}!")

    elif action == "ChangeKey":
        new_key = command_details[2]
        if piece_name in collection.keys():
            for key in collection[piece_name].keys():
                collection[piece_name][key] = new_key
                print(f"Changed the key of {piece_name} to {new_key}!")
        else:
            print(f"Invalid operation1 {piece_name} does not exist in the collection.")

    command = input()

else:
    # In one file there is a condition to sort by name of the piece:
    # for pieces in sorted(collection.keys()):
    #     for details in collection[pieces]:
    #         print(f"{pieces} -> Composer: {details}, Key: {collection[pieces][details]}")
    # # In one file there is a condition to sort by name of the composer:
    #     #To adapt the below in the relevant manner
    #     new_list = []
    #     for one, two in my_dict.items():
    #         for key, value in two.items():
    #             print(key)
    #             print(value)
    #             new_list.append(f"{key} - {one} - {value}")
    #
    #     for song in sorted(new_list):
    #         song_details = song.split(" - ")
    #         print(f"{song_details[1]} -> {song_details[0]} -> {song_details[2]}")
    # # And there is also Word file in Judge with condition to just print the content of the dict
    # # without any sorting.
    for piece, info in collection.items():
        for composer, key in info.items():
            print(f"{piece} -> Composer: {composer}, Key: {key}")


# ----------------------------------------#
# ----------------------------------------#
# 4
# Eine kleine Nachtmusik|Mozart|G Major
# La Campanella|Liszt|G# Minor
# The Marriage of Figaro|Mozart|G Major
# Hungarian Dance No.5|Brahms|G Minor
# # ----------------------------------------#
# Add|Spring|Vivaldi|E Major
# Remove|The Marriage of Figaro
# Remove|Turkish March
# ChangeKey|Spring|C Major
# Add|Nocturne|Chopin|C# Minor
# Stop
# ----------------------------------------#
# ----------------------------------------#
# 3
# Fur Elise|Beethoven|A Minor
# Moonlight Sonata|Beethoven|C# Minor
# Clair de Lune|Debussy|C# Minor
# ----------------------------------------#
# Add|Sonata No.2|Chopin|B Minor
# Add|Hungarian Rhapsody No.2|Liszt|C#
# Minor
# Add|Fur Elise|Beethoven|C# Minor
# Remove|Clair de Lune
# ChangeKey|Moonlight Sonata|C# Major
# Stop
# ----------------------------------------#
# ----------------------------------------#
