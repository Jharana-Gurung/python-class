# Calculate Total with Discount
# Write a function calculate_total that takes any number of item prices and an optional discount percentage (default to 0). Return the total cost after applying the discount.
# Example:

# Input: calculate_total(10, 20, 30, discount=10)
# Output: 54 (60 - 10% of 60 = 54)
# Input: calculate_total(100, 200)
# Output: 300

def calculate_total(*prices, discount=0):
    total = 0

    for price in prices:
        total += price

    discount_amount = (discount / 100) * total

    final = total - discount_amount

    return final


print(calculate_total(10, 20, 30, discount=10))
