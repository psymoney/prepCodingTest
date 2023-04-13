import sys
from math import inf

input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    dp = [-inf] * (N + 1)
    for i in range(1, N+1):
        p = int(input())
        dp[i] = max(dp[i-1] + p, p)

    print(max(dp))
