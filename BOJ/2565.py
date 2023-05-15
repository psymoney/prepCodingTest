import sys
from itertools import combinations
from math import inf

input = sys.stdin.readline

N, M = map(int, input().split())
woks = list(map(int, input().split()))

dp = [inf] * N + [0]
cases = [wok for wok in woks]
if len(woks) != 1:
    comb = list(combinations(woks, 2))
    for c in comb:
        cases.append(sum(c))

cases.sort()

for i in range(N, 0, -1):
    for t in cases:
        if i - t < 0:
            break
        dp[i - t] = min(dp[i - t], dp[i] + 1)

print(dp[0]) if dp[0] != inf else print(-1)