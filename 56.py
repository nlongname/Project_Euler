def power_digits(limit=100):
    best = (0, 0)
    best_sum = 0
    for a in range(2,limit):
        for b in range(1,limit):
            temp = sum(map(int, str(a**b)))
            if temp > best_sum:
                best = (a, b)
                best_sum = temp
                #print(a, b, a**b, temp)
        print(best, best_sum)
    return(best_sum)
print(power_digits(1000))
