from decimal import *
getcontext().prec=10**2
import math

def poly(x:int or float or Decimal, coefficients:list):
    ans = 0
    for i in range(len(coefficients)):
        n = -1-i
        ans += coefficients[n]*(x**i)
    return ans

def deriv(coefficients:list):
    ans = [0]*len(coefficients)
    if len(coefficients) <= 1:
        return [0]
    for i in range(len(coefficients)):
        n = -1-i
        ans[n] = coefficients[n] * i
    return ans[:-1] #last one will always be 0


def zero(coefficients:list, zero_guess=1):
    f = lambda x: poly(Decimal(x), coefficients)
    d = deriv(coefficients)
    g = lambda x: poly(Decimal(x), d)
    last = zero_guess
    x = last - f(last)/g(last)
    i = 0
    while last-x > Decimal(10)**(1-10**2):
        i += 1
        last = x
        x = x = last - f(last)/g(last)
        #print(last)
    #print(x)
    print(i)
    return x

def binary_power(power:int, base:Decimal, mod:int): #power is in binary, base assumed decimal
    a = 1
    for d in str(power):
        a = (a ** 2) % mod
        print(a)
        if int(d) == 1:
            a = (a*base) % mod
            print(a)
    return a

def to_binary(n:int): #presumed decimal
    ans = ''
    d = int(math.log(n,2))
    while n > 0:
        if 2**d <= n:
            n -= 2**d
            ans += '1'
        else:
            ans += '0'
        d -= 1
    return int(ans)

total = 0
for i in range(1,2):
    print(total)
    total += int(binary_power(to_binary(987654321), zero([1,-2**i,0,i], 2**i), 10**8))
print(total)
total = total % 10**8
print(total)
