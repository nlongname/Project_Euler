record = {1: False, 89: True}
nope=[]
    
def square_digit_chains(limit=10000000):
    count = 0
    for n in range(1,568):#567 is the maximum you can get through this process while n<10,000,000
        chain = []
        new = n
        while new not in record.keys() and new not in chain:
            chain.append(new)
            new = sum(map(lambda x: int(x)**2, str(new)))
        #print(new, record[new])
        if record[new]:
#            count += 1
            for c in chain:
                record[c]=True
            if n % 1000000 == 0:
                print(f"{count} out of {n}, {count/n*100}%")
        else:
            for c in chain:
                record[c] = False
    for n in range(1,limit):
        if n % 1000000==0:
            print(f"{count} out of {n}, {count/n*100}%")
        if n in record.keys() and (not record[n]):
            nope.append(n)
            #print(n)
        elif n <568:
            count += 1
        else:
            new = sum(map(lambda x: int(x)**2, str(n)))
            if new not in nope:
                count += 1
    return(count)

print(square_digit_chains())
