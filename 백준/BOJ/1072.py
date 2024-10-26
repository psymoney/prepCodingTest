"""
link: https://www.acmicpc.net/problem/1072
title: 게임
tier: silver 3
"""
"""
dx -> must increase
dy -> when dx increase by 1, increase by 1 -> never going to lose

the case variable z is never going to be changed is when z is already 100 which means x == y

every increase in x affects to z
the order of win or lose is important
"""
x, y = map(int, input().split())
if x == y:
    print(-1)
else:
    z = int(y / x * 100)
    dx = 0
    while int(y / (x + dx) * 100) == z:
        dx += 1
        y += 1
    print(dx)
