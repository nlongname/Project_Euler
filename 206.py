import math

minimum = int(math.sqrt(1020304050607080900)/10)*10
maximum = int(math.sqrt(1929394959697989990)/10)*10+1
for n in range(minimum, maximum, 10):
    s = str(n**2)
    if int(s[2]) == 2 and int(s[4]) == 3 and int(s[6]) == 4 and int(s[8]) == 5 and int(s[10]) == 6 and int(s[12]) == 7 and int(s[14]) == 8 and int(s[16]) == 9:
        print(n, n**2)
    
