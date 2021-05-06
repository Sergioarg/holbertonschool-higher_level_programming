#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if my_list:
        if (idx < 0):
            return (new_list)

        if (idx >= len(my_list)):
            return (new_list)

        for i in range(len(my_list)):
            if (i == idx):
                new_list.append(element)
            else:
                new_list.append(my_list[i])
    return (new_list)
