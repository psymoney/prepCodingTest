"""
link: https://www.acmicpc.net/submit/4811/66557804
title: 알약
tier: gold 5
"""
import sys
input = sys.stdin.readline
DP = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    DP[0][i] = 1

for w in range(1, 31):
    for h in range(w, 31):
        DP[w][h] = DP[w-1][h] + DP[w][h-1]

for _ in range(1000):
    N = int(input())
    if N == 0:
        break
    print(DP[N][N])
