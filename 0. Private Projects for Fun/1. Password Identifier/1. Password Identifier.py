print(chr(4))
print(ord('a'))

user_password = "Hello There"
user_input = input()
password_min_length = 4

while user_input != user_password:
    len_password_to_generate = password_min_length
    password_to_generate = [0 for x in range(len_password_to_generate)]
    generated_password = password_to_generate
    print(password_to_generate)
    symbol_value_ascii = 0
    for symbol in range(len(generated_password)):
        current_symbol_password = generated_password[symbol]
        new_symbol_password = ""
        symbol_value = generated_password[symbol]
        print(symbol_value)


    user_input = input()
    len_password_to_generate += 1
else:
    print(f"The User's Password is: {user_password}")
