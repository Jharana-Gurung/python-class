def products(*args):
    product = 1

    for item in args:
        product = product * item
    return product


output = products(9, 8, 7)
print(output)
