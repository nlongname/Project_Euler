def d(n):
    i = 2
    div = [1]
    while i <= (n/2):
        if n % i == 0:
            div.append(i)
        i += 1
    return(sum(div))

abundant = []
limit = 28123
for n in range(1, limit):
    if d(n) > n:
        abundant.append(n)
    if n % 1000 == 0:
        print(n)
print(len(abundant))
nums = list(range(28125))

for a in abundant:
    for b in abundant[abundant.index(a):]:
        if a+b in nums:
            nums.pop(nums.index(a+b))
print(sum(nums))
