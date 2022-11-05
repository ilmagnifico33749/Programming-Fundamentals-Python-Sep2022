# MyPass123

user_input = int(input())

def progress_visualisation(progress):
    if progress == 100:

        return f"[{(int(progress*0.1)) * '%'}]"

print(progress_visualisation(user_input))