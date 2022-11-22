def validity_check(user_input):
    command_details = user_input.split(", ")

    def symbol_validity(word):
        for symbol in word:
            validity = False
            if symbol.isalnum() is True or symbol == "-" or symbol == "_":
                validity = True
            else:
                validity = False
                break
        if validity is True:
            print(word)

    def longitude_check(username):
        if 3 <= len(username) <= 16:
            symbol_validity(username)

    for username in command_details:
        longitude_check(username)

validity_check(input())

# sh, too_long_username, !lleg@l ch@rs, jeffputt
# Jeff, john45, ab, cd, peter-ivanov, @smith