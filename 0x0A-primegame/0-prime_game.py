#!/usr/bin/python3
"""
Contains a function that implements Prime Game
"""


def sieve_of_eratosthenes(max_n):
    """
    Returns an array where prime[i] is True if i is a prime number,
    False otherwise.
    Uses the Sieve of Eratosthenes to identify primes.
    """
    prime = [True] * (max_n + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, max_n + 1, i):
                prime[j] = False
    return prime


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.
    Maria plays first, and both players play optimally.

    Parameters:
    - x: number of rounds
    - nums: list of integers where each number represents
      the size of the set for that round

    Returns:
    - Name of the player that won the most rounds ("Maria" or "Ben")
    - None if the winner cannot be determined (tie)
    """
    if x < 1 or not nums:
        return None

    # Find the maximum number in nums to optimize the sieve
    max_n = max(nums)

    # Step 1: Generate all primes up to max_n using the sieve
    prime = sieve_of_eratosthenes(max_n)

    # Step 2: Precompute the number of prime removals for each number of rounds
    prime_counts = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if prime[i] else 0)

    # Step 3: Simulate the game for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # The number of moves is equal to the number of primes <= n
        if prime_counts[n] % 2 == 0:
            ben_wins += 1  # Ben wins if the number of primes is even
        else:
            maria_wins += 1  # Maria wins if the number of primes is odd

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
