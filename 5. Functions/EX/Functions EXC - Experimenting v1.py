initial_list = input().split(" ")

for first_number in range(len(initial_list)):

    print(f"Symbol Position: {first_number}")
    print(f"Actual Symbol: {initial_list[int(first_number)]}")
    for second_number in range(len(initial_list)):
        if first_number == second_number:
            print(f"Symbol Position L1 {first_number}")
            print(f"Symbol Position L2 {second_number}")
            pass
        else:
            if initial_list[int(second_number)] > initial_list[int(first_number)]:
                print(f"Symbol L2 Bigger: {initial_list[int(second_number)]}")
                print(f"Symbol L1 Smaller: {initial_list[int(first_number)]}")

                pass
            else:
                initial_list[second_number], initial_list[first_number] = initial_list[first_number], initial_list[
                    second_number]
                print(initial_list)








