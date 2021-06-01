# https://projecteuler.net/problem=751
# Generate a series of integers with this procedure:
# b_1 = theta; b_n = floor(b_(n-1)) * [b_(n-1) - floor(b_(n-1))+1] if n >= 2
# a_n = floor(b_n)
# Then we concatenate each a_n as a decimal i.e. [2, 3, 5, 8] -> 2.358
# Find the only value of theta where a_1 = 2 and our starting value equals
# the concatenation at the end

from decimal import Decimal

# originally planned on trying every next digit to see which works, but I
# missed that you can add more than one digit if floor(b_(n-1)) > 10
def find_next_digit_faulty(n:Decimal) -> Decimal: #only works if the next number is 1 digit, need to totally rewrite
    print(n)
    if type(n) != Decimal:
        n = Decimal(str(n))
    digits = [int(d) for d in str(n) if d.isnumeric()]
    for i in range(10):
        temp = n+i*Decimal(10)**power
        working = True
        for d in digits+[i]:
            floor = temp // 1
            if floor != d:
                working = False
                break
            multiplier = 1 + temp%1
            temp = (floor*multiplier)
        if working:
            return n+i*Decimal(10)**power
    return False

# So what we do is continue the sequence one further than the digits we have
# each time, then start over with the new digits we gained
# e.g. 2.23 gives us [2,2,3,5] so we restart with 2.235 and get [2,2,3,5,6]
def continue_number(n:Decimal) -> Decimal:
    s = str(n)
    if type(n) != Decimal:
        n = Decimal(s)
    temp = n
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            floor = temp // 1
            if not s[i:].startswith(str(floor)):
                return False
            i += len(str(floor))
            multiplier = temp%1 + 1
            temp = floor*multiplier
        else:
            i += 1
    floor = temp // 1
    if len(s) == 1:
        return Decimal(s+'.'+str(floor))
    else:
        return Decimal(s+str(floor))
            

answer = Decimal(2)
while len(str(answer)) < 27:
    answer = continue_number(answer)
    #print(answer)
print(round(answer, 24))
