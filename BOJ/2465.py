import sys
sys.setrecursionlimit(1000 * 1000)

input = sys.stdin.readline

N = int(input())
MAX_ALT = 0
G = []

for _ in range(N):
    g = list(map(int, input().split()))
    MAX_ALT = max(g) if max(g) > MAX_ALT else MAX_ALT
    G.append(g)

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(x, y, visited, rain):
    visited[y][x] = 1
    for dx, dy in d:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N and G[ny][nx] > rain and visited[ny][nx] == 0:
            dfs(nx, ny, visited, rain)

areas = []
for rain in range(0, MAX_ALT + 1):
    visited = [[0] * N for _ in range(N)]
    groups = 0
    for y in range(N):
        for x in range(N):
            if G[y][x] > rain and visited[y][x] == 0:
                groups += 1
                dfs(x, y, visited, rain)

    areas.append(groups)

print(max(areas))
