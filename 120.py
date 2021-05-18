# https://projecteuler.net/problem=120
# r is the remainder when (a-1)^n + (a+1)^n is divided by a^2
# r_max is the max remainder for any n for a given a
# find the sum of r_max for each a 3<=a<=1000

# pencil and paper background:
# (a-1)^n and (a+1)^n have a lot of terms in common
# e.g. n=5: a^5 - 5a^4 + 10a^3 - 10a^2 + 5a - 1
# versus    a^5 + 5a^4 + 10a^3 + 10a^2 + 5a + 1
# when you add them, you're left with all the odd powers if n is odd
# or even if n is even: 2a^5 + 20a^3 + 10a
# all higher powers are divisible by a^2, so the only remainder is from 10a
# more generally, 2*n*a (n odd), so they increase by 4a each time
# even n's can be ignored because the remainder is always 2 (e.g. 2a^4 + 12a^2 + 2)

def max_remainder(a:int):
    remainders = []
    a_sq = a**2
    # so all you need to do is find 2*a % a^2
    temp = 2*a % a_sq
    while temp not in remainders:
        remainders.append(temp)
        # then keep adding 4*a (mod a^2) until it repeats (it always will)
        temp = remainders[-1] + 4*a
        temp %= a_sq
    return max(remainders) # and take the max

l = [max_remainder(x) for x in range(2,1001)]
print(sum(l))
#333082500
