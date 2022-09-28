number_of_messages_sent = int(input())

for m in range(number_of_messages_sent):
    message = int(input())
    if message == 88:
        print("Hello")
    elif message == 86:
        print("How are you?")
    elif message != 88 and message != 86 and message <88:
        print("GREAT!")
    elif message > 86:
        print("Bye.")


