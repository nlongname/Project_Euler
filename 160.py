import math

def factorial_trail(limit:int=10, d:int=5):
    product = 1
    for n in range(1,limit+1):
        while n%10==0:
            n /= 10
        n = int(n)
        product *= n
        while product%10==0:
            product /= 10
        product = int(product)
        product %= (10**(3*d))
    product %= 10**d
    return int(product)

#print(factorial_trail())

for j in range(100000):
    a = int(str(math.factorial(j)).strip('0')[-5:])
    b = factorial_trail(j)
    if a != b:
        print(j, a, b)
