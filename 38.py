import itertools

d = [n for n in range(1,10)]

def minus(big, little): #set subtraction, essentially
    if type(big) == int:
        big = str(big)
    if type(little) == int:
        little = str(little)
    return(list(map(int, filter(lambda x: str(x) not in str(little), big))))

def work(s): #terrible function name, but it's checking whether a set of multiples "works"
    if len(s) != 9:
        return False
    temp = minus(d, s)
    if temp == []:
        return True
    else:
        return False

maximum=0
for a in range(1,10000):
    if len(minus(d, a)) == len(d)-len(str(a)): #no repeated digits in the original number
        ans = ''
        temp = str(a)
        n=1
        while len(temp) + len(ans) <= 9:
            ans += temp
            n += 1
            temp = str(n*a)
        if work(ans):
            if int(ans) > maximum:
                maximum = int(ans)
print(maximum)
