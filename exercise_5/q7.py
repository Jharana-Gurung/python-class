"""
Number Triangle Pattern

Task: Print a right-angle triangle where each row contains the row number repeated.
Example Output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

for i in range(1, 6):
    print((str(i) + " ") * i)
