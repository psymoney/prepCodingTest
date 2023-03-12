import sys
input = sys.stdin.readline
N = int(input())
H = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(3):
        dp[i][j] = H[i-1][j]
        if j == 0:
            dp[i][j] += min(dp[i-1][1], dp[i-1][2])
        elif j == 1:
            dp[i][j] += min(dp[i-1][0], dp[i-1][2])
        else:
            dp[i][j] += min(dp[i-1][0], dp[i-1][1])
print(min(dp[N]))
