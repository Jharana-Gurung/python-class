"""
Diamond Pattern

Task: Print a diamond pattern of stars with 5 rows in the upper half (total 9 rows).
Example Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""


for i in range(1, 6):
    spaces = 5 - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


for i in range(4, 0, -1):
    spaces = 5 - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
