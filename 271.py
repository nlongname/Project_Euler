def S(n:int=13082761331670030):
    total = 0
    i= int(n**(1/3))
    x=i**3
    while i < n-1:
        if x%n==1:
            print(i)
            total += i
        x += 3*i**2+3*i+1
        x %= n
        print(x)
        i += 1
    return total
#for n in range(1,100):
#    temp = S(n**3)
#    if temp != 0:
#        print((n**3, temp))
print(S())
