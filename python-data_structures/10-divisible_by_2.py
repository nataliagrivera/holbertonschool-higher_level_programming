#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list == []:
        return None

    new_list = my_list.copy()
    result = []

    for i in range(len(new_list)):
        if new_list[i] % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
