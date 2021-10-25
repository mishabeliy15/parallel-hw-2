from collections import defaultdict


def eratosthenes(n: int) -> list:
    numbers = list(range(n + 1))
    numbers[1] = 0
    for i in numbers:
        if i > 1:
            for j in range(i + i, len(numbers), i):
                numbers[j] = 0
    return list(filter(lambda x: x != 0, numbers))


def factorize(number: int, primes: list = None) -> dict:
    res = defaultdict(lambda: 0)
    if primes is None:
        primes = eratosthenes(number)
    for prime in primes:
        if number < 2:
            break
        while number % prime == 0:
            res[prime] += 1
            number /= prime
    return res
