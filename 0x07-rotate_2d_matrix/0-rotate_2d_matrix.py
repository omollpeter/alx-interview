#!/usr/bin/python3
"""
Contains function that transposes a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Transposes and displays a 2D n*n matrix
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()
