import math

def double_base_palindromes(limit=1000000, base=2):
    total = 0
    for n in range(1,limit):
        if str(n) == str(n)[::-1]:
            b = change_base(n, base)
            if str(b) == str(b)[::-1]:
                #print(n)
                #print(b)
                total += n
    return(total)

def change_base(n, base=2):
    if n in list(range(0,base)):
        return n
    max_power = int(math.log(n, base))
    power = max_power
    ans = ''
    while len(ans) <= max_power:
        check = base**power
        new_digit = int(n/check)
        n -= new_digit * check
        ans += str(new_digit)
        power -= 1
    return(int(ans))

print(double_base_palindromes())
