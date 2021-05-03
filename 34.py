factorial = [1]
for i in range(1,10):
    factorial.append(i*factorial[i-1])

results=[]
n=10
while n < 10000000:
    digits = list(str(n))
    digits = map(int, digits)
    s = 0
    for d in digits:
        s += factorial[d]
    if s == n:
        print(n)
        results.append(n)
    n += 1
print("total is: "+str(sum(results)))
