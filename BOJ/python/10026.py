"""
link: https://www.acmicpc.net/problem/10026
title: 적록색약
tier: gold 5
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
paint = [list(input().rstrip()) for _ in range(N)]

D = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # delta, respectively up, down, left and right
visited = [[0] * N for _ in range(N)]
area = [0, 0]


def count_area(i, j, c):
    global D, N, paint, visited
    Q = deque([(i, j, c)])

    while Q:
        x, y, colors = Q.popleft()

        for dx, dy in D:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if paint[ny][nx] in colors and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    Q.append((nx, ny, colors))


for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            area[0] += 1
            visited[y][x] = 1
            color = paint[y][x]
            count_area(x, y, color)

visited = [[0] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            area[1] += 1
            visited[y][x] = 1
            color = paint[y][x] if paint[y][x] == 'B' else 'RG'
            count_area(x, y, color)

print(' '.join(map(str, area)))





