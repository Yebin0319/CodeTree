n = int(input())
nums = [int(input()) for _ in range()]
sum = 0

for num in nums:
    sum += num
    if sum<0:
        sum = 0
print(sum)