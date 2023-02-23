import sys

input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
MAX_ALT = max(map(max, G))

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(x, y, rain):
    G[y][x] = rain
    for dx, dy in d:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N and G[ny][nx] > rain:
            dfs(nx, ny, rain)

def bfs(x, y, rain):
    G[y][x] = rain
    Q = [(x, y)]
    while Q:
        ox, oy = Q.pop()
        for dx, dy in d:
            nx = ox + dx
            ny = oy + dy

            if 0 <= nx < N and 0 <= ny < N and G[ny][nx] > rain:
                G[ny][nx] = rain
                Q.append((nx, ny))

areas = []
for rain in range(MAX_ALT, -1, -1):
    groups = 0
    for y in range(N):
        for x in range(N):
            if G[y][x] > rain:
                groups += 1
                bfs(x, y, rain)

    areas.append(groups)

print(max(areas))
