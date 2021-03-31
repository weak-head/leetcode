import math


def countPrimes(n):
    """
    Sieve of Eratosthenes

    Time: O(n * log log n)
    Space: O(n)
    """
    if n < 3:
        return 0

    primes = [True] * n
    primes[0] = primes[1] = False

    for num in range(2, int(math.sqrt(n)) + 1):
        if primes[num]:
            for multiple in range(num * num, n, num):
                primes[multiple] = False

    return sum(primes)
