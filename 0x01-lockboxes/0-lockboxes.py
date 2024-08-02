#!/usr/bin/python3
"""
This module contains the following function:
    canUnlockAll - Returns true if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Returns true if all boxes can be unlocked
    """
    n = len(boxes)
    # Track all unlocked boxes
    unlocked = [False] * n
    # The first box is unlocked
    unlocked[0] = True

    # Start with the first box
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    return all(unlocked)
