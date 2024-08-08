#!/usr/bin/python3
"""
Contains the following function definition
    minOperations - Returns the the number of minimum operations
                    for completing a task
"""


def minOperations(n):
    """
    Returns the the number of minimum operations
    for completing a task
    """
    operations = 0
    initial = n

    while n > 1:
        divisor = 2

        while n % divisor:
            divisor += 1
            if divisor == initial:
                return operations
        operations += divisor
        n = n / divisor

    return operations
