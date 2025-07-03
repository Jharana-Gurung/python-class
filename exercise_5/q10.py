"""
Zigzag Pattern

Task: Print a zigzag pattern of stars across 5 rows, with stars forming a diagonal path.
Example Output:
*    
   * 
*    
   * 
*    

"""


def zigzag_pattern(rows):
    for i in range(0, rows):
        if i % 2 == 0:
            print("*")
        else:

            print(" *")


zigzag_pattern(5
)
