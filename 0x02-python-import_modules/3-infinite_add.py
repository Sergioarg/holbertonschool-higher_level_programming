#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    count = len(sys.argv)
    if (count == 1):
        print("0")
    for number in range(1, count):
        add += int(sys.argv[number])
    print('{:d}'.format(add))
