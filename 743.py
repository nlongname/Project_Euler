def factorial(n):
    ans = 1
    while n > 0:
        ans *= n
        n -= 1
    return ans

def binomial(n,k):
    ans = 1
    countdown = n
    countup = 2 #(1 is a given)
    while countdown > k:
        ans *= countdown
        countdown -= 1
        while countup <= n-k and ans % countup == 0:
            ans = int(ans/countup)
            countup += 1
    return ans

def A(n=3, t=9):
    print(factorial(n))
