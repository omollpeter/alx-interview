#!/usr/bin/python3
"""
This module contains a function that returns Pascals triangle
"""


def pascal_triangle(n):
    """
    Returns pascals triangle
    """
    if n <= 0:
        return []
    i = 0
    pscl_triangle = []
    pascals = []

    while i < n:
        if i == 0:
            pascals = [1]
            pscl_triangle.append(pascals)
            i += 1
        elif i == 1:
            pascals = [1, 1]
            pscl_triangle.append(pascals)
            i += 1
        else:
            new_list = [1]
            for j in range(len(pascals)):
                if j + 1 == len(pascals):
                    new_list.append(1)
                    break
                next = pascals[j] + pascals[j + 1]
                new_list.append(next)
            pascals = new_list
            pscl_triangle.append(pascals)
            i += 1
    return pscl_triangle
