"""
Pascal’s Triangle Pattern

Task: Print the first 5 rows of Pascal’s triangle using numbers.
Example Output:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def binomial_coeff(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


rows = 5
for i in range(rows):
    print(" " * (rows - i), end="")
    for j in range(i + 1):
        print(binomial_coeff(i, j), end=" ")
    print()
