# Double List Elements
# Write a function double_list that takes a list of numbers and returns a new list where each element is doubled. Use a loop instead of map().
# Example:

# Input: double_list([1, 2, 3])
# Output: [2, 4, 6]
# Input: double_list([5, 10])
# Output: [10, 20]


def double_list(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result


print(double_list([1, 2, 3]))
print(double_list([5, 10]))



# Approach 2
nums = [1, 2, 3, 4]
double_numbers = list(map(double, nums))
print(double_numbers)
