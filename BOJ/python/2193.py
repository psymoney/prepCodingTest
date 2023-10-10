import sys


n = int(sys.stdin.readline())
dp = [0, 1]

for _ in range(n - 1):
    dp[0], dp[1] = dp[0] + dp[1], dp[0]

print(sum(dp))
