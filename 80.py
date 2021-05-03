from decimal import *
getcontext().prec=105
total = 0
for n in range(100):
    temp = Decimal(n).sqrt()
    if int(temp) != temp:
        temp = list(filter(lambda x: x != '.', list(str(temp))))[:100]
        #print(len(temp))
        total += sum(map(int,temp))
print(total)
