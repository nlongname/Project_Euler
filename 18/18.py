import csv
with open('input.txt', 'r') as filehandle:
    numreader = csv.reader(filehandle, delimiter=' ')
    nums = [row for row in numreader]
nums = [list(map(int, nums[n])) for n in range(len(nums))]
#print(nums)

for r in range(len(nums)):#going from the top row r=0 down, replace each entry with the max total to that point
    if r != 0:
        for c in range(r+1):
            if c == r: #rightmost "column", only one choice
                nums[r][c] += nums[r-1][c-1]
            elif c == 0: #leftmost "column, only one choice
                nums[r][c] += nums[r-1][c]
            else:
                nums[r][c] += max(nums[r-1][c], nums[r-1][c-1])
    #print(nums[r])
print(max(nums[-1]))
