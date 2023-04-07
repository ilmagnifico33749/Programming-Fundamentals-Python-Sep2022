def print_message(message):
    def message_sender():
        # "Nested Fuction"
        print(message)
    message_sender()

print_message("Some random message")
