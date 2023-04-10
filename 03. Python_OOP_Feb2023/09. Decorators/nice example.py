

def printing_function(function):
    divider_1, divider_2 = function(int(input("Divider_1: ")), int(input("Divider_2: ")))
    divider_3 = int(input("Divider_3: "))

    def wrapper(user_input_text, user_input_number):

        # return function().upper()
        print(user_input_text.upper())
        print(user_input_number / divider_1)
        print(user_input_number / divider_2)
        print(user_input_number / divider_3)

    return wrapper


@printing_function
def printing_text(text, number):
    return text, number

# "Hello there!"

printing_text(str(input("Text:")), int(input("Number: ")))
