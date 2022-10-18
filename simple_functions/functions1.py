from functools import cache


__all__ = ['my_sum', 'factorial', 'my_sin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


def rounded(x):
    return round(x, 10)


def computeSeries(x, n, i_start):
    iterations = 20
    multiplier = 1
    for i in range(i_start, i_start + iterations, 2):
        multiplier *= -1
        next_term = (x**i) / factorial(i)
        n += multiplier * next_term
    return n


def my_sin(x):
    return rounded(computeSeries(x, x, 3))
