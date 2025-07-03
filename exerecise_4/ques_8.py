
def pattern_generator(num):
    for row in range(1, num + 1):
        for column in range(1, row * 2, 2):
            print(column, end='')
