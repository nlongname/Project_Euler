import math
record = {}
sums={0:0, 1:0}

def div(n):#proper divisors this time
    if n in record.keys():
        return record[n]
    i = 2
    div_list = []
    while i <= (math.sqrt(n)):
        if n % i == 0:
            div_list.append(i)
            if n/i != i:
                div_list.append(int(n/i))
        i += 1
    div_list.append(1)
    div_list.sort()
    record[n] = div_list
    return(div_list)

def div_sum(n):#just proper divisors, no record of which ones
    if n in sums.keys():
        return sums[n]
    i=2
    total=1 # 1 is always a proper divisor (assuming n != 1, which we hardcoded)
    while i <= math.sqrt(n):
        if n % i == 0:
            total += i
            if n/i != i:
                total += int(n/i)
        i += 1
    sums[n] = total
    return(total)

def amic_chain(n:int, limit=1000000):
    old = n
    chain = [old]
    new = div_sum(n)
    while new not in chain and new <= limit:
        chain.append(new)
        old = chain[-1]
        new = div_sum(new)
    if new == chain[0]:
        return chain
    else:
        return False

def longest_chain(limit=1000000):
    skip = []
    max_len = 0
    candidate = 0
    for n in range(2,limit+1):
        if n % 10000 == 0:
            print(n)
        chain = amic_chain(n, limit)
        if chain:
            if len(chain) > max_len:
                print(chain, len(chain))
                max_len = len(chain)
                candidate = min(chain)
    return candidate

longest_chain()

#for n in range(1000000):
#    div_sum(n)
#    if n % 10000==0:
#        print(n)
#print(len(sums))
