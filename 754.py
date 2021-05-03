def gauss_factorial_product(n):
    answer=1
    for i in range(1,n):
        power = (n-i) - int((n - i)/i)
        print (i, power)
        answer *= i**power
    return(answer)
