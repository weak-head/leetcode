def consecutiveNumbersSum(N: int) -> int:
    """

        N = (x + 1) + (x + 2) + .. + (x + k)
        N = kx + k(k + 1)/2
        N * 2 = k(2x + k + 1), where k >= 1, x >= 0

        The problem is to figure out all possible pairs of 'k' and '2x + k + 1'
        which are both divisors of a number 'N * 2'.

        Either 'k' or '2x + k + 1' is odd.
        So, for each odd factor of 'N' we can find the consecutive number solution.

        If N = 3^a * 5^b * 7*c * 11*d * ..
        the number of factors that N has equals
        N_factors = (a + 1) * (b + 1) * (c + 1) * (d + 1) * ..

        Explanantion:
            Discard all factors 2 from N.
            Check all odd number 'i' if 'N' is divided by 'i'.
            Calculate the count of factors 'i' that N has.
            Update [res *= count].
            If N==1, we have found all primes and just return res.
            Otherwise, N will be equal to P and we should do res *= count + 1 where count = 1.

    Time: O(P)
    Space: O(1)
        P - biggest prime factor
    """
    res = 1
    i = 3

    # Discard all factors of 2 from N
    while N % 2 == 0:
        N /= 2

    # For all odd numbers from 3 to N
    while i * i <= N:
        count = 0

        # Reduce 'N' by 'i'
        while N % i == 0:
            N /= i
            count += 1

        res *= count + 1
        i += 2

    return res if N == 1 else res * 2
