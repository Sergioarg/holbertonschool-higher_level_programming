#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print('{:d}'.format(row[i]),
                  end=' ' if not (i is len(row) - 1) else '')
        print()
