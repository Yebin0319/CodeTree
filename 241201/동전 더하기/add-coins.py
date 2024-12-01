inputs = input().split()
n = int(inputs[0])
k = int(inputs[1])
values = [int(input()) for i in range(n)]

ans = 0

for coin in values[::-1]:
    ans += k // coin
    k %= coin
print(ans)