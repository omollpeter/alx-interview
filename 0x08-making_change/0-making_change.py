#!/usr/bin/python3
"""
Contains a function that calculates fewest number of coins needed
to make a change
"""


def makeChange(coins, total):
    """
    Returns fewest number of coins needed to make a change
    """
    if total <= 0:
        return 0
    if type(coins) is not list:
        return -1
    total_coins = 0

    coins.sort(reverse=True)
    while coins:
        if coins[0] > total:
            coins.pop(0)
            continue
        total_coins += total // coins[0]
        total %= coins[0]

    if total:
        return -1
    return total_coins
