# Rectangle Area
# Create a function rectangle_area that takes two parameters, length and width
# (with width defaulting to 1), and returns the area of the rectangle.
# Example:

# Input: rectangle_area(5)
# Output: 5
# Input: rectangle_area(5, 3)
# Output: 15


def rectangle_area(length, width=1):
    area = length * width
    return area


print(rectangle_area(5))
print(rectangle_area(5, 3))
