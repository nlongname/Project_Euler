collatz = {}
collatz[1] = 1
n=1

def chain(n):
    if n not in collatz.keys():
        if n % 2 == 0:
            collatz[n] = 1 + chain(int(n/2))
        else:
            collatz[n] = 1 + chain(3*n+1)
    return(collatz[n])

while n <= 1000000:
    chain(n)
    n += 1
l = max(collatz.values())
for k in collatz.keys():
    if collatz[k] == l:
        print(k)
        
