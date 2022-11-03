initial_list = input().split()


def list_sorting(list_numbers):
    for first_number in range(len(list_numbers)):

        print(f"Symbol Position: {first_number}")
        print(f"Actual Symbol: {list_numbers[int(first_number)]}")
        for second_number in range(len(list_numbers)):
            if first_number == second_number:
                print(f"Symbol Position L1 {first_number}")
                print(f"Symbol Position L2 {second_number}")
                pass
            else:
                if list_numbers[int(second_number)] > list_numbers[int(first_number)]:
                    print(f"Symbol L2 Bigger: {list_numbers[int(second_number)]}")
                    print(f"Symbol L1 Smaller: {list_numbers[int(first_number)]}")

                    pass
                else:
                    list_numbers[second_number], list_numbers[first_number] = list_numbers[first_number], list_numbers[second_number]
                    print(list_numbers)
    return list_numbers

print(list_sorting(initial_list))
print(initial_list)





