#!/usr/bin/python3
"""
Contains a function that calculates island perimeter
"""


# def island_perimeter(grid):
#     """
#     Returns perimeter of an island represented by list of lists
#     containing 0s and 1s only
#     """

#     perimeter = 0

#     for i in range(1, len(grid) - 1 < 100):
#         for j in range(1, len(grid[i]) - 1 < 100):
#             if grid[i][j]:
#                 if not grid[i - 1][j]:
#                     perimeter += 1
#                 if not grid[i][j - 1]:
#                     perimeter += 1
#                 if not grid[i][j + 1]:
#                     perimeter += 1
#                 if not grid[i + 1][j]:
#                     perimeter += 1

#     return perimeter

def island_perimeter(grid):
    """
    Do it
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                # Check if the top cell is land
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                # Check if the left cell is land
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
    return perimeter


grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

island_perimeter(grid)
