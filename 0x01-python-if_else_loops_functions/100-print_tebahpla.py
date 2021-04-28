#!/usr/bin/python3
toggle_upper = False
r_letters = 123
while (r_letters >= 98):
    r_letters -= 1
    if (toggle_upper):
        print('{:c}'.format(r_letters - 32), end="")
    else:
        print('{:c}'.format(r_letters), end="")
    toggle_upper = not toggle_upper
