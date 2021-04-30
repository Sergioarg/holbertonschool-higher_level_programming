#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    # Declarete distionarie whit functions
    operator = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    # Get the len of argvs
    count = len(sys.argv)
    argv = (sys.argv)
    if (count != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    # Take the arguments to make the opceracion
    elif (operator.get(argv[2]) == (None)):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        r = operator.get(str(argv[2]))(int(argv[1]), int(argv[3]))
        print('{:s} {:s} {:s} = {:d}'.format(argv[1], argv[2], argv[3], r))
        exit(0)
