"""
link: https://www.acmicpc.net/problem/1912
title: 연속합
tier: silver 2
"""
n = int(input())
seq = list(map(int, input().split()))
dp = [seq[0]] + [0] * (n-1)
for i in range(1, n):
    dp[i] = max(dp[i - 1] + seq[i], seq[i])

print(max(dp))
