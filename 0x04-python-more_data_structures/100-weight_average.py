#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum = 0
        for sub in my_list:
            for i in sub:
                sum = sum + i
        res = sum / len(my_list)
        return (res)
