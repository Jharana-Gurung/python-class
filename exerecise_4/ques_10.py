def filter_range(lst, min_val, max_val):
    result = []
    for num in lst:
        if min_val <= num <= max_val:
            result.append(num)
    return result


print(filter_range([1, 5, 3, 8, 2], 2, 5))
