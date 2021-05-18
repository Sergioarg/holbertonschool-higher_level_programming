#!/usr/bin/pyhon3
def safe_print_list(my_list=[], x=0):
    try:
        lenght = 0
        for i in range(x):
            print('{}'.format(my_list[i]), end="")
            lenght = lenght + 1
        print("")
    except IndexError:
        print("")
    return lenght

