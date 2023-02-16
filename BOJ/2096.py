import sys
input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
max_dp = [0] * 3
min_dp = [0] * 3

for i in range(3):
    max_dp[i] = nums[0][i]
    min_dp[i] = nums[0][i]

for i in range(1, N):
    max_temp = [0] * 3
    min_temp = [0] * 3
    for j in range(3):
        max_temp[j] = nums[i][j]
        min_temp[j] = nums[i][j]
        if j == 0:
            max_temp[j] += max(max_dp[j], max_dp[j+1])
            min_temp[j] += min(min_dp[j], min_dp[j+1])
        elif j == 1:
            max_temp[j] += max(max_dp)
            min_temp[j] += min(min_dp)
        else:
            max_temp[j] += max(max_dp[j], max_dp[j-1])
            min_temp[j] += min(min_dp[j], min_dp[j-1])
    max_dp = max_temp
    min_dp = min_temp

print(f'{max(max_dp)} {min(min_dp)}')
