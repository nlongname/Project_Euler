months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def ly(y): #leap year test
    return(y%400 == 0 or (y%4 == 0 and not y%100 == 0))

def sundays(enddate=2001, offset=2, startdate=1901): #offset is 2 because Jan 1 1901 was a Tuesday, 3rd day of the week but 0-indexed
    total = 0
    for y in range(startdate, enddate):
        for m in range(12):
            if offset == 0:
                total += 1
                print(m+1)
            offset += months[m]
            if m == 1 and ly(y): #if it's Feb and a Leap Year add 1
                offset += 1
            offset = offset%7
    return(total)

print(sundays(1902,1,1901))
