"""
Hollow Right-Angle Triangle

Task: Print a hollow right-angle triangle with 5 rows, where only the border is made of stars.
Example Output:
*
**
* *
*  *
*****

"""

for i in range(1, 6):
    if i == 1 or i == 5:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")
