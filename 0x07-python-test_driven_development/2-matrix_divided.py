#!/usr/bin/python3
"""Module to divide numbers of souble matrix"""


def matrix_divided(matrix, div):
    """Function to divide the numbers of matrix"""
    new_matrix = []

    if type(matrix) != list or type(matrix[0]) != list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")

    for n_rows in matrix:
        if (type(n_rows) != list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if (len(n_rows) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        new_values = []

        for values in n_rows:
            if not (type(values) == int or type(values) == float):
                raise_msg = " "
                raise TypeError("matrix must be a matrix" +
                                "(list of lists) of integers/floats")
            new_values.append(round(values/div, 2))
        new_matrix.append(new_values)

    return new_matrix
