import csv
with open('p067_triangle.txt', 'r') as filehandle:
    numreader = csv.reader(filehandle, delimiter=' ')
    nums = [row for row in numreader]
nums = [list(map(int, nums[n])) for n in range(len(nums))]
#print(nums)

for r in range(len(nums)):
    if r != 0:
        for c in range(r+1):
            if c == r:
                nums[r][c] += nums[r-1][c-1]
            elif c == 0:
                nums[r][c] += nums[r-1][c]
            else:
                nums[r][c] += max(nums[r-1][c], nums[r-1][c-1])
    #print(nums[r])
print(max(nums[-1]))
