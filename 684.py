import math
mod = 1000000007

def S(k:int):
    d = int(k/9)
    r = k-9*d
    total = 0
    temp = 0
    for i in range(d):
        temp += 10**i
    total += temp*45 #adding the 123456789 for each digit we're past
    temp = 0
    for i in range(1,d):
        temp *= 10
        temp += i
    total += temp*9*9 #adding all the excess 9's once we've passed them on the digits we're past
    total += (10**d-1)*r #adding the 9...9 for the ones we're in the middle of
    total += int(r*(r+1)/2)*10**d #adding the 123... for the ones we're in the middle of
    return(total)

fib = [0, 1]
for i in range(2,91):
    fib.append(fib[-1]+fib[-2])
print(fib)

total = 0
for f in fib[2:]:
    total += S(f)
    total %= 1000000007
    print(fib.index(f), f, total)
