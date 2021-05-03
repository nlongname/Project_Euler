import math

a = 1
b = 1
index = 2

while math.ceil(math.log(b,10)) < 1000:
    temp = b
    b = a+b
    a = temp
    index += 1
print(index)
