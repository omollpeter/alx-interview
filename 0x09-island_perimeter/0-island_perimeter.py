#!/usr/bin/python3
"""
Contains a function that calculates island perimeter
"""


def island_perimeter(grid):
    """
    Returns perimeter of an island represented by list of lists
    containing 0s and 1s only
    """
    perimeter = 0

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j]:
                if not grid[i - 1][j]:
                    perimeter += 1
                if not grid[i][j - 1]:
                    perimeter += 1
                if not grid[i][j + 1]:
                    perimeter += 1
                if not grid[i + 1][j]:
                    perimeter += 1
                if not grid[i][j + 1]:
                    break

    return perimeter
