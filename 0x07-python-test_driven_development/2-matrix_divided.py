#!/usr/bin/python3
"""Module that defines matrix_divided function"""


def matrix_divided(matrix, div):
    """
    function that divide all elements of a matrix

    Args:
        matrix (list): a list of lists of ints or integers
        div (int/float): the divisor
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or (isinstance(element, float)))
            for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")

    if (not all(len(row) == len(matrix[0]) for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
