def champ_digit(n):
    digits = 0
    power = 1
    difference = 9 #hard-coded first difference, b/c 9 one-digit numbers
    while digits + difference < n:
        digits += difference
        power += 1
        difference = power*9*10**(power-1) #number of digits times the number of numbers
    number = int((n-digits)/power) + 10**(power-1)
    index = ((n-digits) % power)
    answer = int(str(number)[index])
    #print(answer)
    return(answer)



product = 1

for i in range(7):
    #champ_digit(i)
    product *= champ_digit(10**i-1)
print(product)
