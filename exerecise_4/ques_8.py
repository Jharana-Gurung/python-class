def number_pattern(n):
    for i in range(1, n + 1):
        line = ""
        num = 1
        count = 0
        while count < i:
            if num % 2 != 0:
                line += str(num) + " "
                count += 1
            num += 1
        print(line.strip())


number_pattern(4)
