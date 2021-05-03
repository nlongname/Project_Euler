import itertools

#primes = []
#with open('primes.txt', 'r') as filehandle:
#    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

first_primes = [2, 3, 5, 7, 11, 13, 17] #the specific primes mentioned in the problem
ans=[]
for c in list(itertools.permutations(range(10))):
    s = ''
    for digit in c:
        s += str(digit)
    flag = True
    n=0
    while flag and n < len(first_primes):
        if int(s[n+1:n+4]) % first_primes[n] != 0:
            flag=False
        n += 1
    if flag:
        ans.append(int(s))
        print(int(s))
print("sum: "+str(sum(ans)))
