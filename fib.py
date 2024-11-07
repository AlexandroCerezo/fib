import argparse


def fibonacci_iterative(n: int) -> int:
    """
    Computes the n-th fibonacci number
    :param n: the n-th Fibonacci number
    :return: the n-th Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be a number higher or equal than 0")
    if n < 2:
        return n
    n0 = 0
    n1 = 1
    nth = 0
    for i in range(n - 1):
        nth = n0 + n1
        n0 = n1
        n1 = nth
    return nth


cache = {}


def fibonacci_recursive(n: int) -> int:
    """...
    """
    if n < 0:
        raise ValueError("n must be a number greater or equal to 0")
    if n < 2:
        return n

    if n in cache:
        return cache[n]

    nth = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    cache[n] = nth

    return nth


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('nth', type=int, help="Nth Fibonacci number,")
    args = parser.parse_args()

    result = fibonacci_iterative(args.nth)
    print(result)
