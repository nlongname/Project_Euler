old=1
new=2
n=2

while new % 7 != 0:
    n += 1
    temp = new #save the "new" number because it's now the "old" number
    new += old #find the new "new" number
    old = temp #replace the old "old" number
    print(new)
print(n)
