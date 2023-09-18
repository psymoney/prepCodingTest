"""
link: https://www.acmicpc.net/problem/2206
title: 벽 부수고 이동하기
tier: gold 3
"""
"""
algorithm: DFS
movement count includes start and end points either
if breaking one wall makes the way shorter, can break up to one wall to move
able to move towards up, down, left, right
make a program calculating the shortest movement given map

restrictions:
1 <= N, M <= 1000
(1,1) and (N,M) are always 0

output:
print the shortest way
if not available, print -1

구분해야 하는 것
1. 벽을 부숴 방문한 노드와 벽을 부수지 않고 방문한 노드
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [list(map(int, input().strip())) for _ in range(N)]
D = [(0, -1), (0, 1), (-1, 0), (1, 0)] # up, down, left, right
ans = 10 ** 8 + 1
T = deque([(0, 0, 0, 1)])
MAP[0][0] = -1

while len(T) > 0:
    x, y, cnt, b = T.popleft()
    cnt += 1

    if x == M - 1 and y == N - 1:
        ans = min(cnt, ans)

    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and cnt < MAP[ny][nx]:
            v = MAP[ny][nx]
            if v == 0:
                MAP[ny][nx] = cnt
                T.append((nx, ny, cnt, b))
            elif v == 1 and b == 1:
                MAP[ny][nx] = cnt
                T.append((nx, ny, cnt, b - 1))

print(ans) if ans != 10 ** 8 + 1 else print(-1)

