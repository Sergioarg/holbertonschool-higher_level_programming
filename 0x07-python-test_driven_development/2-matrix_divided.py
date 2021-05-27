#!/usr/bin/python3


def matrix_divided(matrix, div):
    t_matrix = type(matrix)
    new_matrix = []

    if (t_matrix != list or t_matrix != float):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")
    elif (type(div) != int or type != float):
        raise TypeError("div must be a number")

    for number in matrix:
        new_matrix.append(number / div)
        # if (matrix[numbers] == matrix[numbers]):
        #     raise TypeError("Each row of the matrix must have the same size")

    return matrix
