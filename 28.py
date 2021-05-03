n=1
last = 1
total = 1 #start with the 1 in the center
while n < 1001:
    n += 2
    #n^2 - (n-2)^2 = n^2 - (n^2 -4n + 4) = 4n - 4 is the increment from the last of one spiral to the last of the next spiral (where n is the inner side length)
    #n-1 is the increment between each number in the spiral
    #total += (last + n-1) + (last + 2n - 2) + (last + 3n - 3) + (last + 4n-4), then increase n by 2
    #combining like terms:
    total += 4*last + 10*n - 10
    last += 4*n-4
print(total)
