import sys
input = sys.stdin.readline

N = int(input())
max_dp = [0] * 3
min_dp = [0] * 3

for i in range(N):
    nums = list(map(int, input().split()))
    if i == 0:
        for k in range(3):
            max_dp[k] = nums[k]
            min_dp[k] = nums[k]
    else:
        max_temp = [0] * 3
        min_temp = [0] * 3
        for j in range(3):
            max_temp[j] = nums[j]
            min_temp[j] = nums[j]
            if j == 0:
                max_temp[j] += max(max_dp[j], max_dp[j + 1])
                min_temp[j] += min(min_dp[j], min_dp[j + 1])
            elif j == 1:
                max_temp[j] += max(max_dp)
                min_temp[j] += min(min_dp)
            else:
                max_temp[j] += max(max_dp[j], max_dp[j - 1])
                min_temp[j] += min(min_dp[j], min_dp[j - 1])
        max_dp = max_temp
        min_dp = min_temp

print(f'{max(max_dp)} {min(min_dp)}')
