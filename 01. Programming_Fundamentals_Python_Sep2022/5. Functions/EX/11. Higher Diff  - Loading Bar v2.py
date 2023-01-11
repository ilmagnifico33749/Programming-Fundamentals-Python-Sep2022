user_input = int(input())

def progress_visualisation(progress):
    return f"[{int(int(progress)*0.1) * '%'}{(10 - int(int(progress)*0.1)) * '.'}]"

def loading_bar(progress, visualisation):
    if progress == 100:
        return f"{progress}% Complete!\n{visualisation}"
    else:
        return f"{progress}% {visualisation}\nStill loading..."

print(loading_bar((user_input), progress_visualisation(user_input)))

