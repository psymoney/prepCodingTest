import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
D = [(0, -1), (-1, 0), (0, 1), (1, 0)]
glacial = deque

for y in range(1, N - 1):
    for x in range(1, M - 1):
        if G[y][x] > 0:
            glacial.append((x, y))

year = 1
bunches = 0
V = [[0] * M for _ in range(N)]
while glacial:
    x, y = glacial.popleft()
    if V[y][x] != 0 or G[y][x] == 0:
        continue

    seas = 0
    Q = deque()
    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if G[ny][nx] == 0:
                seas += 1
            else:
                Q.append((nx, ny))
    V[y][x] = seas






    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if G[y][x] == 0:
                continue
            if V[y][x] != 0:
                continue

            num_seas = 0
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and G[ny][nx] == 0:
                    num_seas += 1
            V[y][x] = G[y][x] - num_seas if num_seas <= G[y][x] else 0

            Q = deque()
            Q.append((x, y))
            bunches += 1
            if bunches >= 2:
                print(year)
                quit()
            while Q:
                x2, y2 = Q.popleft()
                for dx, dy in D:
                    nx, ny = x2 + dx, y2 + dy
                    if 0 <= nx < M and 0 <= ny < N and V[ny][nx] == 0 and G[ny][nx] > 0:
                        Q.append((nx, ny))

                        num_seas = 0
                        for dx2, dy2 in D:
                            nx2, ny2 = x2 + dx2, y2 + dy2
                            if 0 <= nx2 < M and 0 <= ny2 < N and G[ny2][nx2] == 0:
                                num_seas += 1

                        V[ny][nx] = G[ny][nx] - num_seas if num_seas <= G[ny][nx] else 0
    if bunches == 0:
        print(0)
        quit()
    G = V
    year += 1







