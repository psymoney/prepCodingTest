import sys
input = sys.stdin.readline

N = int(input())

dp = [0, 3, 7]
while len(dp) < N + 1:
    dp.append((2*dp[-1] + dp[-2]) % 9901)
print(dp[N])
