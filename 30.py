import math
n = 10 #may as well skip 1-digit numbers
total = 0
while n < 10**6: #6*9^5 < 999,999, so this is a hard upper limit
    check = 0
    for d in str(n):
        check += (int(d)**5)
    #l = math.log(n,10) #keep track of progress
    #if int(l) == l:
        #print(n)
    if check == n:
        total += n
        print(n)
    n += 1
print("total is: "+str(total))
