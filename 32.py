import itertools

d = [n for n in range(1,10)] #set of all the digits we need, for convenience

def minus(big, little) -> list: #removing all the digits in 'big' that are in 'little'
    if type(big) == int: #easier to use if it's very type-neutral
        big = str(big)
    if type(little) == int:
        little = str(little)
    return(list(map(int, filter(lambda x: str(x) not in str(little), big))))

def work(a,b):
    if len(str(a))+len(str(b))+len(str(a*b)) != 9:
        return False #only bother checking if they're the right length to work
    temp = minus(d, a)
    temp = minus(temp, b)
    temp = minus(temp, a*b)
    if temp == []:
        return True
    else:
        return False

successes=[]
for a in range(1,10000):
    for b in range(int(10000/a)):
        if work(a,b):
            if a*b not in successes:
                successes.append(a*b)
print(sum(successes))
