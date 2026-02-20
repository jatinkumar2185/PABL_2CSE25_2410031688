#Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.


def factorial_digits(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i

    # convert number into list of digits
    return [int(d) for d in str(fact)]

# Examples
print(factorial_digits(5))   # [1, 2, 0]
print(factorial_digits(10))  # [3, 6, 2, 8, 8, 0, 0]
print(factorial_digits(1))   # [1]
