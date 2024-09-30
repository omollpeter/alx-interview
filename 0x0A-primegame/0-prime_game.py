#!/usr/bin/python3
"""
Contains a function that implements Prime Game
"""


def prime_number_picker(nums):
    """
    Returns the first prime number in an array
    """
    for n in nums:
        if n == 1:
            continue
        if n == 2:
            return 2
        divisor = 2
        while divisor <= n // 2:
            if n % divisor == 0:
                break
            divisor += 1
        else:
            return n
        return 0


def multiples_remover(number, nums):
    """
    Removes multiples of number from an array nums
    """
    for num in nums:
        if num % number == 0:
            nums.remove(num)
    return nums


def isWinner(x, nums):
    """
    Returns the winner in a Prime game
    """
    win_counts = {
        "Maria": 0,
        "Ben": 0
    }

    for i in range(x):
        for num in nums:
            player = "Maria"
            game_array = list(range(1, num + 1))

            while game_array:
                prime = prime_number_picker(game_array)
                if prime:
                    game_array = multiples_remover(prime, game_array)
                    player = "Ben" if player == "Maria" else "Maria"
                else:
                    if player == "Maria":
                        win_counts["Ben"] += 1
                    else:
                        win_counts["Maria"] += 1
                    break
    return max(win_counts, key=win_counts.get)
