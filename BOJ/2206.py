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

# input lines for parameters
N, M = map(int, input().split())
MAP = [list(map(int, input().strip())) for _ in range(N)]

# initiation of required data
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
D = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # x,y set for directional movement for respectively up, down, left, and right
ans = 10 ** 8 + 1
T = deque([(0, 0, 0)])  # a queue for dfs meaning respectively x, y, breached count

while len(T) > 0:
    x, y, b_cnt = T.popleft()
    m_cnt = visited[b_cnt][y][x] + 1   # movement count

    if x == M - 1 and y == N - 1:
        ans = min(m_cnt, ans)

    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            v = MAP[ny][nx]
            if v == 0:
                if visited[b_cnt][ny][nx] == 0:
                    visited[b_cnt][ny][nx] = m_cnt
                    T.append((nx, ny, b_cnt))
                elif m_cnt < visited[b_cnt][ny][nx]:
                    visited[b_cnt][ny][nx] = m_cnt
                    T.append((nx, ny, b_cnt))
            elif v == 1:
                if b_cnt == 0:
                    # the case breaching the wall at (x, y)
                    if visited[b_cnt + 1][ny][nx] == 0:
                        visited[b_cnt + 1][ny][nx] = m_cnt
                        T.append((nx, ny, b_cnt + 1))
                    elif m_cnt < visited[b_cnt + 1][ny][nx]:
                        visited[b_cnt][ny][nx] = m_cnt
                        T.append((nx, ny, b_cnt))

print(ans) if ans != 10 ** 8 + 1 else print(-1)

