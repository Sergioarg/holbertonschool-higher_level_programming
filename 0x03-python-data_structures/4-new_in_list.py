#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if my_list:
        if (idx < 0 or idx >= len(my_list)):
            return (new_list)

        for i in range(0, len(my_list)):
            if (idx != i):
                new_list.append(my_list[i])
            else:
                new_list.append(element)
    return (new_list)
