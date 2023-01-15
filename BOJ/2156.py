import sys
input = sys.stdin.readline

n = int(input())

arr = [0]
dp = [0] * (n+1)
for _ in range(n):
    arr.append(int(input())) 
dp[1] = arr[1]

if n >= 2:
    dp[2] = dp[1] + arr[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i-1], arr[i] + max(dp[i-2], dp[i-3] + arr[i-1]))

print(dp[-1])
