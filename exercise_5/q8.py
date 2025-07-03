"""
Hollow Diamond Pattern

Task: Print a hollow diamond pattern with 5 rows in the upper half (total 9 rows), where only the border is made of stars.
Example Output:
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""

n = 5

for i in range(1, n + 1):
    spaces = n - i
    if i == 1:
        print(" " * spaces + "*")
    else:
        inner_spaces = 2 * i - 3
        print(" " * spaces + "*" + " " * inner_spaces + "*")


for i in range(n - 1, 0, -1):
    spaces = n - i
    if i == 1:
        print(" " * spaces + "*")
    else:
        inner_spaces = 2 * i - 3
        print(" " * spaces + "*" + " " * inner_spaces + "*")
