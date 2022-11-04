# logIn
# MyPass123
# Pa$s$s

user_input = input()

def condition_one(password):
    Validity = False
    if 6 <= len(password) <= 10:
        Validity = True
    if Validity == False:
        print(f"Password must be between 6 and 10 characters")
    return Validity

def condition_two(password):
    Validity = False
    count_wrong_symbols = 0
    for symbol in password:
        if 48 <= ord(symbol) <= 57 or 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122:
            continue
        else:
            count_wrong_symbols += 1
    if count_wrong_symbols == 0:
        Validity = True
    else:
       Validity == False
       print(f"Password must consist only of letters and digits")
    return Validity

def condition_three(password):
    Validity = False
    count_digits = 0
    count_wrong_symbols = 0
    for symbol in password:
        if 48 <= ord(symbol) <= 57:
            count_digits += 1
    if count_digits >= 2:
        Validity = True
    if Validity == False:
        print(f"Password must have at least 2 digits")
    return Validity

def password_validator(cond_1, cond_2, cond_3):
    password_validity = False
    if cond_1 == True and cond_2 == True and cond_3 == True:
        password_validity = True
    if password_validity == True:
        print("Password is valid")

password_validator(condition_one(user_input), condition_two(user_input), condition_three(user_input))
