n = int(input())
nums = input().split()
sum = 0

for num in nums:
    sum += int(num)
    if sum<0:
        sum = 0
print(sum)