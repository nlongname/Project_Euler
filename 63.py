import math

digits = list(range(2,10))
n=1
minimum = 1
maximum = 10
count=1
archive = [1]
temp_digits = list(range(2,10))
while digits != []:
    for d in digits:
        if math.log(minimum, d) < n < math.log(maximum, d):
            count += 1
            archive.append(d**n)
            print(f"{d}^{n} = {d**n} which has {1+int(math.log(d**n,10))} digits")
        else:
            temp_digits.remove(d)
            #print(d)
    minimum *= 10
    maximum *= 10
    n += 1
    digits = temp_digits[::1]
print(len(archive))
