#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    return result_matrix
