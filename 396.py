import math, time

def convert_to(n, b): #decimal to listified b-base number
    power = int(math.log(n,b))
    result = []
    if n == 0:
        return result
    while power >= 0:
        if power == 0:
            result.append(n)
            break
        else:
            next_digit = int(n/(b**power))
            n -= next_digit*b**power
            result.append(next_digit)
            power -= 1
    result.reverse()
    return result

def interpret_as(l, b):#interpreting one of these list-numbers back to decimal
    result = 0
    l.reverse()
    for d in l:
        result *= b
        result += d
    return result


def round_trip(n, b):
    l = convert_to(n,b)
    print(l)
    returned = interpret_as(l,b)
    print(returned)
    return(returned==n)

def decrement(l, b=None):
    index=0
    while l[index]==0:
        if b==None:
            print(l, b)
        l[index]=b-1
        index += 1
    l[index] -= 1
    while len(l) > 0 and l[-1] == 0:
        l = l[:-1]
    return l

def goodstein_step(l,b): #b is the last base we used, which is the same number as the next term we're generating
    if type(l)==int:
        l = convert_to(l, b)
    new = decrement(l, b+1)
    b += 1
    return(new, b)

def goodstein_sequence(n):
    count = 1 #first term is just n
    b = 2
    l = convert_to(n,b)
    while l != []:
        l, b = goodstein_step(l, b)
        print(l, count)
        if l != []:
            count += 1
    return count

def reduce_power_of_two(n,d):
    return (n-d)%(4*5**d-1)+d

def goodstein_skip(n):
    b = 2
    l = convert_to(n,b)
    b = 3
    count = 0
    doublej=True
    #402653181
    while l != []:
        if l[0]==l[1]==0 and l[2] != 0 and doublej: #if last two digits are 0, we can skip to the next time that happens
            l = [0,0]+decrement(l[2:], b)
            doublejump = b*(2**reduce_power_of_two(b,9)-1)
            count += doublejump
            count %= 10**9
            b += doublejump
            print(l, b)
            if sum(l)==0:
                return count
        elif l[0] == 0: #if the last digit is 0, we can skip ahead to the next time the last digit is 0 by using the numbers we'll get if we subtract 1
            l = [0] + decrement(l[1:], b)
            count += b
            b += b
            print(l, count)
            if sum(l) == 0:
                return count
        elif len(l) == 1:
            count += l[0]
            return count
        else: #if we can't do anything else, subtract until the last digit is 0, add the same to the base
            count += l[0]
            b += l[0]
            l[0]=0
            #print(l, count)
    return count

def goodstein_sum(n):
    total = 0
    for i in range(1,n+1):
        total += goodstein_sequence(i)
    return(total)
base=2
test=base
power=1
store=[]
start_time = time.time()
while test not in store:
    store.append(test)
    test *= base
    test = test % 10**9
    power += 1
    if power % 10**4 == 0:
        print(power)
    #print(test)
print(len(store))
print(time.time()-start_time, "seconds")
