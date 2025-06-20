divisor = int(input("Enter a number :"))
dividend = 50
if divisor == 0:
    msg = " yesto jpt number nahana"
    raise Exception(msg)

result = dividend / divisor
print(f" The result is : {result}")
# print (" The result is ",result)
