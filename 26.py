nums = list(range(1,1000))
cycle = {}
#first: find terminating decimals by checking factors of 10^n
for i in range(1,10): #only need to go up to 10^9 because 2^10 > 1000
    test = 10**i 
    for n in nums:
        if test % n == 0:
            nums.pop(nums.index(n)) #toss any terminating decimals
            #print(n)
for n in nums:
    t = n
    while t % 2 == 0: #factors of 2 and 5 move repeating decimals further out without changing repetition, so get rid of them
        t = t/2
    while t % 5 == 0:
        t = t/5
    t = int(t)
    flag = True
    j=0
# if you multiply an n-digit repeating decimal by 10^n the decimal lines up in both
# subtract and you get a whole number
# so 1/d*10^n - 1/d = (1/d)*(10^n-1) is an integer if and only if d is a factor of 10^n-1
    while flag:
        j += 1
        if (10**j-1) % t == 0:
            nums.pop(nums.index(n))
            cycle[n] = j
            flag = False
m = max(cycle.values())
for n, c in cycle.items():
    if c == m:
        print(n)
