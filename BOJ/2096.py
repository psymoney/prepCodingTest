import sys
input = sys.stdin.readline

N = int(input())
max_dp = [[0] * 3 for _ in range(N)]
min_dp = [[0] * 3 for _ in range(N)]
for i in range(N):
    nums = input()
    max_dp[i] = list(map(int, nums.split()))
    min_dp[i] = list(map(int, nums.split()))

for i in range(1, N):
    for j in range(3):
        if j == 0:
            max_dp[i][j] += max(max_dp[i-1][j], max_dp[i-1][j+1])
            min_dp[i][j] += min(min_dp[i-1][j], min_dp[i-1][j+1])
        elif j == 1:
            max_dp[i][j] += max(max_dp[i-1])
            min_dp[i][j] += min(min_dp[i-1])
        else:
            max_dp[i][j] += max(max_dp[i - 1][j], max_dp[i - 1][j - 1])
            min_dp[i][j] += min(min_dp[i - 1][j], min_dp[i - 1][j - 1])

print(f'{max(max_dp[-1])} {min(min_dp[-1])}')
