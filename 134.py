primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]
#print(len(primes))
primes = list(dict.fromkeys(primes))
#print(len(primes))

def find_rule(n:int, addition=True, subtraction=True):
    if n%2 == 0 or n%5 == 0:
        print("Doesn't work with multiples of 2 or 5")
        return
    else:
        test=n
        last_digits = []
        if subtraction:
            last_digits.append(1)
        if addition:
            last_digits.append(9)
        while test%10 not in last_digits:
            test += n
        adding = (9 == test%10)
        if adding:
            multiplier = int((test+1)/10)
        else:
            multiplier = int(test/10)
    return((multiplier, adding))

def prime_pair_sums(limit=1000000):
    total = 0
    for i in range(len(primes)):
        if primes[i]<limit:
            p = primes[i]
            if p not in [2, 3]:
                b = primes[primes.index(p)+1]
                #if b==p:
                #    print(b, p)
                mult, add = find_rule(b,True,False)
                temp=p
                for j in range(len(str(p))):
                    #if add:
                    temp = int(temp/10)+mult*(temp%10)
                    #else:
                    #    temp = int(temp/10)-mult*(temp%10)
                answer = (b-(temp%b))*(10**len(str(p)))+p
                #if answer%b != 0 or b > 1000000:# or 1000<p<10000:
                #    print(p, b, answer, answer%b)
                total += answer
        else:
            return(total)
        if i % 1000 == 0:
            print(i)
print(prime_pair_sums())

with open('primes.txt', 'w') as filehandle:
    filehandle.writelines(str(p)+'\n' for p in primes)
