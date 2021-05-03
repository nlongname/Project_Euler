import math, itertools

def prime(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

primes = []
with open('primes.txt', 'r') as filehandle: #starting using a pre-calculated long list of primes, added to as needed
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

d = [n for n in range(1,10)]

def minus(big, little): #set subtraction, essentially
    if type(big) == int:
        big = str(big)
    if type(little) == int:
        little = str(little)
    return(list(map(int, filter(lambda x: str(x) not in str(little), big))))

def work(s):#check whether a string "works"
    temp = minus(d[:len(str(s))], s)
    if temp == []:
        return True
    else:
        return False

flag=False
maximum = 9
while not flag:
    for c in list(itertools.permutations(range(1,maximum+1), maximum))[::-1]:
        s = ''
        for digit in c:
            s += str(digit)
        if prime(int(s)) and not flag:
            print(int(s))
            flag = True
            break
    maximum -= 1
