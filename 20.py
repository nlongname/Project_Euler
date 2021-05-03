def digsum(n): #didn't end up using this helper function
    s = 0
    while n > 0:
        s += n%10
        n = int(n/10)
        print(s)
        print(n)
    return(s)

def factorial(n): #or this one
    p = 1
    while n > 0:
        p *= n
        n -= 1
    return(p)

def dsf(n):
    p = 1
    while n > 0: #here's the factorial
        p *= n
        n -= 1
    s = 0
    p = str(p)
    for d in p: #and here's the digit sum
        s += int(d)
    return(s)

print(dsf(100))
