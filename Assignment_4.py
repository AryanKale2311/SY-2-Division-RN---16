"""
Fibonacci Sequence Calculator
Demonstrates both Memoization (Top-Down) and Tabulation (Bottom-Up) approaches.
Indexing used: fib(1) = 0, fib(2) = 1, fib(3) = 1, fib(4) = 2, ...
"""


def fibonacci_memoization(n, cache=None):
    """Top-down approach using recursion + caching (memoization)."""
    if cache is None:
        cache = {}

    if n <= 0:
        return None
    if n in cache:
        return cache[n]
    if n <= 2:
        return n - 1  # fib(1) = 0, fib(2) = 1

    cache[n] = fibonacci_memoization(n - 1, cache) + fibonacci_memoization(n - 2, cache)
    return cache[n]


def fibonacci_tabulation(n):
    """Bottom-up approach using an iterative loop + table."""
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1

    table = [0] * (n + 1)
    table[1] = 0
    table[2] = 1

    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]


def main():
    try:
        n = int(input("Enter the value of n to find the nth Fibonacci number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if n <= 0:
        print("Please enter a positive integer.")
        return

    memo_result = fibonacci_memoization(n)
    tab_result = fibonacci_tabulation(n)

    print(f"\nUsing Memoization (Top-Down): fib({n}) = {memo_result}")
    print(f"Using Tabulation  (Bottom-Up): fib({n}) = {tab_result}")


if __name__ == "__main__":
    main()