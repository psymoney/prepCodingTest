import sys
input = sys.stdin.readline

dp = [0,1,1,1]

def sol(n):
    while len(dp) < n + 1:
        dp.append(dp[-2] + dp[-3])
    print(dp[n])

T = int(input())
for _ in range(T):
    sol(int(input()))
