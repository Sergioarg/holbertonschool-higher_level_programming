#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    count = len(sys.argv)
    for number in range(1, count):
        add += int(sys.argv[number])
    print('{:d}'.format(add))
