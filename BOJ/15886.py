"""
link: https://www.acmicpc.net/problem/15886
title: 내 선물을 받아줘 2
tier: silver 3
"""
N = int(input())
P = str(input())
r = 0
gifts = 0

while r < N:
    r += 1
    if r == N:
        gifts += 1
    else:
        if P[r-1] == "W" and P[r] == "E":
            gifts += 1

print(gifts)

