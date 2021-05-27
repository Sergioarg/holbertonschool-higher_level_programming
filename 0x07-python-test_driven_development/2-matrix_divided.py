#!/usr/bin/python3
"""Module to divide numbers of souble matrix"""


def matrix_divided(matrix, div):
    """Function to divide the numbers of matrix"""
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
