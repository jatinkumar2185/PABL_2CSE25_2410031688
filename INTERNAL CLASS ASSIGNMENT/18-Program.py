#Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n. 

def factorial(n):
    result = [1]
    carry = 0

    while i in range(2, n+1):
        prod = result[i]