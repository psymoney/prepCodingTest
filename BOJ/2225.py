import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [[0] * (N+1)] + [[1] + [0] * N for _ in range(K)]

for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])
